# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 22:29:26 2022

@author: win10
"""
# import os
# from rpy2.robjects import pandas2ri
# import rpy2.robjects as objects 
from rpy2 import robjects
import numpy as np
# import pandas
# from qytoolspkg.basictools.mycheck import sample_x
# import scipy.stats as st
from rpy2.robjects import numpy2ri
# from Rscript.dcc_garch.dcc_garch import dcc_garch_r_script
import qytoolspkg.consts


def dcc_garch_rpy2(x, y, dt_time=None, forecast_days = None):
    """
    2 variables dcc.
    armaOrder: (0,0)
    garchOrder: (1,1)
    dccOrder: (1,1)
    distribution: norm, mvnorm
        ugarch("norm","std","sstd","ged","sged","nig"....)
        https://www.rdocumentation.org/packages/rugarch/versions/1.4-8/topics/ugarchspec-methods
        dccspec("mvnorm", "mvt", "mvlaplace")
        https://search.r-project.org/CRAN/refmans/rmgarch/html/dccspec-methods.html
    Parameters
    ----------
    x: array
    y: array
    
    """
    # pd_rets - a pandas dataframe of daily returns, where the column names are the tickers of stocks and index is the trading days.
    
    # compute DCC-Garch in R using rmgarch package
    # x = sample_x(x)
    # y = sample_x(y)

    # pandas2ri.activate()
    numpy2ri.activate()
    if dt_time is None:
        dt_time = np.array(range(len(x)))
    # pd_rets = pandas.DataFrame(np.hstack([x,y]),columns=["a","b"],index = dt_time)
    
    if forecast_days is None:
        n_days = 1
    else:
        n_days = forecast_days
    # r_rets = pandas2ri.py2rpy_pandasdataframe(pd_rets) # convert the daily returns from pandas dataframe in Python to dataframe in R
    
    # with (robjects.default_converter + pandas2ri.converter).context():
    #     r_rets = robjects.conversion.get_conversion().py2rpy(pd_rets)
    r_rets = np.hstack([x,y])
    r_dccgarch_code = """
                    library('rmgarch')
                    function(r_rets, n_days){
                            univariate_spec <- ugarchspec(mean.model = list(armaOrder = c(0,0)),
                                                        variance.model = list(garchOrder = c(1,1),
                                                                            variance.targeting = FALSE, 
                                                                            model = "sGARCH"),
                                                        distribution.model = "norm")
                            n <- dim(r_rets)[2]
                            dcc_spec <- dccspec(uspec = multispec(replicate(n, univariate_spec)),
                                                dccOrder = c(1,1),
                                                distribution = "mvnorm")
                            dcc_fit <- dccfit(dcc_spec, data=r_rets)
                            forecasts <- dccforecast(dcc_fit, n.ahead = n_days)
                            
                            Rho=rcor(dcc_fit)
                            rho=as.data.frame(Rho[1,2,])
                            sigma = sigma(dcc_fit)
                            cov = rcov(dcc_fit)
                            list(rho, sigma, cov, forecasts@mforecast$H)
                    }
                    """
                    # COV=rcov(dcc_fit)
                    # COV11=as.data.frame(COV[1,])
                      # COV22=as.data.frame(COV[2,]);COV = sigma(dcc_fit)条件方差也可以用这个
    r_dccgarch = robjects.r(r_dccgarch_code)
    r_res = r_dccgarch(r_rets,n_days)
    # pandas2ri.deactivate()
    numpy2ri.deactivate()
    # end of R
    
    rho = r_res[0] # 条件相关系数
    sigma = np.array(r_res[1]) # 两个变量的条件方差
    sigma0 = sigma[:,0]
    sigma1 = sigma[:,1]
    covariance_matrix = r_res[2]
    # var1 = r_res[2]
    # forecast = r_res[3] # forecasted covariance matrices for n_days
    # if forecast_days is None:
    return np.array(rho)[0], np.array(sigma0), np.array(sigma1)



