# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:13:51 2022

@author: win10
"""
import numpy as np
from datetime import date,datetime
from pandas import Timestamp
    
int_types =[int, np.int32, np.int64, np.int16]

float_types = [float, np.float16, np.float32,np.float64]

scalar_types = int_types + float_types
vector_types = [list, np.ndarray,np.array]
matrix_types = vector_types + [np.matrix]

str_types = [str, np.str_]

datetime_types = [date, datetime,  Timestamp]

str_nan_symbol = ['nan', 'none', 'None']


def isnpnan(x):
    if type(x)==float:
        return np.isnan(x)
    else:
        return False


def missvalue(x):
    if type(x) in float_types:
        if np.isnan(x):
            return True
    return False
def missvalue_series(s):
    _ = np.array([missvalue(si) for si in s])
    return _
    
def nan_types(x):
    if x is None:
        return True
    if type(x) in str_types:
        if x in str_nan_symbol:
            return True
        else:
            return False
    try:
        if np.isnan(x): return True
    except:
        raise TypeError(f"{type(x)}:{x}")
    return False

def existnan(x, raiseError = True):
    # print(x,type(x))
    if type(x) in vector_types + matrix_types:
        x = np.array(x).reshape(1,-1)[0]
        for xi in x:
            if existnan(xi): 
                return True
        return False
    elif nan_types(x):
        return True
    elif type(x) in str_types + scalar_types:
        return False
    else:
        if raiseError:
            raise TypeError(f"cannot recognize {x}:{type(x)}")
        else:
            return  False

def samething(x,y):
    if existnan(x) and existnan(y):
        return True
    for tps in [scalar_types, str_types, datetime_types]:
        if type(x) in tps:
            if type(y) in tps:
                return x == y
            else:
                return False
        else:
            pass
    if type(x) in matrix_types:
        if type(y) in matrix_types:
            x = np.matrix(x).reshape(1,-1)[0]
            y = np.matrix(y).reshape(1,-1)[0]
            if len(x) != len(y):
                return False
            _ = all([x[i] == y[i] for i in range(len(x))])
            return _
    raise TypeError(f"x:{x},y:{y},{type(x)} not found!")

class ignore_nan:
    """
    a decorator to let input in nan types return np.nan
    """
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        for a in args:
            if existnan(a):
                return np.nan
        for k in kwargs:
            if existnan(kwargs[k]):
                return np.nan
        return self.func(*args, **kwargs)
if __name__ == "__main__":
    print(missvalue([]))