# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 23:16:51 2022

@author: win10
"""

from qytoolspkg.basictools.mytypes import *

def cdf_norm(x: matrix_types):
    x = np.array(x)
    xs = x.shape
    if len(xs) == 1:
        x_ = x
    else:
        x_ = x.reshape(1,-1)[0]
    sort_index = np.argsort(np.argsort(x_))
    cdf_list = sort_index / (len(x_) - 1)
    cdf_list = cdf_list.reshape(xs)
    return cdf_list

def range_norm(x: matrix_types,
               _min:float_types = None,
               _max:float_types = None,
               ):
    x = np.array(x)
    if _min is None:
        _min = min(x)
    if _max is None:
        _max = max(x)
    x_std = (x - _min) / (_max - _min)
    return x_std

def z_score(x: matrix_types):
    x = np.array(x)
    if (~np.isnan(x)).sum() == 0:
        return x
    xmean = x[~np.isnan(x)].mean()
    xstd = x[~np.isnan(x)].std()
    if xstd == 0:
        return np.zeros(x.shape)
    x_std = (x - xmean)/xstd
    return x_std

def z_score_shrinkage(x, q = 0.99):
    x = np.array(x)
    if (~np.isnan(x)).sum() == 0:
        return x
    xmean = x[~np.isnan(x)].mean()
    xstd = x[~np.isnan(x)].std()
    if xstd == 0:
        return np.zeros(x.shape)
    x_std = (x - xmean)/xstd
    _max = np.quantile(x_std, q = q)
    _min = np.quantile(x_std, q = 1-q)
    x_std[x_std > _max] = _max
    x_std[x_std < _min] = _min
    return x_std

    
# def cut_max_min(x, _max = None, _min = None):
#     """
#     _max: float,int,None
#         if float<1, num of cutted = len(x) * _max
#     ...
#     """
    
#     if _max < 1:
        
#     x.sort()
    

if  __name__ == "__main__":
    
    _ = z_score([1,2,3,np.nan])