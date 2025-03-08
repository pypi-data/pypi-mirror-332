# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:10:42 2023

@author: win10
"""

import pandas as pd
import numpy as np
from scipy.optimize import fsolve
from scipy.stats import norm  # 正态分布累计概率函数
from scipy import stats
from qyshare.core.stocks.ratios import read_item
from qyshare.core.basictools.basicfunc import aroundzero
import warnings




def _va_sigma_a(V_e, Sigma_e, D, rf, rft=1, x0 = None):
    """
    BS公式
    https://zhuanlan.zhihu.com/p/38294971
    C = S * N(d1)-K exp(-r * t)N(d2)
    C是期权价格，S是当前标的资产价格，K是行权价，r是无风险资产，t是期权的到期期限
    对应这里 ：
    Ve 是 C： 将股价视为期权价。
    Va 是 S： 将公司资产视为标的资产。
    K 是 D 即债务。
    rft 是 t，由于债务到期时间并不是统一的，这里不要求精确，一般就设为 1 年。
    ----------------------------------------------------------
    计算资产市值以及资产波动率
    :param V_e: 股权市值
    :param Sigma_e: 股权波动率
    :param D: 债务面值
    :param rf: 无风险利率
    :param rft: 无风险利率对应期限（期权期限）
    :return: 资产市值V_a和资产波动率sigma_a
    
    如果D特别大，方程不会收敛！const = 2*V_e时结果会返回初始猜测，也能够得到一个大负DD。
    """
    const = 2 * V_e
    V_e = V_e/const
    D  = D/const
    # print("D:",D)
  
    if x0 is None:
        x0 = np.array([V_e, Sigma_e])
    err = 999
    def _f(x):
        """
        方程组，用于根据股权市值，股权波动率，债务面值，无风险利率，求解每只股票的资产市值V_a和资产波动率Sigma_a
        :param x: 列表，两个未知数，分别是资产市值以及资产波动率
        :return: 方程
        """
        x0,x1 = x
        d1 = (np.log(abs(x0)) - np.log(abs(D)) + (rf + 0.5 * (x1 ** 2)) * rft) / (x1 * np.sqrt(rft))
        d2 = d1 - x1 * np.sqrt(rft)
        return [
            x0 * norm.cdf(d1) - D * np.exp(-rf * rft) * norm.cdf(d2) - V_e,
            x0 * x1 * (norm.cdf(d1) / V_e) - Sigma_e
        ]

    # 设定方程求解初始值

        # print("x0:",x0)
    
    # 求解方程组
    # bsm方程组是一个非线性方程组，fslove求得的是局部最优解，所以不一定能得到全局最优解
    # 迭代初始值x0对结果的影响可能很大, 不合适的初值可能导致结果不收敛或偏差太大，因而爆出警告
    # 忽略warnings
    warnings.filterwarnings('ignore') 
    # while err > 0.1:
    result = fsolve(_f, x0)#, xtol = 1e-8)
    err = np.linalg.norm(_f(result))
    # print("x0:", x0)
    # print("result:", result)
    # print("err:",err)
    # x0[0]  = x0[0] + np.random.randn()
    V_a, Sigma_a = result
    return [V_a * const, Sigma_a]


def solve_func(volatility:pd.DataFrame, 
                market_value:pd.DataFrame, 
                rf:pd.DataFrame, 
                debt:pd.DataFrame,
                dp:pd.DataFrame,
                rft:float = 1,
                previous_x0 = False):
    """
    违约距离dd: 
    volatility: 日度波动率时间序列。
    marketvalue: 日度市值序列(元)。
    rf: 日度年化无风险收益序列。
    rft: 债务到期时间(年)，默认为1年
    
    debt: 债务。本身为报表数据，ffill变为日度
    dp：违约点。同上
    
    previous_x0: 使用前值作为初始猜测
    """
    
    volatility.columns =["se"]
    market_value.columns = ["ve"]
    rf.columns = ["rf"]
    dp.columns = ["dp"]
    debt.columns = ["debt"]
    
    volatility = volatility * np.sqrt(252 * rft)
    df = pd.concat([volatility, market_value, rf],axis = 1, join="inner",)
    
    ddp = pd.merge(debt, dp, on="time", how = "inner")
    
    # ag_date = (ddp.index[-1] + pd.Timedelta("1d")).to_period("Q").end_time
    # ag = pd.DataFrame({"debt":[np.nan],"dp":[np.nan]},index = [ag_date])
    # ddp = pd.concat([ddp, ag], axis = 0)
    # ddp.index = [i.to_period("Q") for i in ddp.index]
    # ddp = ddp.resample("D",convention = "end").ffill()
    ddp["zero"] = ddp.apply(lambda x: np.nan if (aroundzero(x["debt"]) or aroundzero(x["dp"]))
                            else False, axis = 1)
    # print(df,ddp)    
    df = pd.merge(df, ddp, how = "inner", on = "time")    
    df = df.dropna()
    if previous_x0:
        _ri = None
        _r = np.zeros((len(df),2))
        for i,t in enumerate(df.index):
            x = df.loc[t]
            _ri = _va_sigma_a(x["ve"], x["se"], x["debt"], x["rf"], rft, _ri)
            # print(_ri)
            _r[i] = _ri
        df[["va","sa"]] = _r
            
    else:   
        df[["va","sa"]] = df.apply(lambda x : _va_sigma_a(x["ve"], x["se"], x["debt"], x["rf"], rft),
                                   axis = 1, result_type = "expand")
    return df
    
def default_distance(volatility:pd.DataFrame, 
                     market_value:pd.DataFrame, 
                     rf:pd.DataFrame, 
                     debt:pd.DataFrame,
                     dp:pd.DataFrame,
                     rft:float = 1,
                     previous_x0 = False,
                     result_cols = "dd"):
    df = solve_func(volatility, market_value, rf, debt, dp,rft, previous_x0)
    df["dd"] =  df.apply(lambda x: (x["va"] - x["dp"])/(x["va"] * x["sa"]), axis = 1)
    if result_cols =="all":
        return df
    else:
        return df[[result_cols]]

# def kmv_solve(code):
    
def _equity_sensitivity_to_asset(A, D, r, sigma_A, T):
    """
    计算公司资产价值下跌1%时，股权价值下跌的百分比。
    
    参数：
    A       : float, 企业资产价值
    D       : float, 企业负债价值
    r       : float, 无风险利率（年化）
    sigma_A : float, 企业资产波动率（年化）
    T       : float, 债务到期时间（以年为单位）
    
    返回：
    ratio   : float, 股权价值下降百分比与资产价值下降1%的比例关系
    """
    # 计算 d1 和 d2
    
    d1 = (np.log(A / D) + (r + 0.5 * sigma_A**2) * T) / (sigma_A * np.sqrt(T))
    d2 = d1 - sigma_A * np.sqrt(T)
    
    # 计算 N(d1) 和 N(d2)
    N_d1 = norm.cdf(d1)
    N_d2 = norm.cdf(d2)
    
    # 计算股权价值 E
    equity_value = A * N_d1 - D * np.exp(-r * T) * N_d2
    
    # 计算股权价值对资产价值的敏感性（Delta，即 ∂E/∂A）
    delta = N_d1
    
    # 假设资产下降1%
    asset_decline = 0.01  # 1%
    new_A = A * (1 - asset_decline)
    
    # 重新计算 d1 和 d2
    new_d1 = (np.log(new_A / D) + (r + 0.5 * sigma_A**2) * T) / (sigma_A * np.sqrt(T))
    new_d2 = new_d1 - sigma_A * np.sqrt(T)
    new_N_d1 = norm.cdf(new_d1)
    new_N_d2 = norm.cdf(new_d2)
    
    # 重新计算股权价值
    new_equity_value = new_A * new_N_d1 - D * np.exp(-r * T) * new_N_d2
    
    # 计算股权价值的变化百分比
    equity_decline = (equity_value - new_equity_value) / equity_value * 100  # 百分比下降
    
    # 返回比例关系
    return equity_decline / asset_decline


def equity_sensitivity_to_asset(V_e, Sigma_e, D, rf, rft=1, x0 = None):
    
    A , sigma_A = _va_sigma_a(V_e, Sigma_e, D, rf, rft, x0)
    return _equity_sensitivity_to_asset(A, D, rf, sigma_A, rft)
    
    


if __name__ == "__main__":
    from wcode.stocks.reader import stock
    from macroeco.macroeco import cbonds
    s = stock("600606")
    
    rf = cbonds().get() / 100   
    rf = rf.resample("Y").mean()
    mv = pd.merge(s.amount(),s.turnover(), on = "time", how = "inner")
    mv["mv"] = mv.apply(lambda x : x['amt'] / x['tov'], axis = 1)
    mv = mv[["mv"]].resample("Y").last()
    
    rt = s.logreturn() / 100
    volatility = rt.rolling(window=252).std()   
    volatility = volatility.resample("Y").last()
    debt= s.debt("Y")
    dp = s.default_point(0.5, "Y")
    
    # df = default_distance(volatility, mv, rf, debt, dp, previous_x0=False)
    df = solve_func(volatility, mv, rf, debt, dp, previous_x0=False)
    
    
    