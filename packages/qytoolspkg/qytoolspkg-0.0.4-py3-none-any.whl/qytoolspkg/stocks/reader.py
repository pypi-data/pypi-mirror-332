# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:03:14 2023

@author: lookingout
"""

import pandas as pd
import os
import numpy as np
from functools import wraps
from qytoolspkg.stocks.info import dictionary, swindustry, province, city
from qytoolspkg.basictools.dftools import merge_resample
from qytoolspkg.basictools.basicfunc import pdiv, remember
from qytoolspkg.stocks.ratios import allratios, read_sheet
from qytoolspkg.stocks.KMV import default_distance
from qytoolspkg.stocks.indicators import idio_logreturn, ncskew, duvol
from qytoolspkg.basictools.dbtools import create_connection, DatabaseError
# from warnings import RuntimeWarning

from qytoolspkg.consts import DB_CONFIG


class LowFreqMarketTrading:
    def __init__(self):
        
        self.name = None
        self.csv:pd.DataFrame = None
        self.DB_CONFIG = DB_CONFIG
        self.csv_table = None
        self.csv_dbname = None
        
    def __str__(self,):
        return self.name


    @property  
    def start(self):
        return self.csv.index[0] if self.csv is not None else None
    
    @property
    def end(self):
        return self.csv.index[-1] if self.csv is not None else None
    
    def _load_data(self, DB_NAME, TABLE_NAME, fillnan = None):
        try:
            connection = create_connection(self.DB_CONFIG)    
            connection.database = DB_NAME
            query = f"SELECT * FROM {TABLE_NAME}"  # 请替换为您的实际查询
            df = pd.read_sql(query, connection)
            return df            
        except DatabaseError as err:
            if err.errno == 1146: 
                return fillnan
            else:
                raise 
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    def load_csv(self):
        if not (self.csv is None):
            return
        
        df = self._load_data(self.csv_dbname, self.csv_table, None)
        if df is None:
            self.csv = pd.DataFrame(columns=["daily_close", "daily_high", "daily_volume", 
                                             "daily_low", "daily_open"])
            self.csv.index.name = 'time'
            return
        else:
            df.rename(columns=self._attr_csv, inplace=True)
            # print(df)
            df["time"] = pd.to_datetime(df["time"])
            df = df.set_index("time")
            self.csv = df
            return

    @remember
    def logreturn_(self):
        """
        记住全部默认参数的logreturn
        """
        return self.logreturn()
    
    def logreturn(self, freq="D", cut_last=True):
        self.load_csv() 
        close = self.close()
        ts = close.resample(freq).last().dropna()
        ts = ts.apply(np.log).diff().dropna() * 100
        _r = self._construct(ts, "logreturn", freq, cut_last)
        return _r

        
    def return_(self, freq = "D", cut_last = True):
        close = self.close()
        ts = close.resample(freq).last().dropna()
        ts = ts.pct_change().dropna() * 100
        _r = self._construct(ts,"return", freq, cut_last) 
        return _r
            
    def volatility(self, engine = "roll", cut_last = True, **kwds):
        """
        engine = roll/ resample/ parkinson
            roll window=200
            resample freq = M
            roll滚动窗口法估计波动率，需传入参数
            window默认为 200
        ...

        """
        if engine == "roll":
            freq = "D"
            if ("window" in kwds):
                window = kwds["window"]
            else:
                window = 200
            vola = self.logreturn(freq).rolling(window=window).std()
        elif engine =="resample":
            if ("freq" in kwds):
                freq = kwds["freq"]
            else:
                freq = "Y"
            vola = self.logreturn().resample(freq).std()
        elif engine == "parkinson":
            # Diebold, Francis X., and Kamil Yilmaz. 
            # “Better to Give than to Receive: Predictive Directional Measurement of Volatility Spillovers.”
            # International Journal of Forecasting 28, no. 1 (January 2012): 57–66. 
            # https://doi.org/10.1016/j.ijforecast.2011.02.006.
            # estimate of the annualized daily percent standard deviation (volatility)
            freq = "D"
            def _f(x):
                s2 = 0.361 * (np.log(x["high"])-np.log(x["low"])) ** 2
                return 100 * np.sqrt(365 * s2)
                
            high = self.high()
            low = self.low()
            df = pd.concat([high, low], axis = 1)
            df["vola"] = df.apply(_f, axis = 1)
            vola = df[["vola"]]
            
        else:
            raise NotImplementedError()
        
        _r = self._construct(vola, "volatility", freq, cut_last)
        return _r
    
    # def _attr_csv_get(self, key):
    #     if key in self._attr_csv:
    #         name = self._attr_csv[key]
    #     else:
    #         raise Exception(key + f"is not in {self.path}")
    #     return name
    
    def close(self, freq = "D",  cut_last = True):
        self.load_csv() 
        key = "daily_close"
        # name  = self._attr_csv_get(key)
        ts = self.csv[[key]]
        ts = ts.resample(freq).last().dropna()
        ts = self._construct(ts,"close", freq, cut_last)
        return ts
    
    def open_(self, freq = "D", cut_last = True):
        self.load_csv() 
        key = "daily_open"
        # name  = self._attr_csv_get(key)
        ts = self.csv[[key]]
        ts = ts.resample(freq).first().dropna()
        ts = self._construct(ts,"open", freq, cut_last)
        return ts
    
    def high(self, freq = "D", cut_last = True):
        self.load_csv() 
        key = "daily_high"
        # name  = self._attr_csv_get(key)
        ts = self.csv[[key]]
        ts = ts.resample(freq).max().dropna()
        ts = self._construct(ts,"high", freq, cut_last)
        return ts
    
    def low(self, freq = "D", cut_last = True):
        self.load_csv() 
        key = "daily_low"
        # name  = self._attr_csv_get(key)
        ts = self.csv[[key]]
        ts = ts.resample(freq).min().dropna()
        ts = self._construct(ts,"low", freq, cut_last)
        return ts
    
    def volume(self, freq = "D", cut_last = True):
        self.load_csv() 
        key = "daily_volume"
        # name  = self._attr_csv_get(key)
        ts = self.csv[[key]]
        ts = ts.resample(freq).mean().dropna()
        ts = self._construct(ts,"volume", freq, cut_last)
        return ts
    
    def _construct(self,  ts, label, freq, cut_last) -> pd.DataFrame:

        if type(ts) == pd.DataFrame:
            ts = ts.dropna()
            ts.columns = [label]
            df = ts.copy()
        else:
            ts = np.array(ts)
            df = pd.DataFrame({label :ts})
            df.index = self.csv.index
            df = df.dropna()
            # if start is None:
            #     return df
            
            # elif end is None:
            #     start = pd.to_datetime(start)
            #     if start in df.index:
            #         return df.loc[start][label]
            #     else:
            #         return np.nan
            
            # else:
            #     end =  pd.to_datetime(end)
            #     return df[start:end]
            
        df = df.sort_index()    
        if (freq != "D") and cut_last and(len(ts) > 0):
            #最后一个周期的通常数据不全
            last_index = df.iloc[-1].name
            df = ts.drop(last_index)
        return df
    
    def _outter(self, params_attr, func, prepare = None):
        def _inner(*kwd):
            if not(prepare is None):
                prepare()
            _attr = "_" + func.__name__
            if not(_attr in self.__dict__):
                _res = func(getattr(self,params_attr), *kwd)
                # print("set", _attr)
                setattr(self, _attr, _res)
            return getattr(self, _attr)
        _inner.__doc__ = func.__doc__
        return _inner


# index_path_prefix =  f"{BASIC}/index_ts/"
# index_file_path = {i[:8]:index_path_prefix+i for i in os.listdir(index_path_prefix)}

class index(LowFreqMarketTrading):
    def __init__(self,code):
        super().__init__()
        self.code = code
        # self.path = index_file_path[code]
        # self.csv =  pd.read_csv(self.path, parse_dates=["date"], index_col="date")
        # self.csv.index.name = "time"    
        self._attr_csv = {
            "date": "time",
            "close": "daily_close",
            "high": "daily_high",
            "volume": "daily_volume",
            "low": "daily_low",
            "open": "daily_open"
        }
        self.csv_table = self.code
        self.csv_dbname = "indexes"
    

    
shanghai  = index("sh000001")
shenzhen = index("sz399001")

# swlv1_path_prefix =  f"{BASIC}/swlv1/ts/"

class swlv1(LowFreqMarketTrading):
    def __init__(self,code):
        super().__init__()

        self.code = code
        # self.path = swlv1_path_prefix + code + ".csv"
        # csv =  pd.read_csv(self.path)
        # csv["time"] = pd.to_datetime(csv["发布日期"])
        # self.csv = csv.set_index("time")
        self._attr_csv = {
            "发布日期": "time",
            "收盘指数": "daily_close",
            "最高指数": "daily_high",
            "成交量": "daily_volume",
            "最低指数": "daily_low",
            "开盘指数": "daily_open"
        }
        self.csv_table = "sw" + str(self.code)
        self.csv_dbname = "swlv1"

    
#默认使用后复权数据
# stock_path_prefix =  f"{BASIC}/allstocks_hfq/"
# stock_file_path = {i[:6]:stock_path_prefix+i for i in os.listdir(stock_path_prefix)}
_ratios = allratios



    
    
    
class stock(LowFreqMarketTrading):

    def __init__(self,code):
        """
        股价： ak.stock_zh_a_hist 
        https://quote.eastmoney.com/concept/sh603777.html?from=classic
            
        报表： ak.stock_financial_report_sina
        https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600600/displaytype/4.phtml?source=fzb&qq-pf-to=pcqq.group
            
        指标： ak.stock_financial_abstract
        https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600004.phtml
        """
        
        self.code = code
        # csv_cols=["日期", "开盘", "收盘", "最高", "最低", "成交量", 
        #           "成交额", "振幅", "涨跌幅", "涨跌额", "换手率"]
        # if self.code in stock_file_path:
        #     self.path =stock_file_path[self.code]
        #     csv =  pd.read_csv(self.path)
        #     csv["time"] = pd.to_datetime(csv["日期"])
        #     self.csv = csv.set_index("time") 
        # else:
        #     self.path = None
        #     csv = pd.DataFrame(columns= csv_cols)
        #     csv["time"] = pd.to_datetime(csv["日期"])
        #     self.csv = csv.set_index("time") 
        super().__init__()

        self._attr_csv = {
            "日期": "time",
            "收盘": "daily_close",
            "最高": "daily_high",
            "成交量": "daily_volume",
            "最低": "daily_low",
            "开盘": "daily_open"
        }

        self.sheets = None
        self.csv_table = "sc" + str(self.code)
        self.csv_dbname = "stocks_hfq"
        
        if self.code in swindustry:
            self.industry_swlv1 = swindustry[self.code]
            self.province = province[self.code]
            self.city = city[self.code]
        else:
            self.industry_swlv1 = np.nan
            self.province = np.nan
            self.city = np.nan
            
        self._tup = (self.code, self.sheets)
        for rts in _ratios:
            setattr(self, rts.__name__, self._outter("_tup", rts, self._get_sheets))
            # setattr(self, rts.__name__, rts(self.code))
    

    
    def _get_sheets(self):
        if self.sheets is None:    
            self.sheets = {sn: read_sheet(self.code, sn) for sn in ["lr","zcfz","xjll"]}
            return
        else:
            return

    # @remember
    # def industry_csrc(self):
    #     """
    #     see
    #         DataBase\projects\dft1018\data_pre.py: _csrc_industry()
    #     """
    #     # path = f"{BASIC}/stocksinfo/industry/csrc/{self.code}.csv"


    #     _r  = pd.read_csv(path, parse_dates=["time"], index_col=["time"])

    #     return _r
    
    # @remember
    # def financing_constraints(self):
    #     pth = PROCESS + f"/financing_constrains/{self.code}/"
    #     if not os.path.exists(pth):
    #         pth = PROCESS + "/financing_constrains/nan/"
    #     files_path = os.listdir(pth)
    #     files = [pd.read_csv(pth + f, index_col="Enddate", \
    #                          parse_dates=["Enddate"]) for f in files_path]
    #     df =  pd.concat(files, axis  = 1,join  = "outer")
    #     df.columns = [f[:-4] for f in files_path]
    #     return df
        
#     def abstract(self, 
#                  col, 
#                  freq = "Y", 
#                  dropna = True):
# # 归母净利润 营业总收入 营业成本 净利润 扣非净利润 股东权益合计(净资产) 商誉 经营现金流量净额 基本每股收益
# # 每股净资产 每股现金流 净资产收益率(ROE) 总资产报酬率(ROA) 毛利率 销售净利率 期间费用率 资产负债率 基本每股收益
# # 稀释每股收益 摊薄每股净资产_期末股数 调整每股净资产_期末股数 每股净资产_最新股数 每股经营现金流 每股现金流量净额 
# # 每股企业自由现金流量 每股股东自由现金流量 每股未分配利润 每股资本公积金 每股盈余公积金 每股留存收益 每股营业收入
# # 每股营业总收入 每股息税前利润 净资产收益率(ROE) 摊薄净资产收益率 净资产收益率_平均 净资产收益率_平均_扣除非经常损益
# # 摊薄净资产收益率_扣除非经常损益 息税前利润率 总资产报酬率 总资本回报率 投入资本回报率 息前税后总资产报酬率_平均
# # 毛利率 销售净利率 成本费用利润率 营业利润率 总资产净利率_平均 总资产净利率_平均(含少数股东损益) 归母净利润
# # 营业总收入 净利润 扣非净利润 营业总收入增长率 归属母公司净利润增长率 经营活动净现金/销售收入 经营性现金净流量/营业总收入
# # 成本费用率 期间费用率 销售成本率 经营活动净现金/归属母公司的净利润 所得税/利润总额 流动比率 速动比率 保守速动比率
# # 资产负债率 权益乘数 权益乘数(含少数股权的净资产) 产权比率 现金比率 应收账款周转率 应收账款周转天数 存货周转率 
# # 存货周转天数 总资产周转率 总资产周转天数 流动资产周转率 流动资产周转天数 应付账款周转率
#         if type(col) == str:
#             col = [col]
#         if not("_abstract" in self.__dict__):
#             df = pd.read_excel(f"{BASIC}/indicators/abstract/{self.code}.xlsx")
#             df = df.drop("选项", axis = 1)
#             df = df.drop_duplicates(["指标"])
#             df = df.set_index("指标")
#             df = df.T
#             df.index.name = "time"
#             df.index = pd.to_datetime(df.index)
#             df = df.sort_index()
#             self._abstract = df
#         col = self._abstract[col]
#         col = merge_resample(col, freq=freq, dropna=dropna)
#         return col
    
    def change_in_day(self):
        ts = self.csv["涨跌幅"]
        _r = self._construct(ts, "change_in_day","D",True)
        return _r
    
    def turnover(self):
        """
        有的股票换手率一直是0，应该是没有记录
        """
        ts = np.array(self.csv["换手率"])/100
        _r = self._construct(ts, "tov","D",True)
        return _r
    
    def amount(self):
        ts = self.csv["成交额"]
        _r = self._construct(ts, "amt","D",True)
        return _r
    
    @remember
    def intraday_return(self):
        op = self.open_()
        cl = self.close()
        df = pd.concat([op, cl], join = "inner", axis =1)
        df["intraday_return"] = df.apply(lambda x:pdiv(x["close"] - x["open"],x["open"]), axis = 1)
        return df[["intraday_return"]]
    
    def amp(self):
        """
        振幅
        不知道是怎么算出来的，
        好像是 (最高-最低)/开盘
        又差了一点点，反正也大差不差，直接用了。
        """
        ts = self.csv["振幅"]
        _r = self._construct(ts, "amp","D",True)
        return _r
    
    @remember
    def mamp(self):
        """
        modified amp
        计算liq时考虑到涨跌停时日内振幅为0，(实际流动性很差)，因此不直接使用amp
        分三种情况
        close_1 前一日收盘价， high 今最高价， low 今最低价
        1 low < close_1 < high, AMP = high - low
        2 close_1 > high, AMP = close_1-low
        3 close_1 < low,  AMP = high - close_1
        """
        def _f(x):
            h = max(x["close_1"], x["high"])
            l = min(x["close_1"], x["low"])
            r =  pdiv((h - l), x["close"])
            return r
        df = self.csv[["收盘","最高","最低"]].copy()
        df.columns = ["close", "high", "low"]
        df["close_1"] = df["close"].shift(1)
        df["mamp"] = df.apply(_f,axis = 1)
        df = df.dropna()
        return df[["mamp"]]
    
    @remember 
    def illiq(self):
        """
        Amihud 流动性指数，日度。需对样本区间取平均。成交金额单位： 百万元
        """
        VOLD = self.amount().copy() / 1000000
        abs_R = self.logreturn().copy().apply(abs, axis = 0)
        df = pd.merge(VOLD, abs_R, how = "inner", on = "time")
        df["_illiq"] = (df["logreturn"]/df["amt"])
        return df[["_illiq"]]

    @remember
    def liq(self):
        CHANGE = self.turnover().copy()
        AMP = self.mamp().copy()
        df = pd.merge(CHANGE, AMP, how = "inner", on = "time")
        df["_liq"] = (df["tov"]/df["mamp"])
        return df[["_liq"]]

    # def illiq(self, freq = "Y"):
    #     _df = self._illiq().resample(freq).mean()
    #     _df = self._construct(_df, "illiq", freq, True)
    #     return _df
    
    # def liq(self, freq = "Y"):
    #     _df = self._liq().resample(freq).mean()
    #     _df = self._construct(_df, "liq", freq, True)
    #     return _df
    
    # def share(self, nature = "total", freq = "Y"):
    #     """
    #     nature = 
    #             total: 总股权
    #             outstanding: 流动
    #             nontradable: 非流动
                
    #     see
    #         DataBase\projects\dft1018\data_pre.py: 19-50
    #         # 从stock_share里的csv文件读取, time需要移到12-31日
    #     """
    #     assert(freq == "Y")
    #     attr = f"{nature}_share"
    #     path = f"{BASIC}/stock_share/by_stock/{attr}/{self.code}.csv"

    #     if not(attr in self.__dict__):
    #         _r  = pd.read_csv(path, parse_dates=["time"], index_col=["time"])
    #         setattr(self, attr, _r)
    #     return getattr(self, attr)
    
    # def is_finance_company(self, year = None):
    #     """
    #     year : int 2014
    #     """
    #     if year is None:
    #         ind = self.industry_csrc()["csrc_industry"].unique()
    #         if len(ind) == 0:
    #             return np.nan
    #         else:
    #             return ("金融、保险业" in ind) or ("金融业" in ind)
    #     else:
    #         # year = pd.to_datetime(year).year
    #         ind = self.industry_csrc().loc[str(year):str(year)]["csrc_industry"]
    #         if len(ind) == 0: 
    #             return np.nan
    #         else:
    #             ind = ind.loc[0]["csrc_industry"]
    #             return (ind == "金融业") or (ind == "金融、保险业")
    
    # @remember
    # def market_value(self):
    #     """
    #     单位：元
    #     """
    #     freq = "Y"
    #     amt = self.amount().copy().resample(freq).last()
    #     tov = self.turnover().copy().resample(freq).last()
    #     # close = self.close(freq = freq)
    #     # close.columns = ["p"]#这么算不行，得用不复权的close   
    #     vol = self.volume().copy().resample(freq).last()
    #     p = pd.concat([amt,vol], axis = 1)
    #     # print(p)
    #     p["p"] = p.apply(lambda x: (x["amt"] / x["volume"]) / 100, axis = 1) 
    #     #成交额 = 成交量 * 100（1手有100股） * 股价
    #     p = p[["p"]]
    #     ots = self.share("outstanding").copy()
    #     ots.columns = ["os"]   
        
    #     ns = self.share("nontradable").copy()
    #     ns.columns = ["ns"]
    #     ts = self.share("total")
    #     ts.columns = ["ts"]
        
    #     if self.is_finance_company():
    #         na = self.equity_parent().copy()
    #     else:
    #         na = self.net_assets().copy()

    #     na.columns = ["na"]
    #     mv = pd.concat([ns,ts,na, ots,p], axis = 1)
    #     # mv = pd.concat([ns,ts,na,amt, tov], axis = 1)

    #     mv["mvn"] = mv.apply(lambda x: x["ns"] * (x["na"]/ x["ts"]), axis = 1)
    #     mv["mvo"] = mv.apply(lambda x: x["p"] * x["os"], axis = 1)
    #     # mv["mvo"] = mv.apply(lambda x: pdiv(x["amt"], x["tov"]), axis = 1)#tov应该也是百分制的
    #     mv = mv.dropna()
    #     mv["mv"] = mv.apply(lambda x: x["mvo"] + x["mvn"], axis = 1)
    #     return mv[["mvo","mvn","mv"]]
        
        
    # def default_distance(self,
    #                      alpha = 0.5,
    #                      rf = None,
    #                      freq = "Y",
    #                      rft = 1):
    #     """
    #     Parameters
    #     alpha : 长期负债和短期负债权重 DP = Ds流动负债 + alpha(default=0.5) * Dl非流动负债
    #     rf: 10年期国债收益率
    #     freq 只能为Y
    #     rft:到期时间,默认为1年
    #     """
    #     assert(freq == "Y")

    #     if rf is None:
    #         rf = cbonds().get() / 100   
    #     rf = rf.resample(freq).mean()
    #     mv = pd.merge(s.amount(),s.turnover(), on = "date", how = "inner")
    #     mv["mv"] = mv.apply(lambda x : x['amt'] / x['tov'], axis = 1)
    #     mv = mv[["mv"]].resample(freq).mean()
        
    #     rt = s.logreturn()/100
    #     volatility = rt.rolling(window=252).std()   
    #     volatility = volatility.resample(freq).last()
    #     debt= s.debt(freq)
    #     dp = s.default_point(0.5, freq)     
    #     df = default_distance(volatility, mv, rf, debt, dp, previous_x0=False)
    #     return df
    
    # def idio_logreturn(self,
    #                    market = "shanghai",
    #                    adv:int = 2,
    #                    lag:int = 2,
    #                    freq = "D",
    #                    to_read = True,
    #                    to_save = True):
    #     """
    #     market = swindustry / shanghai
    #     adv: 未来的期数
    #     lag: 之前的期数
    #     """ 
    #     path = PROCESS + "/stock/idio_return/"
    #     file = f"{self.code}m{market}adv{adv}lag{lag}freq{freq}.csv"
    #     if to_read and (file in os.listdir(path)):    
    #         return pd.read_csv(path+file, index_col="time", parse_dates=["time"])
                
    #     if market == "swindustry":
    #         ind = swindustry[self.code]
    #         market = swlv1(ind)
    #     elif market == "shanghai":
    #         market = shanghai
    #     elif market == "shenzhen":
    #         market = shenzhen
    #     else:
    #         raise NotImplementedError()

    #     _r = self.logreturn(freq).copy()
    #     _m = market.logreturn(freq).copy()          
        
    #     if len(set(_r.index) & set(_m.index)) < 3 + adv + lag:
    #         raise RuntimeWarning(f"{self.code} is too short to estimate idio logreturn.")
    #         _r = _r* np.nan
    #         _r.columns = ["idio_logreturn"]
    #         return _r
        
    #     r = idio_logreturn(_r,
    #                        _m,
    #                        adv,
    #                        lag)
    #     r = r.dropna()
    #     if to_save:
    #         r.to_csv(path+file)
    #     return r
    
    
    
    
    

        
if __name__ == "__main__":
    s = stock("000001")
    
    # s.total_share()
    # s.volatility(window = 100).plot()
    # _ = s.mamp()
    # _ = s.illiq("M")["2014-05":"2022-10"]
    # _.plot()
    # print(s.roe())
    # a = s.amp
    # a = s.logreturn("20220101","20230101")
    # print(a)
    # b = s.amp("2022-01-01","2023-01-01")
    # print(b)
    # print(pd.merge(a,b,on = 'date'))
    # a.plot()
    # sh = index("shanghai")
    # a = shanghai.logreturn()
    # print(a)
    # a = swlv1("801710")
    # a.logreturn().plot()
    # from tqdm import tqdm 
    # for s in tqdm(list(dictionary.keys())):
    #     try:
    #         stock(s).idio_logreturn()
    #     except:
    #         print(s)
        
    