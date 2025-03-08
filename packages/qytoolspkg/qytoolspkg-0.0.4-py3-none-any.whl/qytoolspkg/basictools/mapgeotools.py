# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:27:57 2023

@author: win10
"""

import json
import requests
from urllib.request import urlopen
from urllib.parse import quote
import numpy as np
from qytoolspkg.basictools._china_cities_coordinate import coordinate, provinces, provinces_mainland
from geopy.point import Point
from geopy.distance import geodesic
import addressparser as ad



ak = "mRxAQ0sVIXwFRNZkvu1PYBk8dAH5nrzo"


def search(query,region = "全国"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
    }

    params = {
        'query':  query,                #检索关键字
        'region': region,               #检索行政区划区域
        'output': 'json',               #输出格式为json
        'scope': '1',                   #检索结果详细程度。取值为1 或空，则返回基本信息；取值为2，返回检索POI详细信息
        'page_size': 1,                #单次召回POI数量，默认为10条记录，最大返回20条。
        'page_num': 0,                  #分页页码，默认为0,0代表第一页，1代表第二页，以此类推。
        'ak': ak
    }


    res = requests.get("http://api.map.baidu.com/place/v2/search", params=params, headers=headers)
    content = res.text
    decodejson = json.loads(content)  #将已编码的 JSON 字符串解码为 Python 对象，就是python解码json对象
    if decodejson["results"]>0:
        return decodejson["results"][0]
    else:
        return np.nan
    
def geocoding(address:str):
    root_url = "http://api.map.baidu.com/geocoding/v3/"
    add = quote(address)
    url = root_url + "?" + "address=" + add + "&output=json" + "&ak=" + ak
    req = urlopen(url)
    res = req.read().decode()
    temp = json.loads(res)
    return temp
    
    
def reverse_geocoding(lat, lng):
    
    root_url = "http://api.map.baidu.com/reverse_geocoding/v3/"
    
    location=str(lat) + "," + str(lng);
        #  coordtype :bd09ll（百度经纬度坐标）、bd09mc（百度米制坐标）、gcj02ll（国测局经纬度坐标，仅限中国）、wgs84ll（ GPS经纬度）
    url = root_url + "?ak=" + ak + f"&output=json&coordtype=wgs84ll&location="+location
    
    req = urlopen(url)
    res = req.read().decode()
    temp = json.loads(res)
    return temp

def my_reverse_geocoding(lat, lng):
    if lng>180:
        return "NaN"
    url = f"http://127.0.0.1:9527/queryPoint?lng={lng}&lat={lat}"
    # print(url)
    r = requests.get(url)
    # print(r.text)
    l = eval(r.text)["v"]["list"]
    if len(l) == 0:
        return "NaN"
    else:
        return l[-1]["ext_path"]
# df = geocoding("北师")

# df = reverse_geocoding(lat=39.96734505008757, lng=116.37214096404064)


def stdprov(prov):
    return ad.transform([prov]).iloc[0]["省"]

province_region_mapping = {
    '北京市': '华北',
    '天津市': '华北',
    '河北省': '华北',
    '山西省': '华北',
    '内蒙古自治区': '华北',

    '辽宁省': '东北',
    '吉林省': '东北',
    '黑龙江省': '东北',

    '上海市': '华东',
    '江苏省': '华东',
    '浙江省': '华东',
    '安徽省': '华东',
    '福建省': '华东',
    '江西省': '华东',
    '山东省': '华东',

    '河南省': '华中',
    '湖北省': '华中',
    '湖南省': '华中',

    '广东省': '华南',
    '广西壮族自治区': '华南',
    '海南省': '华南',

    '重庆市': '西南',
    '四川省': '西南',
    '贵州省': '西南',
    '云南省': '西南',
    '西藏自治区': '西南',

    '陕西省': '西北',
    '甘肃省': '西北',
    '青海省': '西北',
    '宁夏回族自治区': '西北',
    '新疆维吾尔自治区': '西北'
}


def distance_to_city(lat, lng, city):
    """
    coor : (纬度, 经度)
    city
    上海市
    上海市-市辖区
    上海市-市辖区-嘉定区
    """
    lng1, lat1 = coordinate[city]
    # print(lng1, lat1)
    p0 = Point(longitude = lng, latitude = lat)
    p1 = Point(longitude = lng1, latitude = lat1)
    distance = geodesic(p0, p1).kilometers
    return distance
    
if __name__ == "__main__":
    d = distance_to_city(31,121, "上海市")
    print(d)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
