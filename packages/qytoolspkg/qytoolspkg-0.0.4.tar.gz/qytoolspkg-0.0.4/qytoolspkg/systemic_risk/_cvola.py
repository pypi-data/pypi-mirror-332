# -*- coding: utf-8 -*-
"""
Created on Sat May 27 22:47:16 2023

@author: win10
"""
# from statsmodels.tsa.stattools import ARMA #ADF单位根检验    
from arch import arch_model
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

def conditional_volatility(x, 
                           arma_order:[None, tuple] = None,#(1,0,1),
                           garch_order:dict = {"p":1,"o":0,"q":1},
                           ):
    """
    求条件方差
    if arma_order is None, no mean value model.
    """
    # print(x.std())
    if x.std() < 1e-1:
        ts = np.array([100 * float(xi) for xi in x])
    else:
        ts = np.array(x)
    # The scale of y is 0.000229. Parameterestimation work better when this value is between 1 and 1000. 
    # The recommended rescaling is 100 * y.
    
    if arma_order is None:
        res = ts
    else:
        arma_ = ARIMA(ts,arma_order).fit(disp=0)
        res = arma_.resid    
    am=arch_model(res,**garch_order) 
    g = am.fit(update_freq = 0,disp="off") 
    return g.conditional_volatility  

