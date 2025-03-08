# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:22:03 2023

@author: win10
"""

import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
from qytoolspkg.basictools.basicfunc import pdiv
from qytoolspkg.basictools.basicfunc import remember
from itertools import permutations

def to_series(x:pd.DataFrame):
    if type(x) == pd.Series:
        return x
    elif type(x) == pd.DataFrame:
        name = x.columns[0]
        x = pd.Series(x[name].values, index = x.index)
        return x
    else:
        raise TypeError()
        
def statistics_summary(df):
    """
    生成输入 DataFrame 的基本统计结果表。

    参数:
        df (pd.DataFrame): 输入的多维时间序列数据，变量名称在列名称中。

    返回:
        pd.DataFrame: 包含基本统计指标的结果表。
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("输入数据必须是 pandas DataFrame 类型。")

    # 确保数据中不存在空值
    if df.isnull().any().any():
        print("警告：输入数据包含缺失值，已自动忽略缺失值。")
        df = df.dropna()

    # 计算基本统计结果
    summary = pd.DataFrame({
        "Mean": df.mean(),          # 均值
        "Std Dev": df.std(),        # 标准差
        "Min": df.min(),            # 最小值
        "25%": df.quantile(0.25),   # 第一四分位数
        "Median": df.median(),      # 中位数
        "75%": df.quantile(0.75),   # 第三四分位数
        "Max": df.max(),            # 最大值
        "Skewness": df.skew(),      # 偏度
        "Kurtosis": df.kurt(),      # 峰度
    })

    # 为方便查看，结果保留两位小数
    summary = summary.round(2)

    return summary

def vts_lw_before(x, date, lw):
    """
    vts
    get lw valid data before date
    """
    date = pd.to_datetime(date)
    if not(date in x.index):
        for t in x.index:
            if t >= date:
                date = t
                break
                
    x["index"] = x.index
    date = pd.to_datetime(date)
    x.index = range(len(x))
    k = x[x["index"] == date].index().to_list()[0]
    x_ = np.array(x)
    return x_[k - lw: k]

# def roll(x:pd.DataFrame,
#          y:pd.DataFrame,
#          func:callable,
#          lw: int,
#          func_kwd:dict = {},
#          name = None,
#          return_df = True):
    
#     data = pd.merge(x, y, how = "inner", on = x.index.name)
#     _d = np.array(data)
#     _result = []
    
#     for k in range(lw, len(_d)):
#         _r = func(_d[k-lw:k,0],_d[k-lw:k,1],**func_kwd)
#         _result.append(_r)
    
#     if return_df:
#         if name is None:
#             name  = func.__name__
#         df = pd.DataFrame({name: _result})
#         df.index = data.index[lw:]
#         return df
#     else:
#         return np.array(_result), np.array(data.index[lw:])

# # 假设 x 和 y 是 DataFrame，函数 func 是你定义的计算逻辑
# data = pd.merge(x, y, how="inner", on=x.index.name)
# # 使用 Pandas 的 rolling 方法
# result = data.rolling(window=lw).apply(lambda row: func(row[0], row[1], **func_kwd), raw=False)
# # 结果
# result.index = data.index[lw:]


def merge_resample(x:pd.DataFrame, 
                   start = "1990",
                   freq = "Y",
                   dropna = True):
    """
    按freq生成从start开始到现在的date_range作为index,与x进行merge
    特性：只会按date_range生成的index保留数据
    """
    timerange = pd.date_range(start, datetime.datetime.now(), freq = freq)
    _df = pd.DataFrame({"time":timerange,"_":range(len(timerange))})
    _df = _df.set_index("time")
    df = pd.merge(x, _df, how = "right", on = "time")
    df = df[x.columns]
    if dropna:
        return df.dropna()
    else:
        return df
    
def nearest_tradeday(t, idx, before = True, tol = 15):

    sgn = -1 if before else 1         
        
    date = pd.to_datetime(t).date()
    for dt in range(1,tol):  
        t_ = pd.to_datetime(date + datetime.timedelta(days = sgn * dt))
        if t_ in idx:
            break
        else:
            t_ = None
    return t_    

def bitsop(x:pd.DataFrame,
           func = "diff",
           delta = "Y",
           dropna = True):
    """
    timeseries binary operations
    func(xt, xt-delta) -> result
    
    func: str or function
        str
            diff:        x0-x1
            growth_log:  np.log(x0)/np.log(x1)
            growth:      pdiv((x0 - x1) , x1)
        function
            func(xt, xt-delta) -> res

    将x按时间间隔做操作
    delta = "D" "W" "M" "Q" "Y"
    """
    # 减去一天
    # xi - datetime.timedelta(days=1)
    # 减去一年
    # xi - relativedelta(years=1)
    # 减去一月
    # xi - relativedelta(months=1)
    # 减去一周
    # xi - relativedelta(weeks=1)
    x = x.copy()
    if func == "diff":
        func = lambda x0, x1: x0-x1
        func.__name__ = "diff"
    elif func == "growth_log":
        func = lambda x0, x1: np.log(x0)/np.log(x1)
        func.__name__ = "growth_log"
    elif func == "growth":
        func = lambda x0, x1: pdiv((x0 - x1) , x1)
        func.__name__ = "growth"
    else:
        pass
    cols = x.columns
    
    if delta == "D":
        dt = datetime.timedelta(days=1)
    elif delta == "W":
        dt = relativedelta(weeks=1)
    elif delta == "M":
        dt = relativedelta(months=1)
    elif delta == "Q":
        dt = relativedelta(months=3)
    elif delta == "Y":
        dt = relativedelta(years=1)
    else:
        assert(hasattr(delta, '__call__'))
        dt = delta    

    res_cols = []
    for c in cols:  
        def _shift(xi):
            t = xi.name
            _t = t - dt
            if _t in x.index:
                _xi = x.loc[_t][c]
            else:
                _xi = np.nan
            return func(xi[c], _xi)
        rcn = c + "_" + func.__name__
        x[rcn] = x[[c]].apply(_shift, axis = 1)    
        res_cols.append(rcn)

    if dropna:
        return x[res_cols].dropna()
    else:
        return x[res_cols]

def expand_df(df, date_range, fill = "zero"):

    df_expanded = df.reindex(date_range)
    if fill == "zero":
        df_filled = df_expanded.fillna(0)
    elif fill == "average":
        df_filled = df_expanded.apply(lambda x: x.fillna(x.mean()))
    else:
        raise Exception()
    return df_filled

def dummy(y):
    """
    把01array序列变为pandas dummies
    """
    import pandas as pd
    if type(y[0])!=str :
        y = [str(i) for i in y]
    df=pd.DataFrame(y)
    df1=pd.get_dummies(df,prefix = "y")
    return df1 
        
if __name__ == "__main__":
    

    1