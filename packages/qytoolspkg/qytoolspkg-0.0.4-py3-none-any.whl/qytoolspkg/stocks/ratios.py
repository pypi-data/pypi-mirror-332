# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 09:56:23 2023

@author: win10
"""
from qytoolspkg.basictools.basicfunc import pdiv
from qytoolspkg.basictools.dbtools import create_connection
import pandas as pd
import datetime
import os
import numpy as np

def df_freq(freq):
    _fq = {"Y":"A-DEC",
           "Q":"Q-DEC"}
    if freq in _fq.keys():
        freq = _fq[freq]
    return freq

# exist_sheet = {sn : os.listdir(BASIC + f"/sheet_{sn}") for sn in ["lr","zcfz","xjll"]}

# def read_sheet(comp, sn):
    
#     if f"{comp}.csv" in exist_sheet[sn]:
#         df = pd.read_csv(f"{BASIC}/sheet_{sn}/{comp}.csv",
#                         parse_dates=["报告日"], 
#                         index_col=["报告日"])
#         df = df.sort_values(by=["报告日"])
#         df.index = df.index.rename("time")
#         return df
#     else:
#         df = pd.DataFrame(columns=["time"])
#         df = df.set_index("time")
#         return df

def read_sheet(db_config, comp, sn):
    # 修改数据库名称
    db_config['database'] = f"sheet_{sn}"
    
    # 创建数据库连接
    connection = create_connection(db_config)
    
    if connection:
        table_name = f"sc{comp}"
        try:
            # 从数据库读取数据
            query = f"SELECT * FROM `{table_name}`"
            df = pd.read_sql(query, connection)

            # 将 "报告日" 列设置为索引并重新命名
            if "报告日" in df.columns:
                df["报告日"] = pd.to_datetime(df["报告日"])  # 确保日期列是 datetime 类型
                df.set_index("报告日", inplace=True)
                df.index = df.index.rename("time")  # 重命名索引
                df.sort_index(inplace=True)  # 按时间排序
            
            return df
        except Exception as e:
            print(f"The error '{e}' occurred while reading from the database")
            return pd.DataFrame(columns=["time"])  # 出现错误时返回一个空 DataFrame
        finally:
            connection.close()  # 确保连接在最后关闭
    else:
        return pd.DataFrame(columns=["time"])  # 如果连接失败，返回一个空 DataFrame

def read_item(company, sheet, items, rename = None, freq="Y", pass_in_sheet = None):
    """
    rename: list or str
        if list, len(rename) = len(items)
    """
    if type(items) == str:
        items = [items]
    
    freq = df_freq(freq)
    company = str(company)
    if pass_in_sheet is None:
        df = read_sheet(company, sheet)
    else:
        df = pass_in_sheet[sheet]
    timerange = pd.date_range("1990",datetime.datetime.now(), freq = freq)
    _df = pd.DataFrame({"time":timerange,"_":range(len(timerange))})
    _df = _df.set_index("time")
    df = pd.merge(df, _df, how = "right", on = "time")
    # df = pd.concat([df, _df], axis = 1)
    df.index = df.index.rename("time")
    # print(df)
    if not(rename is None):
        if type(rename) == str:
            rename = [rename]
        dic = {items[i]:n for i,n in enumerate(rename)}
        for k in dic:
            if not (k in df.columns):
                df[k] = df.apply(lambda x: np.nan , axis = 1)
                print(f"{k} not in {company} {sheet}")
        df.rename(columns=dic,inplace=True)    
        return df[rename]
    else:
        return df[items]

def _comp(company):
    """

    Parameters
    ----------
    company : str or list
        list:[str, dict]

    """
    if type(company) == "str":
        return company, None
    else:
        return company[0], company[1]


def tax_shield(company, freq = "Y"):
    """
    累计折旧+待摊费用 / 资产总计
    """
    company, pass_in_sheet = _comp(company)#"长期待摊费用？？？？"
    df =  read_item(company, "zcfz", ["资产总计","累计折旧","待摊费用"], ["zc","zj","dtfy"], freq, pass_in_sheet)
    df["tax_shield"] = df.apply(lambda x: pdiv(x["dtfy"] + x["zj"],x["zc"]), axis = 1)
    return df[["tax_shield"]].dropna()

def tangible_asset_ratio(company, freq = "Y"):
    """
    有形资产占比
    有形净资产＝[[所有者权益]]－[[无形资产]]－[[递延资产]]
    return (总资产-"无形资产"-"递延所得税资产")/总资产
    """
    company, pass_in_sheet = _comp(company)
    df =  read_item(company, "zcfz", ["资产总计","无形资产","递延所得税资产"], ["zc","wx","dy"], freq, pass_in_sheet)
    df["tangible_asset_ratio"] = df.apply(lambda x: pdiv(x["zc"] - x["wx"] - x["dy"], x["zc"]), axis = 1)
    return df[["tangible_asset_ratio"]].dropna()

    
def roe(company, freq = "Y"):
    """
    Return on Equity
    净资产收益率 = 净利润 / 净资产  
                = 净利润/销售收入(Pricing Power) * 销售收入/总资产(Turnover rate) * 总资产/净资产(Leverage)
    
    freq = "Y" or "Q"
    
    about freq: ROE的分子是流量数据（来自利润表），而分母则是存量数据（来自资产负债表），
        一个季度的利润和一年的利润显然差别很大，但是第一季度末和年底的资产负债表并不会差3/4，
        所以一季度的ROE其实并不是年化的概念，值是偏小的，不能直接和年度的ROE来比较。
    """
    company, pass_in_sheet = _comp(company)
    freq = df_freq(freq)
    jlr = read_item(company, "lr", "净利润", "jlr", freq, pass_in_sheet)
    zcfz = read_item(company, "zcfz", ["资产总计","负债合计"], ["zc","fz"], freq, pass_in_sheet)
    df = pd.merge(jlr, zcfz, on = "time", how = "inner").dropna()
    df["roe"] = df.apply(lambda x: pdiv(x["jlr"] , x["zc"] - x["fz"]), axis = 1)
    return df[["roe"]].dropna()

def debt(company, freq = "Y"):
    company, pass_in_sheet = _comp(company)
    fz =  read_item(company, "zcfz", "负债合计", "debt", freq, pass_in_sheet)
    fz = fz.dropna()
    return fz

def assets(company, freq = "Y"):
    company, pass_in_sheet = _comp(company)
    fz =  read_item(company, "zcfz", "资产总计", "assets", freq, pass_in_sheet)
    fz = fz.dropna()
    return fz

def default_point(company, alpha = 0.5, freq = "Y"):
    """
    违约点DP
    DP = Ds流动负债 + alpha(default=0.5) * Dl非流动负债
    Returns
    -------
    dp: float
    """
    company, pass_in_sheet = _comp(company)
    df = read_item(company, "zcfz", ["流动负债合计", "非流动负债合计" ],["ds","dl"], freq, pass_in_sheet)    
    df['dp'] = df.apply(lambda x: x["ds"] + alpha * x["dl"], axis = 1)
    dp = df[["dp"]]
    dp = dp.dropna()
    return dp

def net_assets(company, freq = "Y"):
    company, pass_in_sheet = _comp(company)
    df = read_item(company, "zcfz", "所有者权益(或股东权益)合计", "net_assets", freq, pass_in_sheet)
    df = df.dropna()
    return df

def equity_parent(company, freq = "Y"):
    """
    Equity Attributable to Owners of the Parent 银行股
    """
    company, pass_in_sheet = _comp(company)
    df = read_item(company, "zcfz", "归属于母公司股东的权益", "equity_parent", freq, pass_in_sheet)
    df = df.dropna()
    return df


def current_debt_ratio(company, freq = "Y"):
    """
    流动负债比率
    """
    company, pass_in_sheet = _comp(company)
    df = read_item(company, "zcfz", ["流动负债合计","负债合计"], ["ldfz","fz"], freq, pass_in_sheet)    
    df["current_debt_ratio"] = df.apply(lambda x: pdiv(x["ldfz"],x["fz"]), axis = 1)    
    return df[["current_debt_ratio"]].dropna()

def cash_flows_operating_ratio(company,  freq = "Y"):
    """
    经营现金流量比率=经营现金流量净额÷流动负债
    """
    company, pass_in_sheet = _comp(company)
    xjl = read_item(company, "xjll", "经营活动产生的现金流量净额", "xjl", freq, pass_in_sheet)
    ldfz = read_item(company, "zcfz", "流动负债合计", "ldfz", freq, pass_in_sheet)    
    df = pd.merge(xjl, ldfz, on = "time", how = "inner").dropna()
    df["cash_flows_operating_ratio"] = df.apply(lambda x: pdiv(x["xjl"],x["ldfz"]), axis = 1)    
    return df[["cash_flows_operating_ratio"]].dropna()

def fcf1(company, freq = "Y"):
    company, pass_in_sheet = _comp(company)
    df = read_item(company, "xjll", ["经营活动产生的现金流量净额","投资活动产生的现金流量净额"],\
                   ["jy","tz"],freq, pass_in_sheet)
    df["fcf1"] = df.apply(lambda x : x["jy"] + x["tz"], axis = 1)
    return df[["fcf1"]].dropna()

def wcr(company, freq = "Y"):
    """
    营运资本比率 = 营运资本/ 总资产
    营运资本 = 流动资产 - 流动负债
    """
    company, pass_in_sheet = _comp(company)
    df = read_item(company, "zcfz", ["流动资产合计","流动负债合计","资产总计"], \
                   ["ldzc","ldfz","zc"], freq, pass_in_sheet)
    df["wcr"] = df.apply(lambda x: pdiv((x["ldzc"]-x["ldfz"]),\
                                        x["zc"]), axis = 1)
    return df[["wcr"]].dropna()


allratios = [roe, 
             debt, 
             assets,
             default_point,
             net_assets, 
             current_debt_ratio, 
             cash_flows_operating_ratio, 
             wcr,
             fcf1,
             tax_shield,
             tangible_asset_ratio,
             equity_parent]






if __name__ == "__main__":
    # _  = read_item("600606", "lr","五、净利润", "jlr","Y")
    # ri = read_item("601398", "zcfz", ["资产总计","负债合计"], ["zc","fz"], "Q")
    # _ = read_item("601398", "zcfz", ["流动负债合计", "非流动负债合计" ],["ds","dl"], "Y")
    # ri = assets_turnover("600606")
    # print(ri)
    1