# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:57:14 2023

@author: qiyu

Reference
---------
[1] 银行间困境传染及系统重要性与脆弱性识别 ———基于 DebtRank 算法  郑红, 包芮, 黄玮强

"""
import numpy as np
import copy
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd
from qytoolspkg.basictools.arraytools import sickle

def _equity(Ae, Le, A):
    return Ae - Le + A.sum(axis = 1) - A.sum(axis = 0)

def _At(A0, ht_1):
    At = A0.copy() * 0
    for j,h in enumerate(ht_1):
        At[:, j] = A0[:, j] * (1 - h)
    return At

# def _Lambda(A, E):
#     Lambda = A.copy() * 0
#     for i, e in enumerate(E):
#         Lambda[i,:] = A[i,:] / e
#     return Lambda
        
def _min_ht_1(ht):
    ht_n = ht.copy()
    for i,h in enumerate(ht):
        if h>1:
            ht_n[i] = 1 
    return ht_n

def contagion(A:np.ndarray,
              Ae:np.array,
              Le:np.array,
              shock: np.array,
              ):
    """
    Parameters
    ----------
    A: 银行间借贷关系矩阵, 元素 Aij 表示银行 i 借给银行 j 的资金数额
    Ae: 外部资产
    Le: 外部负债
    shock: 冲击，单位与资产负债同
    
    
    Return
    ------
    Loss: 每家银行的最终损失
    """
    # N = len(Ae)
    # E0 = _equity(Ae, Le, A)
    # #初始冲击
    # h = np.zeros((1, N))
    # Ae1 = Ae - shock
    
    # E1 = _equity(Ae1, Le, A)
    # h = np.vstack([h, (E0 - E1)/E0])
    # A1 = _At(A, h[0])
    # while True:
        
    #     Lambda = _Lambda(A1, E1)
        
    #     h_tp1_ = h[-1] + (Lambda @ (h[-1] - h[-2]).reshape(-1, 1)).T[0]
    #     h_tp1 = min([1, h_tp1_])
    #     h = np.vstack([h, h_tp1])
        
    #     A1 = _At(A, h[0])
    #     E1 = E0 - h[-1] * E0
        
        
        
    N = len(Ae)
    E0 = _equity(Ae, Le, A)
    A0 = A
    #初始冲击
    h = np.zeros((1,N))
    Ae1 = Ae - shock
    
    h_left = (Ae - Ae1) / E0
    # print(h_left)
    while True:
        ht = h[-1,:]
        # print(ht)
        At = _At(A0, ht)
        ht = h_left + (A0 - At).sum(axis = 1) / E0
        ht = _min_ht_1(ht)
        h = np.vstack([h, ht])
        if np.linalg.norm(h[-1] - h[-2]) < 1e-3:
            break
    return h[-1] * E0
    # print(h)
    # return h


class DebtRankContagion:
    def __init__(self, banks, net):
        """
        net银行间资产网络 net[i,j] i把钱借给j i的资产
        """
        self.banks = banks.copy()
        self.bankid = list(banks.index)
        self.num_banks = len(banks)
        self.A = np.array(net.loc[self.bankid][self.bankid])
        self.A0 = self.A
        self.Ae = np.array(banks.loc[self.bankid]["total_assets"])\
            - self.A.sum(1)
        self.Le = np.array(banks.loc[self.bankid]["total_assets"])\
            - self.A.sum(0) - np.array(banks["capital"])

        self.E0 =  np.array(banks.loc[self.bankid]["capital"])
        self.E0_ = self.E0
        self.t = 0
        self.st = 0
        self.banks["E0"] = self.E0_
        self.stepid_old = None
        self.stepid = None
        # self.phi = np.zeros(self.num_banks)
    def E(self):
        # return self.Ae[i] - self.Le[i] + \
        #     self.A[i][self.varA].sum() - self.A[:, i]
        return sickle(self.Ae - self.Le + \
                      self.A.sum(axis = 1) - self.A0.sum(axis = 0))
                      # 只折资产，不折负债
    @property
    def varA(self):
        return self.E0 > 0
    
    def finish(self, threshold = 1e2):
        if self.stepid_old is None:
            return False
        else:
            _ = -1 * ((np.array(self.banks[self.stepid + "-E0"]) - \
                       np.array(self.banks[self.stepid_old + "-E0"])).sum()) < threshold
            return _
    
    def shock(self, s, ratio = True):
        """
        s:dict
            s[bank] = shock value
        if ratio is True
            s[bank] = s * E0
        """
        self.st += 1
        self.t = 0
        self.stepid_old = None
        shockid = f"drshock{self.st}"
        self.banks[shockid] = np.zeros(self.num_banks)
        for bank in s:
            assert(bank in self.bankid)
            if ratio:
                ss = s[bank] * self.banks.loc[bank, "E0"]
            else:
                ss = s[bank]
            self.banks.at[bank, shockid] = ss
        s = np.array(self.banks.loc[self.bankid][shockid])
        # self.phi += -1 * s
        self.Ae = self.Ae - s
        return
        
    def update_A(self, A, E1):
        w = np.zeros((self.num_banks, self.num_banks))
        for j in range(self.num_banks):
            if self.varA[j]:
                w[:, j] = E1[j]/self.E0[j]
            else:
                w[:, j] = 0
        u = A * w       
        # self.phi += A.sum(axis = 1) - u.sum(axis = 1)
        return u
    
    def update_label(self):
        self.t += 1
        self.stepid_old = self.stepid
        self.stepid = f"drstep{self.st}-{self.t}"

    def step(self):
        self.update_label()
        E1 = self.E()
        self.A = self.update_A(self.A, E1)
        self.E0 = E1.copy()
        _ = pd.DataFrame(self.E(), columns=[self.stepid + "-E0"])
        _ = _.set_index(self.banks.index)
        self.banks = pd.concat([self.banks, _], axis = 1)
        # self.banks[self.stepid + "-E0"] = self.E()  
        # self.phi = np.zeros(self.num_banks)
        return 
    
    def run(self, shock):
        self.shock(shock)
        while True:
            self.step()
            if self.finish():
                break
        return
    
    
class DebtRank2ChannelContagion(DebtRankContagion):
    def __init__(self, banks, net, abnet, price, total_share, alpha = 1.0536):
        """
        net银行间资产网络 net[i,j] i把钱借给j i的资产
        abnet [num_banks, num_assets]#份额，非价值
        price dic[num_assets]
        total_share = dic[num_assets]
        alpha 越大价格变化越快
        """
        self.banks = banks.copy()
        self.bankid = list(banks.index)
        self.assetid = abnet.columns
        self.price = np.array([[price[a]] for a in self.assetid])
        self.num_banks = len(banks)
        self.total_share = np.array([total_share[a] \
                                     for a in self.assetid])
        self.A = np.array(net.loc[self.bankid][self.bankid])
        self.A0 = self.A
        self.abnet = np.array(abnet.loc[self.bankid][self.assetid])#
        
        self.Ae = np.array(banks.loc[self.bankid]["total_assets"])\
            - self.A.sum(1) - (self.abnet @ self.price).sum(axis = 1)
        self.Le = np.array(banks.loc[self.bankid]["total_assets"])\
            - self.A.sum(0) - np.array(banks["capital"])

        self.E0 =  np.array(banks.loc[self.bankid]["capital"])
        self.E0_ = self.E0
        self.t = 0
        self.st = 0
        self.banks["E0"] = self.E0_
        # self.phi = np.zeros(self.num_banks)
        self.TA0 = self.TA()
        self.lev = self.TA0/self.E0
        self.price_history = []
        self.price_history.append(self.price)
        self.stepid_old = None
        self.stepid = None
        self.alpha = alpha
        return
    
    def step(self):
        self.update_label()        
        self.sell()
        # self.phi = np.zeros(self.num_banks)
        E1 = self.E()
        self.A = self.update_A(self.A, E1)
        self.E0 = E1.copy()
        # self.banks[self.stepid+"-E0"] = self.E()
        _ = pd.DataFrame(self.E(), columns=[self.stepid + "-E0"])
        _ = _.set_index(self.banks.index)
        self.banks = pd.concat([self.banks, _], axis = 1)
        return 
    
    def E(self):
        return sickle(self.Ae - self.Le + \
                      self.A.sum(axis = 1) - self.A0.sum(axis = 0)\
                          + (self.abnet @ self.price).sum(axis = 1))

    
    def TA(self):
        _ = self.Ae + self.A.sum(axis = 1) + \
            + (self.abnet @ self.price).sum(axis = 1)
        return _
    
    def sell(self):
        """
        return 
        [num_bank, num_assets]
        """
        #本轮银行承受的损失
        # sell_value = self.phi * (self.TA0 / self.E0)
        # sell_value = -1 * self.phi * self.lev
        sell_value = sickle(self.TA()-self.lev * self.E())
        # 如何卖出资产？按自己的持有份额平均？
        # 按资金平均？
        # 随机卖
        sellabnet = np.zeros(self.abnet.shape)
        for i,b in enumerate(self.bankid):
            val = 0
            ab = self.abnet[i]
            while True:
                idx = np.random.choice(range(len(ab)))
                val += self.price[idx]
                if (val > sell_value[i]) or \
                    ((sellabnet[i] >= self.abnet).all()):
                     break
                if sellabnet[i, idx] < self.abnet[i, idx]:
                    sellabnet[i, idx] += 1
                else:
                    break
                
        # print("sellabnet", sellabnet)
        self.abnet = self.abnet - sellabnet
        self.Le = self.Le - (sellabnet @ self.price).reshape(-1)
        # update price        
        x = (sellabnet.sum(axis = 0)/\
             self.total_share).reshape(self.price.shape)
        # print(x)
        # print(self.stepid + " dp : ",self.price * (1 - np.exp(-1 * alpha * x)))
        self.price = self.price * np.exp(-1 * self.alpha * x)
        self.price_history.append(self.price)
        return 
    
    def plot_price(self):    
        ph = np.array(self.price_history).squeeze(-1)
        for i,_ in enumerate(ph.T):
            plt.plot(ph[:, i], label = f"ta:{self.total_share[i]}")
        plt.legend()
        plt.show()
        return 

def DR(drc, i, level):
    shock = {i:level}        
    drc.run(shock)
    banks = drc.banks
    el = drc.stepid + "-E0"
    loss = (banks[el] - banks["E0"]).copy()
    loss.loc[i] = 0
    E0 = banks["E0"].copy()
    E0.loc[i] = 0
    return loss.sum()/E0.sum()

def VUL(drc, i, level):
    LOSS = []
    E0 = drc.banks.loc[i, "E0"]
    for j in tqdm(drc.bankid):
        if j == i:
            continue
        drc_j = copy.deepcopy(drc)
        shock = {j:level}        
        drc_j.run(shock)
        banks = drc_j.banks
        el = drc_j.stepid + "-E0"
        loss_j2i = banks.loc[i, el] - E0
        LOSS.append(loss_j2i / E0)
    return np.array(LOSS).mean()


if __name__ == "__main__":
    from MaxEntropy import SRAS
    from qyshare import path
    import pandas as pd
    # year = 2015
    df = pd.read_csv(path.PROCESS+f"/bankcontagion/bank_data_2022_all.csv", index_col=["Bankcd"])
    ia1 = np.array(df["ia1"])
    ib1 = np.array(df["ib1"])
    A,_ = SRAS(ia1, ib1)
    A = pd.DataFrame(A, index = df.index, columns=df.index)
    # contagion(A, Ae, Le, shock)
    # TA = np.array(df["total_assets"]).reshape(1,-1)[0]
    # Ae = TA - ia1
    # E = np.array(df["capital"]).reshape(1, -1)[0]
    # Le = Ae - E - ib1
    
    # def __init__(self, banks, net, abnet, price, total_share):
    #     """
    #     net银行间资产网络 net[i,j] i把钱借给j i的资产
    #     abnet  dataframe[num_banks, num_assets]#份额，非价值
    #     price dic[num_assets]
    #     total_share = dic[num_assets]
    #     """
    
    # num_assets = 5
    # total_share = {a:np.random.uniform(1e5,1e6) for a in range(num_assets)}
    # price = {a:np.random.uniform(1,10) for a in range(num_assets)}
    
    
    # abnet = df.copy()
    # for a in range(num_assets):
    #     abnet[a] = abnet["total_assets"].apply(lambda x: int(x * np.random.uniform(0.7,1.3) * 0.01))
    
    # abnet = abnet[list(range(num_assets))]
    
    
    shock = {101:1e4}
    # r = contagion(A, Ae, Le, shock)
    drc = DebtRankContagion(df, A)
    drc.shock(shock)
    drc.step()    
    # drcc = DebtRank2ChannelContagion(df, A, abnet, price, total_share)
    # drcc = DebtRankContagion(df, A)
    
    # VUL(drcc, 4, 0.05)
    
    # drc = drcc
    # i = 101
    # level = 0.05
    # LOSS = []
    # E0 = drc.banks.loc[i, "E0"]
    # for j in tqdm(drc.bankid):
    #     if j == i:
    #         continue
    #     drc_j = copy.deepcopy(drc)
    #     shock = {j:level}        
    #     drc_j.run(shock)
    #     banks = drc_j.banks
    #     el = drc_j.stepid + "-E0"
    #     loss_j2i = banks.loc[i, el] - E0
    #     LOSS.append(loss_j2i / E0)
    
        
        