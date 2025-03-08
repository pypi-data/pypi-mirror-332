# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:02:04 2023

@author: lookingout

Reference
---------
[1] 王志强, 齐佩金 & 刘丽巍. 解读巴塞尔协议Ⅱ中内部评级法关于资本要求的计算. 
    数理统计与管理 125–131 (2007) doi:10.13860/j.cnki.sltj.2007.01.022.
    
[2] 杨子晖 & 李东承. 我国银行系统性金融风险研究——基于“去一法”的应用分析. 经济研究 53, 36–51 (2018).

[3] De Lisa, R., Zedda, S., Vallascas, F., Campolongo, F. & Marchesi, M. 
    Modelling Deposit Insurance Scheme Losses in a Basel 2 Framework. 
    J Financ Serv Res 40, 123–141 (2011).
    
# 函数中货币单位均为 亿美元
-------    

"""
import pandas as pd
import numpy as np
from scipy.optimize import fsolve
from scipy.stats import norm, chi2
from scipy.integrate import quad
from tqdm import tqdm
import os

def binary_solve(func, left, right, tol = 1e-6, max_iter = 99999):
    # https://zhuanlan.zhihu.com/p/136823356
    error = tol + 1  # 循环开始条件
    cur_root = left
    count = 1
    if func(left) * func(right) > 0:
        _ = ''.join(["func(", str(left) ,") = ", str(func(left)) ,'\n',
                     "func(", str(right),") = ", str(func(right))])
        raise ValueError(_)
    while count < max_iter:
        if error < tol:
            return left
        else:
            middle = (left + right) / 2
            if (func(left) * func(middle)) < 0:
                right = middle
            else:
                left = middle
            cur_root = left
        error = abs(func(cur_root))
        count += 1
    raise Exception(f"error = {error}")
    

def _B(PD):
    _ = (0.11852 - 0.05478 * np.log(PD)) ** 2
    return _

def _R(PD, S, asset):
    """
    当银行的总资产超过 1000 亿美元时需要乘以 1. 25,因此R是asset的函数
    """
    m = 1 if (asset < 1000) else 1.25
    r = 0.12 * (1 - np.exp( -50 * PD)) / (1 - np.exp(-50)) +\
        0.24 * (1 - (1 - np.exp( -50 * PD)) / (1 - np.exp(-50))) -\
        0.04 * (1 - (S - 5)/45)
    return m * r
            
def CAR(PD, LGD = 0.45, M = 2.5, S = 50, z = 0.999 ,asset = 999):
    
    """
    CAR:Capital Adequacy Ratio
    
    PD: 资产k的隐含违约率
    LGD: 违约损失率
    M: 期限
    S: 规模
    """
    PD, LGD, M, S, z, asset = float(PD), float(LGD), float(M), float(S), float(z), float(asset)
    # assert 0 < z < 1, f"z = {z}"
    # assert 0 < PD < 1, f"PD = {PD}"
    
    rkwds = [PD , S, asset]
    q =  np.sqrt(1 / (1 - _R(*rkwds))) * norm.ppf(PD) + \
        np.sqrt(_R(*rkwds) / (1 - _R(*rkwds))) * norm.ppf(z)
    # print(q)
    _ = (LGD * norm.cdf(q) - PD * LGD) * (1 + (M - 2.5) * _B(PD)) * \
        (1 / (1 - 1.5 * _B(PD))) * 1.06
    return _

def estimate_pd(bd):
    def func(d):
        # print(0.08 * d["risk_weighted_assets"] / d["total_assets"])
        _f = lambda pd: 0.08 * d["risk_weighted_assets"] / d["total_assets"]\
            - CAR(pd, LGD = 0.45, M = 2.5, S = 50, asset = d["total_assets"])#TODO:这里和文章不一样，文章是写错了吧,CAR乘总资产才能和rwa放一起
        # r =  fsolve(_f, [0.001], xtol=1e-6 )[0]
        # print("r = ", r)
        # if r < 1e-8:r = 1e-8
        if (_f(1e-6) < 0) or (_f(0.1) > 0):
            print("pd estimate error:" ,d.name, " _f ", _f(1e-6), _f(0.1))
            return np.nan
        else:
            r = binary_solve(_f, 1e-6, 0.1)
            return r
    bd["pd"] = bd.apply(func, axis = 1)
    bd = bd.dropna()
    return bd

# def _loss(bd, loss_corr):
#     N = len(bd)
#     zcov = (np.zeros((N, N)) + loss_corr) + np.eye(N) * (1 - loss_corr)
#     # zcov_inv = np.linalg.inv(zcov)
#     # while True:
#     #     zi = np.random.multivariate_normal(mean = np.zeros(N), cov = zcov)
#     #     if  zi.reshape(1,-1) @ zcov_inv @ zi.reshape(-1,1) > chi2.pdf(0.9, N):
#     #     # https://zhuanlan.zhihu.com/p/90272131
#     #         break
#     zi = np.random.multivariate_normal(mean = np.zeros(N), cov = zcov)
#     bd["zi"] = zi
#     def func(d):
#         return CAR(PD = d["pd"], z = norm.cdf(d["zi"]), asset = d["total_assets"]) * d["total_assets"]#TODO:文章里没这个cdf，不太对
#     bd["loss0"] = bd.apply(func, axis = 1)
#     return bd

# def _failure(bd, r):
#     bd[f"failed{r}"] = bd.apply(lambda d: d[f"loss{r}"] >= d["capital"], axis = 1)
#     return bd


# def _contagion(bd, loss_ratio):
#     #iban 银行间资产网络 inter bank assets network
#     iban = triple_max_entropy(bd)
#     rd = 0
#     while True:
#         if rd == 0:
#             fail = np.array(bd["failed0"])
#         else:
#             fail = np.array(bd[f"failed{rd}"]) ^ np.array(bd[f"failed{rd - 1}"])#不存在 True False的情况, ^ 即xor
#         if not fail.any():
#             break
#         ctg_loss = iban[fail].sum(axis = 0) * loss_ratio#TODO:这里axis应该是啥？
#         rd += 1
#         bd[f"loss{rd}"] = ctg_loss + np.array(bd[f"loss{rd - 1}"])
#         bd = _failure(bd, rd)
#     return bd, rd

# def SYMBOL(bank_data, 
#            loss_corr = 0.5,
#            loss_ratio = 0.7,
#            mcrd = 999,
#            save = None):
#     """
#     计算银行系统损失分布
#     ------------------
#     bank_data: DataFrame
#         include columns:["name",#银行名称
#                          "total_assets",#总资产，CAR的参数
#                          "risk_weighted_assets",#风险加权资产，用来计算MCR，然后算PD
#                          "capital",#自有资本，损失大于自有资本则破产,
#                          "inter_bank_assets",(ia1 ia2 ia3)
#                          "inter_bank_liability"(ib1 ib2 ib3)]
            
#     # MCR:minimum capital requires
#     pd_kwds
#     """
#     # 第一步：bankdata里需要有pd
#     loss_list = []
#     for i in tqdm(range(mcrd)):
#         bd = bank_data.copy()
#         # 第二步：计算每家银行i的损失
#         bd = _loss(bd, loss_corr)
    
#         # 第三步: 判断违约
#         bd = _failure(bd, 0)
        
#         # 第四步: 传染损失
#         bd, maxcontrd = _contagion(bd, loss_ratio)
#         # bd.to_csv("bd.csv")
#         if not(save is None):
#             path = RESULT + "/leaveone/symbol/"
#             bd.to_csv(path + save + str(i) + ".csv")
#         L = np.array(bd[f"loss{maxcontrd}"]).sum()
        
#         loss_list.append(L)
#     # print(loss_list)
#     return np.array(loss_list)

# def leave_one_out(bank_data,
#                   h,
#                   L,
#                   p,
#                   mcrd = 999):
#     """
#     去一法
#     As in Puzanova and Düllman (2013), we define the system risk as 
#     the Expected Shortfall (ES) of the banking system liabilities 
#     computed at a probability level p, (where the probability of a 
#     systemic event is (1 − p)). The ES represent the expected loss 
#     for a given portfolio in the worst (1 − p) share of cases.[3]
#     系统性风险用ES衡量
#     """
#     bd_leave = bank_data.copy().drop(h)
#     mc_leave = SYMBOL(bank_data = bd_leave, mcrd = mcrd)
#     #系统期望损失
#     hpd = bank_data.loc[h].copy()

#     #去掉h的系统期望损失
#     hpd["L_dh"] = _system_ES(mc_leave, p)
    
#     #h单独的期望损失
#     hpd["l_h"] = _single_ES(float(hpd["pd"]), float(hpd["total_assets"]), p)
#     hpd["L"] = L
    
#     hpd["sys_h"] =  hpd["L"] - hpd["L_dh"] - hpd["l_h"] 
#     return pd.DataFrame(hpd)

# def LOO(bank_data,
#         p,
#         mcrd,
#         path_file,
#         skip_exist = True,
#         ):
#     """
#     如果skip_exist bank_data将由保存的bank_data.csv决定
#     p必须保持一致
#     mcrd也应当保持一致，不强制
#     """
#     save_path = RESULT+f"/LOO/{path_file}"
#     saved = os.listdir(save_path)
#     if skip_exist and ("loo_info.npy" in saved):
#         _p, _mcrd = np.load(f"{save_path}/loo_info.npy")
#         if _p != p:
#             raise Exception(f"p {p} != {_p} saved in {save_path}")
#         if _mcrd != mcrd:
#             print("warning: {mrcd} != {_mrcd}")
#     else:
#         np.save(f"{save_path}/loo_info.npy", np.array([p, mcrd]))
        
#     if skip_exist and ("bank_data.csv" in saved):
#         bank_data = pd.read_csv(f"{save_path}/bank_data.csv", index_col="Bankcd")
#         print(bank_data)
#     else:
#         bank_data = bank_data.copy()
#         print("estimating pd...")
#         bank_data = estimate_pd(bank_data)
#         bank_data.to_csv(f"{save_path}/bank_data.csv")
#         print("finish.")
        
#     if skip_exist and ("L.npy" in saved):
#         L = float(np.load(f"{save_path}/L.npy"))
#     else:
#         print("simulating total loss...")
#         mc_all = SYMBOL(bank_data = bank_data, mcrd = mcrd)
#         # num_bank = len(bank_data.index)
#         L = _system_ES(mc_all, p)
#         np.save(f"{save_path}/L.npy", L)
#         print("finish.")
    
#     for i,h in enumerate(bank_data.index):
#         save_name  = f"{h}.csv"
#         if skip_exist and (save_name in saved):
#             continue
#         else:
#             print(f"LOO ::: {h}")
#             r = leave_one_out(bank_data, h, L, p, mcrd) 
#             r.to_csv(f"{save_path}/{save_name}")
#     return
    
# def _system_ES(mcresult, p):
#     """
#     ES = \sum(P(x) * x) / \sum(P(x))
#     P是给定置信度下，收益低于x的概率
#     """
#     q = np.quantile(mcresult, p)
#     tail = mcresult[mcresult > q]
#     return tail.mean()
    
# def _single_ES(pd, total_assets, p):
#     """
#     单独银行的损失

#     Parameters
#     ----------
#     pd : 违约距离.
#     total_assets : 总资产
#     p : 置信度
#     es = integrate_p^1 (f(z) * loss(z)) dz / 1-p
#     """
#     def func(z):
#         return norm.pdf(z) * CAR(PD = pd, z = z,\
#                                  asset = total_assets) * total_assets
#     r,_  = quad(func, p, 1)
#     return r / (1 - p)
    
    
# if __name__ == "__main__":
#     if 0:
#         # _ = _system_ES(np.array([1,2,3,4,8]), p = 0.7) 
#         _ = _single_ES(0.01, 999, 0.9)
#         print(_)
        
        
#         data = pd.read_csv("refine.csv",encoding="gbk")
#         data = data[["公司名称", "资产总计","RWA/Total Assets", "所有者权益/总资产","同业资产","同业负债"]]
        
#         data["risk_weighted_assets"] = data.apply(lambda x: (x["RWA/Total Assets"] * x["资产总计"])/100, axis = 1)
#         data["capital"] = data.apply(lambda x:(x["所有者权益/总资产"] * x["资产总计"])/100, axis = 1)
        
#         data = data.rename(columns = {"资产总计": "total_assets", "同业资产": "inter_bank_assets", "同业负债": "inter_bank_liability","公司名称":"name"})
#         data = data[["name","total_assets", "risk_weighted_assets","capital", "inter_bank_assets","inter_bank_liability"]]
#         data = data.set_index("name")
#         data = data.apply(lambda x: x/1e8)
#         # print(data)
#         SYMBOL(data)

    