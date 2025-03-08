# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:10:37 2025

@author: qiyu
"""

from qytoolspkg.stocks.reader import stock, shanghai
from qytoolspkg.systemic_risk.MES import MES, LRMES
import pandas as pd


def SRISK(company, 
          k = 0.08,
          market = shanghai.logreturn(),  
          alpha = 0.95):
    
    # k = 0.08
    # c = "000001"
    stk = stock(company)
    mes = MES(stk.logreturn(), 
              market=market, 
              alpha=alpha,
              to_plot=False,
              to_save=False)
    
    lrmes = LRMES(mes)
    lrmes = lrmes.resample("Y").last()
    D = stk.debt()
    mv = stk.market_value()
    srisk = pd.concat([D, lrmes, mv], axis= 1)
    srisk = srisk[["debt", "mv", "LRMES"]].dropna()
    def _func(x):
        _ = max(0, k * (x["debt"]) - (1 - k) * (x["mv"]) * (1 - x["LRMES"]))
        return _
    srisk["SRISK"] = srisk.apply(_func, axis = 1)
    return srisk[["SRISK"]]


