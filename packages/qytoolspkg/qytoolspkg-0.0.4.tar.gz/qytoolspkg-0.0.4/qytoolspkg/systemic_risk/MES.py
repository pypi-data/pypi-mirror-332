# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:09:30 2025

@author: qiyu
"""
from qytoolspkg.systemic_risk.DCC_GARCH import *
from qytoolspkg.stocks.reader import stock, swlv1, shanghai
def _mes(rm, ri, alpha=0.95):

    rho,ht_m,ht_i = dcc_garch_r_script(rm, ri)
    c = np.quantile(rm, alpha)
    
    # ===================================
    # MES MatLab program.
    # em=data$rm/ht_m                        #  market first column
    # xi=(data$ri/ht_i-rho*em)/sqrt(1-rho^2) #  asset second column
    # bwd=nrow(data)^(-0.2)                  #  Scaillet's bwd p21
    # K1=sum(em*pnorm((c/ht_m-em)/bwd))/sum(pnorm(c/ht_m-em)/bwd)
    # K2=sum(xi*pnorm((c/ht_m-em)/bwd))/sum(pnorm(c/ht_m-em)/bwd)
    # MES = (ht_i*rho*K1) + (ht_i*sqrt(1-rho^2)*K2)
    # return(-MES)
    # ===================================
    
    pnorm = st.norm._cdf
    em=rm/ht_m                        #  market first column
    xi=(ri/ht_i-rho*em)/np.sqrt(1-rho**2) #  asset second column
    bwd=2**(-0.2)                  #  Scaillet's bwd p21
    K1=sum(em*pnorm((c/ht_m-em)/bwd))/sum(pnorm(c/ht_m-em)/bwd)
    K2=sum(xi*pnorm((c/ht_m-em)/bwd))/sum(pnorm(c/ht_m-em)/bwd)
    MES = (ht_i*rho*K1) + (ht_i*np.sqrt(1-rho**2)*K2)
    return -1 * MES

def MES(company, 
        market = shanghai.logreturn(),  
        alpha = 0.95,
        to_plot = False,
        to_save = False,
        save_in = None) -> pandas.DataFrame:
    
    if type(company) == str:
        target_name = company
        company = stock(company).logreturn()
    if type(market) == str:
        source_name = market
        market = swlv1(market).logreturn()
    
    source_name = market.columns[0]
    target_name = company.columns[0]
    
    data = pandas.merge(market, company,on ="time",how = "inner")
    data = data.dropna()
    _tl = data.index
    _data = np.array(data)
    _source = _data[:,0]
    _target = _data[:,1]
    _m = _mes(_source, _target, alpha)

    
    _result = pandas.DataFrame({"date":_tl, "MES":_m})
    _result = _result.set_index("date")
    
    if to_plot:
        _result.plot(figsize = (10,2))
    if to_save:
        if save_in[-1] != "/":
            save_in = save_in + "/" 
        _save_name = source_name + "_to_" + target_name +"_" + ".csv"
        _result.to_csv(save_in + _save_name)

    return _result

    
def LRMES(mes):
    mes["LRMES"] = mes["MES"].apply(lambda x: 1-np.exp(-18*x))
    return mes

if __name__ == "__main__":
    
    
    from stocks.reader import shanghai,stock
    c = stock("600606")
    _ = MES(shanghai.logreturn(), c.logreturn())
    print(_["2012":"2013"])
