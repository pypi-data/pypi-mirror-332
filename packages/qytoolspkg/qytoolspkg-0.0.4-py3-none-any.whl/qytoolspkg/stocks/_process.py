# -*- coding: utf-8 -*-
"""
处理从BASIC -> PROCESS的部分数据，不能被调用

Created on Wed May 22 15:18:32 2024

@author: qiyu
"""

import pandas as pd
from qyshare.path import BASIC, PROCESS
from qyshare.core.stocks.info import dictionary
from tqdm import tqdm
from qyshare.core.basictools.basicfunc import mymkdir
import sys


def _csrc_industry():
    df = pd.read_excel(BASIC + "/stocksinfo/industry/证监会行业.xlsx")
    df.columns = [c[:-3] for c in df.columns]
    df["time"] = [pd.Timestamp(pd.Period(str(y)[:4]).end_time.date()) \
                        for y in df["D"]] 
    
    df = df.set_index("time")
    df = df.drop("D", axis = 1)
    # all_ind = np.array(df).reshape(1,-1)[0]
    # all_ind = [s for s in all_ind if type(s) == str]
    # all_ind = list(set(all_ind))
    sys.exit()
    for code in tqdm(dictionary):
        if code in df.columns :
            ind = df[[code]]
            ind.columns = ["csrc_industry"]
            ind = ind.dropna()
            ind.to_csv(BASIC + f"/stocksinfo/industry/csrc/{code}.csv")



def _financing_constrains():
    idx = "KZ"
    idx_ = "kz"
    
    df = pd.read_excel(BASIC + f"/融资约束/融资约束—{idx}指数/BDT_FinConst{idx}.xlsx")
    df_ =  df.iloc[2:].dropna()
    comps = df["Symbol"]
    
    comps = set(comps)
    for c in comps:
        d = df_[df_["Symbol"] == c]
        fc000 =  d[(d["STPT"] == 0) & (d["IsNewOrSuspend"] == 0) & (d["ISBSE"] == 0)][["Enddate",idx]].set_index("Enddate")
        
        fc100 =  d[(d["STPT"] == 1) & (d["IsNewOrSuspend"] == 0) & (d["ISBSE"] == 0)][["Enddate",idx]].set_index("Enddate")
        fc001 =  d[(d["STPT"] == 0) & (d["IsNewOrSuspend"] == 0) & (d["ISBSE"] == 1)][["Enddate",idx]].set_index("Enddate")
        fc010 =  d[(d["STPT"] == 0) & (d["IsNewOrSuspend"] == 1) & (d["ISBSE"] == 0)][["Enddate",idx]].set_index("Enddate")
        
        fc110 =  d[(d["STPT"] == 1) & (d["IsNewOrSuspend"] == 1) & (d["ISBSE"] == 0)][["Enddate",idx]].set_index("Enddate")
        fc101 =  d[(d["STPT"] == 1) & (d["IsNewOrSuspend"] == 0) & (d["ISBSE"] == 1)][["Enddate",idx]].set_index("Enddate")
        fc011 =  d[(d["STPT"] == 0) & (d["IsNewOrSuspend"] == 1) & (d["ISBSE"] == 1)][["Enddate",idx]].set_index("Enddate")
        
        fc111 =  d[(d["STPT"] == 1) & (d["IsNewOrSuspend"] == 1) & (d["ISBSE"] == 1)][["Enddate",idx]].set_index("Enddate")
    
    
        mymkdir(PROCESS + f"/financing_constrains/{c}")
        fc000.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}000.csv")
        fc100.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}100.csv")
        fc001.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}001.csv")
        fc010.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}010.csv")
        fc110.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}110.csv")
        fc101.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}101.csv")
        fc011.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}011.csv")
        fc111.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}111.csv")
        
        
def _financing_constrains_1():
    idx = "SA"
    idx_ = "sa"
    
    df = pd.read_excel(BASIC + f"/融资约束/融资约束—{idx}指数/BDT_FinConst{idx}.xlsx")
    df_ =  df.iloc[2:].dropna()
    comps = df["Symbol"]
    
    comps = set(comps)
    for c in comps:
        d = df_[df_["Symbol"] == c]
        fc00 =  d[(d["STPT"] == 0) & (d["IsSuspend"] == 0) ][["Enddate",idx]].set_index("Enddate")
        fc10 =  d[(d["STPT"] == 1) & (d["IsSuspend"] == 0) ][["Enddate",idx]].set_index("Enddate")
        fc01 =  d[(d["STPT"] == 0) & (d["IsSuspend"] == 1) ][["Enddate",idx]].set_index("Enddate")
        fc11 =  d[(d["STPT"] == 1) & (d["IsSuspend"] == 1) ][["Enddate",idx]].set_index("Enddate")
        
    
    
        mymkdir(PROCESS + f"/financing_constrains/{c}")
        fc00.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}00.csv")
        fc10.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}10.csv")
        fc01.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}01.csv")
        fc11.to_csv(PROCESS + f"/financing_constrains/{c}/{idx_}11.csv")

          
_financing_constrains_1()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    