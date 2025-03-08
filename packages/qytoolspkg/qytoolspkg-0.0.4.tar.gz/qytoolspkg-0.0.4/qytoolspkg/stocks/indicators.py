# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:45:41 2023

@author: lookingout


Reference
===========
[1] 高管媒体从业经历与股价大跌风险——基于上市公司的实证研究


"""

import numpy as np
import pandas as pd
from pandas import DataFrame
import statsmodels.api as sm
from qytoolspkg.basictools.dftools import to_series




def idio_logreturn(x: DataFrame,
                   market: DataFrame,
                   adv: int = 2,
                   lag: int = 2):
    """
    特质收益率
    """
    stamp = x.index.name
    df = pd.merge(x, market, on = stamp, how = "inner")
    df.columns = ["x","m"]
    
    mcol_names = ["m"]
    for s in range(-1*adv, lag+1):
        if s == 0: continue
        cn = f"m_{s}"
        mcol_names.append(cn)
        df[cn] = df["m"].shift(s)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna()
    df = sm.add_constant(df)
    mod = sm.OLS(df["x"], df[mcol_names])
    res = mod.fit().resid
    
    # lnr = lambda x : np.log(1 + x)
    # res = res.apply(lnr, axis = 0)
    ir = DataFrame({"idio_logreturn":res.values}, index=res.index)
    return ir
    
def duvol(x:DataFrame, freq = "M"):
    """
    负偏态收益率
    
    freq to resample 需要低于x的频率
    """
    x = to_series(x)
    rs = x.resample(freq)

    df = rs.agg({"up":lambda x:(x[x > x.mean()]**2).sum(),
                  "Nu":lambda x:(x > x.mean()).sum(),
                  "down":lambda x:(x[x < x.mean()]**2).sum(),
                  "Nd":lambda x:(x < x.mean()).sum()})
    df["del"] = df.apply(lambda d:np.nan if  (d["Nu"] <= 1)or\
                          (d["Nd"] <=1) else False, axis = 1) 
    df = df.dropna()    
    df["duvol"] = np.log((df["down"] * (df["Nu"]-1)) / (df["up"] * (df["Nd"] - 1)))
    return df["duvol"].to_frame()
    
def ncskew(x:DataFrame, freq = "M"):
    """
    收益率上下波动比率
    
    freq to resample 需要低于x的频率
    """
    x = to_series(x)
    rs = x.resample(freq)

    df = rs.agg({"3p":lambda x:(x**3).sum(),
                 "2p":lambda x:(x**2).sum(),
                 "N":lambda x: len(x.dropna())
                 })
    df["del"] = df.apply(lambda d:np.nan if \
                         (d["N"] <= 10) else False, axis = 1) 
    df = df.dropna()    
    df["ncskew"] = (-1* df["N"] * pow((df["N"] - 1), 3/2) * df["3p"]) / ((df["N"] - 1)\
        * (df["N"] - 2) * pow(df["2p"], 3/2))
    return df["ncskew"].to_frame()



if __name__ == "__main__":
    from reader import shanghai, stock
    x = stock("600606")
    a =  idio_logreturn(x.logreturn(), shanghai.logreturn())
    # a = a.resample("W").mean()
    # print(duvol(a, "Y"))
    # ncskew(a)