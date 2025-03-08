# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:43:29 2023

@author: lookingout
"""


from arch import arch_model
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from scipy.stats import norm
import pandas



def _garch_covar(source,
                target,
                q = 0.95,
                arma_order=(1,0,0),
                garch_order={"p":1,"o":0,"q":1},
                ):
    
    # 基于GARCH的CoVaR算法    
    
    _q = norm.ppf(q)
    
    # 求VaR
    N = len(source)

    #source的VaR
    arma = ARIMA(endog =source,order = arma_order, enforce_stationarity=False).fit()
    mu = arma.predict(start = 0,end = N-1)
    res = arma.resid
    am=arch_model(res, **garch_order)
    g = am.fit(update_freq=0,disp="off")
    cv = g.conditional_volatility
    cVaR = np.zeros(N)
    for i,mu_i in enumerate(mu):
        cVaR[i] = mu_i - _q * cv[i]

    #target的VaR，用来得到delta CoVaR
    arma = ARIMA(endog = target,order = arma_order).fit()
    mu = arma.predict(start = 0,end =N-1)
    res = arma.resid
    am=arch_model(res, **garch_order)
    g = am.fit(update_freq=0,disp="off")
    ev = g.conditional_volatility
    eVaR = np.zeros(N)
    for i,mu_i in enumerate(mu):
        eVaR[i] = mu_i - _q * ev[i]
     
    #将source的VaR作为外生变量代入target的均值方程
    e = target
    cvar = cVaR
    evar = eVaR
    arma_ = ARIMA(endog = e, order = arma_order, exog = cvar).fit()
    mu_ = arma_.predict(start = 0, end = N-1, exog = cvar)
    res_ = arma_.resid
    am_=arch_model(res_,**garch_order)
    g_ = am_.fit(update_freq = 0, disp="off")
    cv_ = g_.conditional_volatility

    CoVaR = np.zeros(N)
    delta_CoVaR = np.zeros(N)
    percent_CoVaR = np.zeros(N)
    for i,mu_i in enumerate(mu_):
        CoVaR[i] = mu_i - _q * cv_[i]
        delta_CoVaR[i] = CoVaR[i] - evar[i]
        percent_CoVaR[i] = (CoVaR[i]- evar[i]) / evar[i]
    return {"CoVaR":CoVaR, "dCoVaR":delta_CoVaR, "pCoVaR":percent_CoVaR}


def GARCH_CoVaR(source:pandas.DataFrame,
                target:pandas.DataFrame,
                q = 0.95,
                arma_order=(1,0,0),
                garch_order={"p":1,"o":0,"q":1},
                CoVaR_type = ["CoVaR","dCoVaR","pCoVaR"],
                to_plot = False,
                to_save = False,
                save_in = None):

    source_name = source.columns[0]
    target_name = target.columns[0]
    
    data = pandas.merge(source, target,on ="time",how = "inner")
    _tl = data.index
    _data = np.array(data)
    _source = _data[:,0]
    _target = _data[:,1]
    _covar = _garch_covar(_source, 
                         _target,
                         q,                
                         arma_order,
                         garch_order)
    _result = pandas.DataFrame({"date":_tl})
    for typ in CoVaR_type:
        _result[typ] = _covar[typ]
    _result = _result.set_index("date")
    
    if to_plot:
        _result.plot(figsize = (10,2))
    if to_save:
        if save_in[-1] != "/":
            save_in = save_in + "/" 
        _save_name = source_name + "_to_" + target_name + ".csv"
        _result.to_csv(save_in + _save_name)
    
    return _result

