# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:10:55 2023

@author: win10
"""
# from qyshare.path import BASIC
import pandas as pd
import numpy as np
# import akshare as ak
from qytoolspkg.basictools.strtools import fill0forstockcode
# from tqdm import tqdm
import datetime
from qytoolspkg.basictools.dbtools import fetch_table
from qytoolspkg.consts import DB_CONFIG, DATE_FORMAT

"""
目前仅包括
沪深京 A股的股票，代码数字不会重复，但和境外股票，债券间代码可能重复，届时需要加入后缀。
http://quote.eastmoney.com/center/gridlist.html#hs_a_board

"""

__all__ = [
    "dictionary",
    "swindustry",#表格里只有4430条，其他为 -
    # "swindustrycode",
    # "comp_is_st",
    "province",#表格里只有4773条，其他为 -
    "city",#表格里只有4773条，其他为 -
    # "getinfo",
    "market_by_code",
    # "is_st",
    "now"
    ]

now = (datetime.datetime.now() - pd.Timedelta("1d")).date().strftime(DATE_FORMAT)
# now = (datetime.datetime.now() - pd.Timedelta("1d")).date()


# def _gen_dictionary():
#     #A股
#     df = ak.stock_info_a_code_name()
#     df = df.set_index("code")
    
#     szde = ak.stock_info_sz_delist("终止上市公司")
#     shde = ak.stock_info_sh_delist()
    
#     szde.columns = ["code","name","list_date","de_date"]
#     shde.columns = ["code","name","list_date","de_date"]
#     de = pd.concat([shde, szde], axis = 0)
#     de = de.drop_duplicates(subset = "code", keep = "last")
#     de = de.set_index("code")
#     for c in de.index:
#         if not(c in df.index):
#             df.loc[c] = de.loc[c][["name"]]
#     de.index = ["\t" + i for i in de.index]
#     de.index.name = "code"
#     de.to_csv(f"{BASIC}/stocksinfo/delist.csv")
#     return df

# def _gen_swindustry():
#     """
#     直接拼接ak下载的sw成分股
#     {code: industry}
#     """
#     swlv1 = ak.sw_index_first_info()
#     swlv1.to_csv(f"{BASIC}/swlv1/ak/lv1info.csv")
#     inds = []
#     for c in tqdm(swlv1["行业代码"]):
#         cc = c[:-3]
#         df = ak.index_component_sw(symbol=cc)
#         df.to_csv(f"{BASIC}/swlv1/ak/{cc}.csv")
#         code = list(df["证券代码"])
#         ind = pd.DataFrame({"code":code,"swindustry":[cc]*len(code)})
#         ind = ind.set_index("code")
#         inds.append(ind)
#     df = pd.concat(inds)
#     return df

def csrc_industry_convert(ind):
    if type(ind)!=str:
        return "NaN"
    else:
        industry_mapping = {
            '交通运输、仓储业': "交通运输",
            '交通运输、仓储和邮政业': "交通运输",
            '传播与文化产业': '传播与文化产业',
            '住宿和餐饮业': '住宿和餐饮业',
            '信息传输、软件和信息技术服务业': '信息技术与信息服务',
            '信息技术业': '信息技术与信息服务',
            '农、林、牧、渔业': '农林牧渔业',
            '制造业': '制造业',
            '卫生和社会工作': '卫生和社会工作',
            '居民服务、修理和其他服务业': '居民服务和其他服务业',
            '建筑业': '建筑业',
            '房地产业': '房地产业',
            '批发和零售业': '批发和零售业',
            '批发和零售贸易': '批发和零售业',
            '教育': '教育',
            '文化、体育和娱乐业': '文化、体育和娱乐业',
            '水利、环境和公共设施管理业': '水利、环境和公共设施管理',
            '电力、热力、燃气及水生产和供应业': '能源供应业',
            '电力、煤气及水的生产和供应业': '能源供应业',
            '社会服务业': '社会服务业',
            '科学研究和技术服务业': '科学研究和技术服务',
            '租赁和商务服务业': '租赁和商务服务',
            '综合': '综合',
            '综合类': '综合',
            '采掘业': '采矿业',
            '采矿业': '采矿业',
            '金融、保险业': '金融保险业',
            '金融业': '金融保险业'}
        return industry_mapping[ind]


# def _gen_region_npy():
#     """
#     每个公司的注册地址都可能会变化，应该是时间序列数据，然而绝大部分都是不变的，
#     为方便，仅采用最后一个注册地.
#     """
#     rg = pd.read_excel(f"{BASIC}/stocksinfo/region.xlsx", usecols = ["Symbol","PROVINCE","CITY"])
#     code = np.array(rg["Symbol"])
#     prov = np.array(rg["PROVINCE"])
#     city = np.array(rg["CITY"])
#     prov_arr = []
#     city_arr = []
#     code_arr = []
    
#     for i, c in enumerate(code[:-1]):
#         if c != code[i+1]:
#             code_arr.append(fill0forstockcode(c))
#             prov_arr.append(prov[i])
#             city_arr.append(city[i])

#     df = pd.DataFrame({"code":code_arr,
#                        "province":prov_arr,
#                        "city":city_arr})
#     df = df.set_index("code")
#     return df



# def update_info():
#     """
    
#     以下，原始文件生成infocsv，update需要更新原始文件并生成读取文件
#     ------------
#     dictionary:
#         "{BASIC}/stocksinfo/stocklist.csv" 
#         from akshare
        
#     region: 
#         "{BASIC}/stocksinfo/region.xlsx"
#         from wind, by hand
    
#     industry:
#         "{BASIC}/swlv1/ak/" 
#         from akshare
    
#     以下，直接读原始文件
#     --------
#     getinfo:
#         "{BASIC}/stocksinfo/info/{code}.csv"
#         from akshare
        
#     is_st:
#         f"{BASIC}/other/SPT_Trdchg.xlsx"
#         from csmar website, by hand
#     """
#     a = _gen_dictionary()
#     b = _gen_swindustry()
#     df = pd.merge(a, b, on = "code", how = "left")
#     c = _gen_region_npy()
#     df = pd.merge(df, c, on = "code", how = "left")
#     df.index = ["\t" + i for i in df.index]
#     df.index.name = "code"
#     df.to_csv(f"{BASIC}/stocksinfo/infocsv.csv")
#     return 
    

# infocsv = pd.read_csv(f"{BASIC}/stocksinfo/infocsv.csv",
#                       index_col=["code"],
#                       converters={"code":lambda x: str(x[1:]),
#                                   "swindustry":str})
infocsv = fetch_table(DB_CONFIG, "stocks_info", "infocsv", "code")
_infocsv = infocsv.to_dict()
stockcodes = list(infocsv.index)
dictionary = _infocsv["name"]
province = _infocsv["province"]
city = _infocsv["city"]
swindustry = _infocsv["swindustry"]

# class swindustrycode:
#     def __init__(self):
#         self.swcsv = pd.read_csv(f"{BASIC}/swlv1/ak/lv1info.csv")
#         self.cdic = {c[:-3]:self.swcsv.iloc[i]["行业名称"] \
#                      for i,c in enumerate(self.swcsv["行业代码"])}
#         self.cdic[""] = ""
#         self.ndic = {self.cdic[k]:k for k in self.cdic}
        
#     def getcode(self, name):
#         if name in self.ndic.keys():
#             return self.ndic[name]
#         else:
#             assert(name in self.cdic)
#             return name
#     def getname(self, code):
#         if code in self.cdic.keys():
#             return self.cdic[code]
#         else:
#             assert(code in self.ndic)
#             return code    
#     def convert(self, string):
#         if string in self.cdic.keys():
#             return self.cdic[string]
#         else:
#             assert(string in self.ndic)
#             return self.ndic[string]
    
# def swindustrycodename(string):
#     sw = swindustrycode()
#     return sw.convert(string)    

    
        
def market_by_code(c):
    """
    看这个：https://zhuanlan.zhihu.com/p/63064991
    
    股票代码是以数字、字母或其他符号来代表某只股票。每只股票都有自己的股票代码。
    我国不同股票代码的开头表示的含义主要有：
    （1）600或601开头的表示该股票为上海证券交易所上市的沪市A股；
    （2）900开头的表示该股票为上海证券交易所上市的沪市B股；
    （3）000开头的表示该股票为深圳证券交易所上市的深市A股；
    （4）200开头的表示该股票为深圳证券交易所上市的深市B股；
    （5）002开头的表示该股票为深圳证券交易所上市的中小板股票；
    （6）300开头的表示该股票为深圳证券交易所上市的创业板股票；
    （7）730开头的股票代码表示该股票为沪市新股申购，深市新股申购的代码与深市股票买卖代码相同。
    （8）股票配股代码沪市以700开头，深市以080开头。
    
    1、沪市主板：以600、601或603开头

    2、深市主板：以000、001、002、003开头
    
    3、创业板：以300开头，属于深交所
    
    4、科创板：以688开头，属于上交所
    
    5、北交所：以8开头
    
    6、新三板；以400、430、830开头
    
    """
    # if c[:3] == "688":
    #     return "科创板"
    # # elif c[:3] == "002":
    # #     return "中小板"#也属于大盘股
    # elif c[:3] in["300","301"]:
    #     return "创业板"
    # elif c[:2] in ['83', '43', '87']:
    #     return "北交所"
    # else:
    #     return "沪深大盘股"
    if c[:3] in ["000","001"]:
        return "深圳-A"
    if c[:3] in ["002","003","004"]:
        return "深圳-中小"
    if c[:3] in ["300"]:
        return "深圳-创业"
    if c[:2] in ["60"]:
        return "上海-A"
    if c[:2] in["68"]:
        return "上海-科创"
    else:
        return "other"
    
    
# class MarketInfo:
#     """
#     月度数据，好像是从东方财富手动下载的？
#     单位 亿元
#     """
#     def __init__(self, market = "shanghai"):
        
#         self.market = market
#         self.path0 = BASIC + '/other/market_info.xlsx'
#         excel0 = pd.read_excel(self.path0)
    
#         dates = excel0["数据日期"]
#         for i,d in enumerate(dates):
#             if type(d) == int:
#                 _d = np.datetime64('1900-01-01') + np.timedelta64(d, "D")
#                 dates[i] = pd.Timestamp(pd.Period(str(_d)[:4] + "-" + str(_d)[5:7]).end_time.date())
        
#         self.excel0 = excel0.set_index("数据日期")
    
    
#     def _get0(self, key, month):
#         if type(month) != pd.Timestamp:
#             month = pd.Timestamp(month)
#             # raise Exception()
#         if not(month in self.excel0.index):
#             return np.nan
        
        
#         key_col = \
#         {"shanghai_equity":0,
#          "shenzhen_equity":1,
#          "shanghai_value": 2,
#          "shenzhen_value": 3,
#          "shanghai_amount":4,
#          "shenzhen_amount":5,
#          "shanghai_volume":6,
#          "shenzhen_volume":7}
        
#         k = self.market + "_" + key

#         _ = self.excel0.loc[month][key_col[k]]
#         if _ == "-":
#             return np.nan
#         else:
#             return float(_)
    
#     def equity(self, month):
#         """
#         发行总股本
#         """
#         return self._get0("equity", month)
        
#     def value(self, month):
#         """
#         总市值
#         """
#         return self._get0("value", month)

#     def amount(self, month):
#         """
#         成交金额
#         """
#         return self._get0("amount", month)

#     def volume(self, month):
#         """
#         成交量
#         """
#         return self._get0("volume", month)

# market_info_sh = MarketInfo("shanghai")
# market_info_sz = MarketInfo("shenzhen")

# def getinfo(code):
#     """
#     from ak.stock_individual_info_em(symbol="000001")
#     """
#     _info = pd.read_csv(f"{BASIC}/stocksinfo/infos/{code}.csv", index_col=["item"])
   
#      #    item          value
#      #   总市值     11372184604.8
#      #   流通市值   2434641097.6
#      #   行业           软件开发
#      #  上市时间       20221028
#      #  股票代码         688152
#      #   股票简称            N麒麟
#      #   总股本     52844724.0
#      #   流通股     11313388.0
#     return _info
    


# class is_st:
#     """
#     A: 正常, 
#     B: ST, 
#     C: PT, 
#     D: *ST, 
#     T: 退市整理期, 
#     X: 退市
#     """
#     def __init__(self,):
#         spt = pd.read_excel(f"{BASIC}/stocksinfo/SPT_Trdchg.xlsx")
#         self.sptcode = np.array([fill0forstockcode(i) for i in spt["Stkcd"]])
#         sptdate = np.array(spt["Annoudt"])
#         self.spttype = np.array(spt["Chgtype"])
#         self.sdates = np.array(pd.to_datetime(sptdate))
#         self.comp_in_spt = list(set(self.sptcode))

#     def judge(self,code, date):
#         """
#         A:正常, B:ST, C:PT, D:*ST, T: 退市整理期, X:退市
#         ['BC', 
#           'DA', 
#           'AX', 
#           'DB', 
#           'CA', 
#           'AD', 
#           'SX', 
#           'AT', 
#           'BD', 
#           'CB', 
#           'BA', 
#           'BT', 
#           'AB', 
#           'TX', 
#           'DT']
#         """
#         date = pd.to_datetime(date)
#         _i = np.argwhere(self.sptcode == code).reshape(1,-1)[0]
#         stypes = self.spttype[_i]
#         dates = self.sdates[_i] 
#         if (code in stockcodes):
#             if not(code in self.comp_in_spt):
#                 return "A"
#             else:
#                 if date < dates[0]:
#                     return "A"
#                 for i,d in enumerate(dates):
#                     if d == date:
#                         return stypes[i][-1]
#                     if d > date:
#                         return stypes[i-1][-1]
#                 return stypes[-1][-1]
        
#         else:
#             raise Exception(f"{code} not in code list.")
        
# def comp_is_st(code, date): 
#     s = is_st()
#     return s.judge(code, date)


if __name__ =="__main__":
    # print(swindustries)
    # print(city["000002"])
    # dictionary["000002"]
    # print(comp_is_st(code = "000004",date = "2020-05-28"))
    # update_info()
    # dic = _gen_dictionary()
    # _gen_swindustry()
    # swname = swindustrycode()
    # print(swname.cdic)
    1