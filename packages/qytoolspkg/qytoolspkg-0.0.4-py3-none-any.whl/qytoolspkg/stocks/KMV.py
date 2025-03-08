# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:44:59 2025

@author: qiyu
"""

import numpy as np
import pandas as pd
from scipy.optimize import fsolve
from scipy.stats import norm
import warnings


def _calculate_d1_d2(A, D, r, sigma_A, T):
    """
    根据资产价值、债务价值等参数计算d1和d2。

    参数：
        A (float): 企业资产价值。
        D (float): 企业负债价值。
        r (float): 无风险利率（年化）。
        sigma_A (float): 企业资产波动率(年化sigma_A = sigma_A * np.sqrt(252 * T))。
        T (float): 债务到期时间（单位：年）。

    返回：
        tuple: 包含d1和d2的元组。
    """
    d1 = (np.log(A / D) + (r + 0.5 * (sigma_A ** 2)) * T) / (sigma_A * np.sqrt(T))
    d2 = d1 - sigma_A * np.sqrt(T)
    return d1, d2


def bs_rel(A = None, sigma_A = None, D = None, r = None,  T = None, d1 = None, d2 = None):
    """
    A, sigma_A -> E,sigma_E

    根据企业资产价值和波动率计算股权市值和股权波动率。
    参数：
        A (float): 企业资产价值。
        sigma_A (float): 企业资产波动率(年化sigma_A = sigma_A * np.sqrt(252 * T))。
        D (float): 企业负债价值。
        r (float): 无风险利率。
        T (float): 债务到期时间（单位：年）。
        d1 (float): Black-Scholes模型中的d1。
        d2 (float): Black-Scholes模型中的d2。
    
    返回：
        list: 包含股权市值 (E) 和股权波动率 (sigma_E) 的列表。
    """
    if (d1 is None) or (d2 is None):
        d1, d2 = _calculate_d1_d2(A, D, r, sigma_A, T)
    E = A *  norm.cdf(d1) - D * np.exp(-r * T) * norm.cdf(d2)
    sigma_E =  A * sigma_A * norm.cdf(d1) / E 
    return [E, sigma_E]
    

def _solve_bs_rel(E, sigma_E, D, r, T, x0):
    """
    使用Black-Scholes模型通过非线性方程组求解资产市值和资产波动率。

    参数：
        E (float): 股权市值。
        sigma_E (float): 股权波动率。
        D (float): 债务面值。
        r (float): 无风险利率。
        T (float): 债务到期时间（单位：年）。
        x0 (list or None): 初始猜测值，默认为None。

    返回：
        list: 包含资产市值 (V_a) 和资产波动率 (Sigma_a) 的列表。
    """
    const = 2 * E

    E = E/const
    D = D/const
    err = 999
    rd = 0
    if x0 is None:
        x0 = np.array([E, sigma_E])
    def _f(x):
        """
        方程组，用于根据股权市值，股权波动率，债务面值，无风险利率，求解每只股票的资产市值V_a和资产波动率Sigma_a
        :param x: 列表，两个未知数，分别是资产市值以及资产波动率
        :return: 方程
        """
        x0,x1 = x
        d1 = (np.log(abs(x0)) - np.log(D) + (r + 0.5 * (x1 ** 2)) * T) / (x1 * np.sqrt(T))
        d2 = d1 - x1 * np.sqrt(T)
        return [
            x0 * norm.cdf(d1) - D * np.exp(-r * T) * norm.cdf(d2) - E,
            x0 * x1 * norm.cdf(d1) / E - sigma_E
        ]

    # 设定方程求解初始值    
    # 求解方程组
    # bsm方程组是一个非线性方程组，fslove求得的是局部最优解，所以不一定能得到全局最优解
    # 迭代初始值x0对结果的影响可能很大, 不合适的初值可能导致结果不收敛或偏差太大，因而爆出警告
    # 忽略warnings
    # warnings.filterwarnings('ignore') 
    while (err > 1e-4):
        result = fsolve(_f, x0, xtol = 1e-4)
        err = np.linalg.norm(_f(result))
        x0 = x0 + np.random.randn(2)
        rd += 1
        if rd == 999:
            return [np.nan, np.nan]
    # print("x0:", x0)
    # print("result:", result)
    # print("err:",err)
    # x0[0]  = x0[0] + np.random.randn()
    A, sigma_A = result
    return [A * const, sigma_A]



def inv_bs_rel(E, sigma_E, D, r, T, x0=None):
    """
    E, sigma_E -> A, sigma_A
    
    根据股权市值和波动率计算企业资产市值和波动率。

    参数：
        E (float): 股权市值。
        sigma_E (float): 股权波动率(年化sigma_A = sigma_A * np.sqrt(252 * T))）。
        D (float): 债务面值。
        r (float): 无风险利率。
        T (float): 债务到期时间（单位：年），默认为1年。
        x0 (list or None): 初始猜测值，默认为None。

    返回：
        list: 包含资产市值 (V_a) 和资产波动率 (Sigma_a) 的列表。
    """
    # 将volatility标准化到年化波动率
    
    const = 2 * E
    E, D = E / const, D / const
    if x0 is None:
        x0 = [E, sigma_E]
    A, sigma_A = _solve_bs_rel(E, sigma_E, D, r, T, x0)
    return [A * const, sigma_A]


def _solve_func(A_df, sigma_A_df, r_df, D_df, DP_df, T=1, previous_x0=False):
    """
    计算资产市值和波动率，并返回包含这些数据的DataFrame。

    参数：
        A_df (pd.DataFrame): 日度市值序列。
        sigma_A_df (pd.DataFrame): 波动率时间序列(年化sigma_A = sigma_A * np.sqrt(252 * T))。
        r_df (pd.DataFrame): 无风险利率序列。
        D_df (pd.DataFrame): 债务序列。
        DP_df (pd.DataFrame): 违约点序列。
        T (float): 债务到期时间（单位：年），默认为1年。
        previous_x0 (bool): 是否使用前值作为初始猜测，默认False。

    返回：
        pd.DataFrame: 包含资产市值 (va) 和波动率 (sa) 的DataFrame。
    """
    # 标准化列名
    sigma_A_df.columns, A_df.columns, r_df.columns = ["se"], ["ve"], ["r"]
    DP_df.columns, D_df.columns = ["dp"], ["debt"]

    # 合并数据
    df = pd.concat([sigma_A_df, A_df, r_df], axis=1, join="inner")
    ddp = pd.merge(D_df, DP_df, on="time", how="inner")
    df = pd.merge(df, ddp, how="inner", on="time").dropna()

    # 计算资产市值和波动率
    if previous_x0:
        _ri = None
        results = []
        for _, row in df.iterrows():
            _ri = inv_bs_rel(row["ve"], row["se"], row["debt"], row["r"], T, _ri)
            results.append(_ri)
        df[["va", "sa"]] = results
    else:
        df[["va", "sa"]] = df.apply(
            lambda row: inv_bs_rel(row["ve"], row["se"], row["debt"], row["r"], T),
            axis=1,
            result_type="expand"
        )

    return df


def default_distance(A_df, sigma_A_df, r_df, D_df, DP_df, T = 1, previous_x0=False, result_cols="dd"):
    """
    计算违约距离 (DD)。

    参数：
        A_df (pd.DataFrame): 日度市值序列。
        sigma_A_df (pd.DataFrame): 波动率时间序列(年化sigma_A = sigma_A * np.sqrt(252 * T))。
        r_df (pd.DataFrame): 无风险利率序列。
        D_df (pd.DataFrame): 债务序列。
        DP_df (pd.DataFrame): 违约点序列。
        T (float): 债务到期时间（单位：年），默认为1年。
        previous_x0 (bool): 是否使用前值作为初始猜测，默认False。
        result_cols (str): 返回的列，默认为"dd"，"all"返回全部计算结果。

    返回：
        pd.DataFrame: 包含违约距离或全部结果的DataFrame。
    """
    df = _solve_func(A_df, sigma_A_df, r_df, D_df, DP_df, T, previous_x0)
    df["dd"] = df.apply(lambda x: (x["va"] - x["dp"]) / (x["va"] * x["sa"]), axis=1)
    return df if result_cols == "all" else df[[result_cols]]


def sensitivity_a2e(A, sigma_A, D, r, T = 1, pct_change_A = 0.01, pct_change_sigma_A = 0.01):
    """
    计算公司资产价值变化对股权价值变化的敏感性。

    参数：
        A (float): 企业资产价值。
        D (float): 企业负债价值。
        r (float): 无风险利率（年化）。
        sigma_A (float): 企业资产波动率（(年化sigma_A = sigma_A * np.sqrt(252 * T))）。
        T (float): 债务到期时间（单位：年），默认为1年。
        pct_change_A (float): 资产价值变化的百分比，默认为0.01。
        pct_change_sigma_A (float): 资产波动率变化的百分比，默认为0.01。

    返回：
        list: 包含股权价值变化的百分比和股权波动率变化的百分比。
    """
    E, sigma_E = bs_rel(A,sigma_A,D,r,T)
    new_A = A * (1 + pct_change_A)
    new_sigma_A = sigma_A * (1 + pct_change_sigma_A)
    E_ , sigma_E_ = bs_rel(new_A, new_sigma_A, D, r, T)
    pct_change_E = (E_ - E) / E
    pct_change_sigma_E = (sigma_E_ - sigma_E) / sigma_E
    return [pct_change_E, pct_change_sigma_E]



def sensitivity_e2a(E, sigma_E, D, r, T = 1, pct_change_E = 0.01, pct_change_sigma_E = 0.01):
    
    """
    计算股权价值变化对资产价值变化的敏感性。

    参数：
        E (float): 股权市值。
        sigma_E (float): 股权波动率(年化sigma_A = sigma_A * np.sqrt(252 * T))。
        D (float): 债务面值。
        r (float): 无风险利率。
        T (float): 债务到期时间（单位：年），默认为1年。
        pct_change_E (float): 股权价值变化的百分比，默认为0.01。
        pct_change_sigma_E (float): 股权波动率变化的百分比，默认为0.01。

    返回：
        list: 包含资产价值变化的百分比和资产波动率变化的百分比。
    """
    A, sigma_A = inv_bs_rel(E, sigma_E, D, r, T)
    new_E = E * (1 + pct_change_E)
    new_sigma_E = sigma_E * (1 + pct_change_sigma_E)
    A_, sigma_A_ = inv_bs_rel(new_E, new_sigma_E, D, r, T)
    pct_change_A = (A_ - A) / A
    pct_change_sigma_A = (sigma_A_ - sigma_A) / sigma_A
    return [pct_change_A, pct_change_sigma_A]


if __name__ == "__main__":
    E  = 9592.181266337651
    sigma_E = 0.004645172250670376
    A = 320000.
    sigma_A = 0.048
    D = 312517.28
    r = 0.03
    T = 1
    
    sigma_E = sigma_E * np.sqrt(252 * T)
    # sigma_A = sigma_A * np.sqrt(252 * T)

    PE = np.arange(-0.2, 0, step = 0.01)
    ch = []
    for pe in PE:
        # s = sensitivity_e2a(E, sigma_E, D, r, pct_change_E=pe, pct_change_sigma_E=0.05)
        s = sensitivity_a2e(A, sigma_A, D, r, pct_change_A=pe, pct_change_sigma_A=0.01)
        ch.append(s[0])
    import matplotlib.pyplot as plt
    plt.plot(PE, ch)
    _calculate_d1_d2(A, D, r, sigma_A, T)


