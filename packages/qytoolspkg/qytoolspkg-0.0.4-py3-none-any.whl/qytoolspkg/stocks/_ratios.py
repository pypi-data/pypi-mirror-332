# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:50:50 2022

@author: lookingout
"""
#read xlsx for the sheets
import sys
import pandas
import numpy as np
from wcode.path import BASIC
from wcode.consts import my_date_format
"""
ratios所有time变量均可用abcd代指季度报表日期

所有涉及增长率的指标目前只算年度
因为前后两个季度是累计关系

time format: "2019a" or 20190301, see _period().
"""

# class ignore:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         # print("[DEBUG]: enter {}()".format(self.func.__name__))
#         try: 
#             return self.func(*args, **kwargs)
#         except Exception as e:
#             return np.nan

def check_denominator(x):
    if -0.0001<x<0.0001:
        return np.nan
    else:
        return x


def _period(time):
    """
    2019Q1 -> 20190331
    """
    q = pandas.to_datetime(time).to_period("Q")
    t = q.end_time.strftime(my_date_format)
    return t 

def read_item(company, sheet, item, time):
    
    company = str(company)
    time = _period(time)    
    d = pandas.read_csv(f"{BASIC}/sheet_{sheet}/{company}.csv")

    # print(d["报表日期"][0])
    d = d.set_index("报表日期")
    
    try:
        _ = d[item][int(time)]
    except KeyError:
        return np.nan
    # print(_)
    try:
        float(_)
    except Exception as e:
        if str(e) == "cannot convert the series to <class 'float'>":
            _  = np.array(_)[0]
        else:
            print(e)
            print(_, type(_), company, sheet, item, time)
            sys.exit()
    return float(_)

def shift_period(time, shift):
    _a = {"a":0,"b":1,"c":2,"d":3}
    _b = {list(_a.values())[i]:_aa for i,_aa in enumerate(_a)}
    year = int(time[:4])
    s_y = np.floor((shift + _a[time[-1]]) / 4)
    # print(s_y)
    s_p = (shift + _a[time[-1]]) % 4
    if s_p<0:
        s_p = 4 + s_p
    return str(int(year + s_y)) + _b[s_p]
    

    
    
def roe(company, time):
    """
    Return on Equity
    净资产收益率 = 净利润 / 净资产  
                = 净利润/销售收入(Pricing Power) * 销售收入/总资产(Turnover rate) * 总资产/净资产(Leverage)
    """
    # time = _period(time)
    jlr = read_item(company, "lr", "五、净利润", time)
    zc = read_item(company, "zcfz", "资产总计", time)
    fz = read_item(company, "zcfz", "负债合计", time)   
    de = check_denominator(zc - fz)
    return jlr / de

def net_profit_operating_income(company, time):
    # net_profit_margin_on_operating_income
    # pop pricing power
    jlr = read_item(company, "lr", "五、净利润", time)
    yysr = read_item(company, "lr", "一、营业总收入", time)
    de = check_denominator(yysr)

    return jlr/de


def turnover_current(company, time):
    """
    流动资产周转率 = 主营业务收入净额/平均流动资产总额
    """
    yysr = read_item(company, "lr", "一、营业总收入", time)
    zc = read_item(company, "zcfz", "资产总计", time)
    zc_q = read_item(company, "zcfz", "资产总计", shift_period(time,-4))#季度增长还是年度？
    de = check_denominator(zc -zc_q)
    return yysr/de


def asset_liability(company, time):
    zc = read_item(company, "zcfz", "资产总计", time)
    fz = read_item(company, "zcfz", "负债合计", time)  
    de = check_denominator(zc -fz)
    return zc / de

def net_asset(company, time):
    """
    Net Asset Growth Rate
    净资产增长率 = (期末净资产—期初净资产)/期初净资产
    """
    # time = _period(time)
    zc = read_item(company, "zcfz", "资产总计", time)
    fz = read_item(company, "zcfz", "负债合计", time)    
    jzc = zc - fz

    return jzc
    
def cash_flows_operating_ratio(company, time):
    """
    经营现金流量比率=经营现金流量净额÷流动负债
    """
    xjl = read_item(company, "xjll", "经营活动产生现金流量净额", time)
    ldfz = read_item(company, "zcfz", "流动负债合计", time)    
    de = check_denominator(ldfz)
    return xjl / de
    
def ebit(company, time):
    """
    Earnings before interest and taxes
    近似 ： 息税前利润（EBTI）=净利润+财务费用+所得税费用
    """
    jlr = read_item(company, "lr", "五、净利润", time)
    cwfy = read_item(company, "lr", "财务费用", time)#花出去的费用，可以为负，意为利息收入
    sds = read_item(company, "lr", "减：所得税费用", time)#交出去的税
    return jlr + cwfy + sds
    
    
def ebitda(company, time):
    """
    税息折旧及摊销前利润 EBITDA = 息税前利润（EBIT）+折旧费用+摊销费用 
    """
    et = ebit(company, time)
    zj = read_item(company, "xjll", "固定资产折旧、油气资产折耗、生产性物资折旧", time)
    wxzc_tx = read_item(company, "xjll", "无形资产摊销", time)
    cqdt_tx = read_item(company, "xjll", "长期待摊费用摊销", time)
    return et + zj + wxzc_tx + cqdt_tx


def roic(company, time):
    """
    投入资本回报率 
    = NOPAT  /投资资本,  NOPAT = 税后净营业收益=营业利润 * (1-税率)
    近似 = EBIT / (所有者权益 + 非流动负债)
    """
    equity = read_item(company, "zcfz", "所有者权益(或股东权益)合计", time)
    # xj = read_item(company, "zcfz", "货币资金", time)
    fldfz = read_item(company, "zcfz", "非流动负债合计", time)    
    et = ebit(company, time)
    de = check_denominator(equity + fldfz)
    return et / de

def quick_ratio(company, time):
    """
    速动资产=流动资产-存货-预付款项-待摊费用
    速动资产/ 流动负债
    """
    ldfz = read_item(company, "zcfz", "流动负债合计", time)    
    ldzc =  read_item(company, "zcfz", "流动资产合计", time)
    ch =  read_item(company, "zcfz", "存货", time)
    yfkx = read_item(company, "zcfz", "预付款项", time)
    dtfy = read_item(company, "zcfz", "待摊费用", time)
    quick = ldzc - ch - yfkx -dtfy
    de  = check_denominator(ldfz)
    
    return quick / de

def real_ratio(company, time):
    """
    liquidity_ratio
    流动比率 = 流动资产/流动负债
    """
    ldzc = read_item(company, "zcfz", "流动资产合计", time)
    ldfz = read_item(company, "zcfz", "流动负债合计", time)    
    de  = check_denominator(ldfz)
    return ldzc /de
def working_captial(company, time):
    """
    营运资本 = 流动资产 - 流动负债
    """
    ldzc = read_item(company, "zcfz", "流动资产合计", time)
    ldfz = read_item(company, "zcfz", "流动负债合计", time)    
    return ldzc - ldfz

def wcr(company, time):
    """
    营运资本比率 = 营运资本/ 总资产
    """
    wc = working_captial(company, time)
    zc = read_item(company, "zcfz", "资产总计", time)
    de = check_denominator(zc)
    return wc/de
    
def current_debt_ratio(company, time):
    """
    流动负债比率
    """
    ldfz = read_item(company, "zcfz", "流动负债合计", time)    
    fz = read_item(company, "zcfz", "负债合计", time) 
    de  = check_denominator(fz)

    return ldfz/ de

def cash_debt_ratio(company, time):
    """
    现金流动负债比率
    """
    xj = read_item(company, "zcfz", "货币资金", time)
    ldfz = read_item(company, "zcfz", "流动负债合计", time)    
    de  = check_denominator(ldfz)

    return xj / de


def turnover_total(company, time):
    "资产周转率turnover rate = 营业总收入/平均资产总计"
    yysr = read_item(company, "lr", "一、营业总收入", time)
    zc = read_item(company, "zcfz", "资产总计", time)
    zc_q = read_item(company, "zcfz", "资产总计", shift_period(time,-4))#季度增长还是年度？
    de = check_denominator(zc - zc_q)
    return yysr/de

def roa(company, time):
    """
    return on assets
    资产净利润率 = 净利润 / （期初总资产 + 期末总资产）/2
    # period : "y"年度
    #          "s"季度
    """    
        
    jlr = read_item(company, "lr", "五、净利润", time)
    zc = read_item(company, "zcfz", "资产总计", time)

    zc_q = read_item(company, "zcfz", "资产总计", shift_period(time,-4))#季度增长还是年度？
    de= check_denominator((zc + zc_q)/2)
    return jlr / de


def fcf1(company, time):
    jyxjl = read_item(company, "xjll", "经营活动产生现金流量净额", time)
    tzxjl = read_item(company, "xjll", "投资活动产生的现金流量净额", time)
    return jyxjl + tzxjl


def asset(company, time): 
    zc = read_item(company, "zcfz", "资产总计", time)
    return zc

def debt(company, time): 
    fz = read_item(company, "zcfz", "负债合计", time)
    return fz

def current_asset(company, time):
    ldzc = read_item(company, "zcfz", "流动资产合计", time)
    return ldzc

def current_debt(company, time):
    ldfz = read_item(company, "zcfz", "流动负债合计", time)
    return ldfz


def total_operating_income(company, time):
    yysr = read_item(company, "lr", "一、营业总收入", time)
    return yysr

def net_profit(company, time):
    jlr = read_item(company, "lr", "五、净利润", time)
    return jlr

def operating_profit(company, time):
    yylr = read_item(company, "lr", "三、营业利润", time)
    return yylr


def net_cash_flow(company, time):
    """"_from_operating_activities"""
    xjl = read_item(company, "xjll", "经营活动产生现金流量净额", time)
    return xjl


class growth:
    """
    生成财务指标的年度增长率
    self.__name__ = r.__name__ + "_ag"
    """
    def __init__(self, r):
        self.r = r
        self.__name__ = r.__name__ + "_ag"

    def __call__(self, company, time):   
        _time = shift_period(time,-4)
        a = self.r(company, time)
        b = self.r(company, _time)
        b = check_denominator(b)
        return (a-b)/b
    
def annual(func):
    """
    年度时间序列
    """
    def _wrapper(company, time = None, plot = False):
        if time is None:
            years = pandas.date_range("1990","2021",freq="Y")
            ts = np.array([func(company, str(y)) for y in years])
            if plot:
                import matplotlib.pyplot as plt
                fig =  plt.figure(figsize=(14,6))
                ax =  fig.add_subplot(111)
                label =company + ": " + func.__name__
                ax.plot(ts, "-s", color = "black", label = label)
                tks=np.array(range(len(years)))[:]
                ax.set_xticks(tks)
                ax.set_xlim(0,len(years))
                ax.set_xticklabels(years[tks],rotation=50)
                ax.legend(fontsize = 20,shadow = False,frameon=False)
                ax.tick_params(labelsize=20)
                plt.show()
        else:
            return func(company, time)
    return _wrapper


if __name__ == "__main__":
    # a = read_item("000006", "zcfz", "流动负债合计", "2022c")
    # print(a)
    # a = pandas.DataFrame({"x":[1,2,3],"y":[4,5,6]})
    # a = a.set_index("x")
    # print(roe("000006","20220930"))
    # print(jzc_zzl("000006","2022a"))
    # print(shift_period("2022a", 4))
    # print(a["y"][1])
    # samples()
    # ratio_ts("600136")
    # annual_ratios("000006" , quick_ratio, plot  = True)
    # roe_g = growth(roe)
    # print(roe_g("000006","2021d"), roe_g.__name__)
    # print(roe("000006","2021d"))
    # print(roe("000006","2020d"))
    print(roe.__doc__)