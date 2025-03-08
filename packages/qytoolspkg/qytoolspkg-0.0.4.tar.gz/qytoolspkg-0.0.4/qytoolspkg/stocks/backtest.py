# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:16:37 2023

@author: qiyu
"""

import pandas as pd
from qytoolspkg.stocks.info import now
from qytoolspkg.stocks.reader import stock, shanghai
import numpy as np
import datetime
from tqdm import tqdm
sell_loss_rate = 0.001
buy_loss_rate = 0.001
        
def _fee(old_pos, new_pos):
    sell = 0
    # print(old_pos,new_pos)
    for k in old_pos:
        if not(k in new_pos):
            sell += old_pos[k]
        else:
            _v = old_pos[k] - new_pos[k]
            _v = _v if _v>0 else 0
            sell += _v
            
    buy = 0
    for k in new_pos:
        if not(k in old_pos):
            buy += new_pos[k]
        else:
            _v = new_pos[k] - old_pos[k]
            _v = _v if _v>0 else 0
            buy += _v
            
    return sell * sell_loss_rate + \
        buy * buy_loss_rate
    
def _span(x, pdic_i_1, df_i_1):
    start = x["start"]
    end = x["end"]
    pdic = x["pdic"]
    assert(0.999 < sum(pdic.values()) <1.001)
    value = df_i_1.iloc[-1]["value"]
    old_pos = {}
    # print(pdic_i_1)
    for k in pdic_i_1:
        old_pos[k] = df_i_1.iloc[-1][k]
    new_pos = {k: value * pdic[k] for k in pdic}
    
    fee = _fee(old_pos, new_pos)
    value = value - fee
    # print(fee)
    indexes = pd.date_range(start, end)
    df = pd.DataFrame()
    df.index = indexes
    df.index.name = "time"
    df_list = []
    for s in pdic:
        df_s = df.copy()
        stk = stock(s)
        close = stk.close().resample("D").ffill()
        open_ = stk.open_().resample("D").bfill()#向后插值
        close_series = close[start: end]
        start_price = open_.loc[start]["open"]
        position = value * pdic[s] * close_series / start_price
        df_s[s] = position
        df_list.append(df_s)
    df_tot = pd.concat(df_list, axis = 1)
    df_v = df.copy()
    df_v["value"] = np.array(df_tot).sum(axis = 1)
    df_tot = pd.concat([df_tot, df_v], axis = 1)
    return df_tot
        
def simple_backtest(ptf: pd.DataFrame(),
                    value = 1e8,
                    end = pd.Timestamp(now)):
    """
    ptf:
    time: {stock:share, stock:share}
    time: ....
            
    sum(share) = 1
    """ 
    ptf.index = pd.to_datetime(ptf.index)
    ptf = ptf.sort_index()    
    ptf.columns = ["pdic"]    
    # ptf.loc[end] = [{"nan":0}]
    ptf["start"] = ptf.index
    ptf["end"] = ptf["start"].shift(-1)
    
    ptf.iat[-1,2] = end
    # print(end)
    # print(ptf)
    df = pd.DataFrame(columns=["value"])
    df.index.name = "time"
    df.loc[ptf.index[0] - datetime.timedelta(days=1)] = [value]
    dfi = df.copy()
    # print(dfi)
    pdic_i_1 = {}
    for i, idx in tqdm(list(enumerate(ptf.index[:]))):        
        dfi = _span(ptf.loc[idx], pdic_i_1, dfi)
        df = pd.concat([df,dfi[["value"]]], axis = 0)
        pdic_i_1 = ptf.loc[idx]["pdic"]
    return df.dropna()
        
def plot_simple_backtest(ptf: pd.DataFrame(),
                         value = 1e8,
                         end = now,
                         benchmark = shanghai.close(),
                         ):
    end = pd.Timestamp(end)
    df = simple_backtest(ptf, value, end)
    bc = benchmark
    df = pd.merge(df, bc, how = "inner", on = "time")
    df.columns = ["value","benchmark"]
    df["benchmark"] = df["benchmark"] / df.iloc[0]["benchmark"]
    df["value"] = df["value"] / df.iloc[0]["value"]
    df.plot()
    return df


if __name__ == "__main__":
    ptf = {"time":[pd.Timestamp('2020-1-1'),pd.Timestamp('2021-1-1'),pd.Timestamp('2022-1-1')],
           "pdic":[{"000002":0.5,"600606":0.5},
                   {"600606":1},
                   {"600004":0.4,"000002":0.6}]}
    ptf = pd.DataFrame(ptf)
    
    ptf = ptf.set_index("time")
    df = plot_simple_backtest(ptf)
        