# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 18:44:00 2023

@author: win10
"""
# from qytoolspkg.stocks.info import dictionary,swindustrycode,now
# import os
# import akshare as ak
# import time
# from tqdm import tqdm
# import datetime
# import pandas as pd


# def akupdate(path,
#              codes,
#              akfunc,
#              func_kws:dict,
#              col_use,
#              ):
#     """
#     akfunc参数包括：symbol, start_date, end_date 
#     col_use第一个元素是time axis
#     """
#     exist_csv = os.listdir(path)
#     cse = [c.split("_") for c in exist_csv] # code, start, end
#     codeinfo = {c[0]:[path + exist_csv[i],c[1],c[2][:-4]] for i,c in enumerate(cse)}
#     # {code: [path, start, end]}
#     time_col = col_use[0]
#     def _update(c):
#         if c in codeinfo:
#             old_path = codeinfo[c][0]
#             _start = codeinfo[c][1]
#             _end = codeinfo[c][2]
#             if pd.to_datetime(_end)>=pd.to_datetime(now):
#                 return False
#             start = _end
#         else:
#             start = "20000101"
#             _start = start
#         new = akfunc(symbol = c,
#                      start_date=start,
#                      end_date = now,
#                      **func_kws)
        
#         new = new[col_use]
#         new[time_col] = pd.to_datetime(new[time_col])
#         new = new.set_index(time_col)
#         if c in codeinfo:
#             old = pd.read_csv(old_path,usecols=col_use, parse_dates=[time_col],index_col=time_col)
#             new = pd.concat([old, new],axis = 0).drop_duplicates()
#             assert(not(new.index.duplicated().any()))
#             os.remove(old_path)
#         new.to_csv(f"{path}{c}_{_start}_{now}.csv")
#         return True
#     for c in tqdm(codes):
#         try:
#             sleep = _update(c)
#         except Exception as e:
#             print(f"error when update: {c}")
#             print(e)
#             sleep = True
#         if sleep:
#             time.sleep(6)
#     return 

# def update_stocks(adj = "hfq"):    
    
#     path =  f"{BASIC}/allstocks_{adj}/"
#     codes = list(dictionary.keys())    
#     col_use = ["日期","开盘","收盘","最高","最低","成交量","成交额","振幅","涨跌幅","涨跌额","换手率"]
#     akupdate(path, codes, ak.stock_zh_a_hist, {"adjust":adj}, col_use)

#     return

# def update_index():
#     path = f"{BASIC}/index_ts/"
#     indexes = ["sh000001","sz399001"]
#     col_use = ["date","open" ,"close" ,"high","low","volume","amount"]
#     akupdate(path, indexes, ak.stock_zh_index_daily_em, {}, col_use) 
    
#     # index名称列表，目前仅更新上证和深圳
#     # print(stock_zh_index_spot_df)
#     # stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sz399552")
#     # print(stock_zh_index_daily_df)
#     return 
    
# def update_swlv1():
#     codes = swindustrycode()
#     for c in tqdm(codes.cdic):
#         ts = ak.index_level_one_hist_sw(c)
#         ts.to_csv(f"{BASIC}/swlv1/ts/{c}.csv")
#         time.sleep(6)


# def update_sheets():
    
#     sndic = {"zcfz":"资产负债表",
#               "lr":"利润表",
#              "xjll":"现金流量表"}
#     # codes = list(dictionary.keys())  
#     codes = ["688478","688479"]
#     for c in tqdm(codes):
#         # for sn in sndic:
#         for sn in ["xjll"]:
#             try:
#                 df = ak.stock_financial_report_sina(stock=c, symbol=sndic[sn])
#                 df.to_csv(f"{BASIC}/sheet_{sn}/{c}.csv")
#             except:
#                 print(f"error occured {c}{sn}")
                    
#             time.sleep(6)
#     return 
            
# def update_individual_infos():
#     for c in tqdm(list(dictionary.keys())):
#         try:
#             df = ak.stock_individual_info_em(symbol=c)
#             df = df.set_index("item")
#             df.to_csv(f"{BASIC}/stocksinfo/infos/{c}.csv")
#         except:
#             print(f"error occured {c}")
#         time.sleep(6)
#     return 

# import warnings
# warnings.filterwarnings("ignore")
# def update_indicators():
#     codes = list(dictionary.keys())  
#     for i,c in enumerate(codes):
#         if c+".xlsx" in os.listdir(f"{BASIC}/indicators/all/"):
#             continue
#         print(i)
#         try:
#             dfa = ak.stock_financial_analysis_indicator(symbol=c, start_year="2000")
#             dfa = dfa.set_index("日期")
#             dfa.to_excel(f"{BASIC}/indicators/all/{c}.xlsx")
#         except:
#             print(f"error occured {c} all")
#         time.sleep(6)
        
#         # try:
#         #     dfb = ak.stock_financial_abstract(symbol=c)
#         #     dfb = dfb.set_index("指标")
#         #     dfb.to_excel(f"{BASIC}/indicators/abstract/{c}.xlsx")
#         # except:
#         #     print(f"error occured {c} abstract")

#         time.sleep(6)
#     return 
    


# if __name__ == "__main__":
#     # update_stocks()
#     # update_index()
#     # update_swlv1()
#     # update_sheets()
#     # update_individual_infos()
#     # "600004"
#     # update_indicators()
