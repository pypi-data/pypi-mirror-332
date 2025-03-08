# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:15:59 2023

@author: win10
"""

import pandas as pd
import os
import numpy as np
from qytoolspkg.basictools.strtools import month_str
from qyshare.path import BASIC

# class EPU:
    
#     def __init__(self, excel_ = "SNMP", sheet_ =0):
#         self.path = BASIC + "/other/EPU_"+ excel_ + ".xlsx"
#         excel = pd.read_excel(self.path, sheet_name = sheet_)

#         mth = np.array(excel["month"])
#         excel["time"] = [pd.Timestamp(pd.Period(str(y) +"-"+ month_str(mth[i])).end_time.date()) \
#                            for i,y in enumerate(excel["year"])]
#         excel = excel.set_index("time")
#         col = excel.columns[2]
#         self.csv = excel[[col]]
#     def get(self, month):
#         return self.csv.loc[month][2]
    
    
# epu0 = EPU("SNMP")
# epu1 = EPU("mainland","EPU 2000 onwards")
# tpu = EPU("mainland","TPU 2000 onwards")


# # class cbonds:
# #     def __init__(self, due = 10):
# #         if due == 10:
# #             path = BASIC + "/other/" + "china10yearsbond.csv"
# #         csv = pd.read_csv(path,parse_dates=["date"], index_col=["date"])
# #         csv["percent"] = [float(s[:-1]) for s in csv["percent"]]
# #         self.csv = csv.sort_values(by=["date"])
# #         for k in self.csv.columns:
# #             setattr(self, k, self.csv[[k]])
        


# class cbonds:
#     def __init__(self):
#         """
#         ak.bond_zh_us_rate(start_date="19901219")
#         中美国债收益率曲线，每日均价，没有开盘收盘等详细信息
#         country = China, USA
#         due = 2, 5, 10, 30
#         """
        
#         path = BASIC + "/macroeco/bonds.xlsx"
#         excel = pd.read_excel(path)
#         excel["time"] = pd.to_datetime(excel["日期"])
#         self.excel = excel.set_index("time")
        
    
#     def get(self, country = "China", due = 10):
#         ndic = {"China":"中",
#                 "USA":"美"}
#         col = f"{ndic[country]}国国债收益率{due}年"
#         r = self.excel[[col]]
#         r.columns = [f"{country}{due}"]
#         r = r.dropna()
#         return r
        
# shvix:pd.DataFrame = pd.read_csv(BASIC + "/other/" + "vix.csv",parse_dates=["date"], index_col=["date"])
# shvix.index.name = "time"


# if __name__ == "__main__":
#     df = cbonds().get()