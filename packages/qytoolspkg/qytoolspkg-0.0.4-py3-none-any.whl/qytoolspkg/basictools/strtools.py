# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:53:15 2022

@author: win10
"""
import numpy as np
import random
import jieba
from xpinyin import Pinyin
def _common_elements(strings, k = None):
    elements = np.array([''])
    count = np.array([0])
    for s in strings:
        sl = s.split(" ")
        for si in sl:
            if si in elements:
                _i = np.argwhere(elements == si)[0,0]
                count[_i] += 1
    
            else:
                elements = np.hstack([elements,[si]])
                count = np.hstack([count,[1]])
    
    # print({elements[i]:c for i,c in enumerate(count)})
    
    if k is None:
        k = sum(np.sort(count) > 0.1 *len(strings))
        print("k = ",k)
        
    ids = np.argsort(count)[-k:]
    ce = elements[ids]
    return ce

def _del_elements(strings, ce):
    new_strings = []
    for s in strings:
        sl = s.split(" ")
        for r in ce:
            if r in sl:
                sl.remove(r)
         
        new_strings.append(''.join(sl))
    return np.array(new_strings)


def _only_char(s):
    r = ''.join(x for x in s if (x.isalpha() or x==" "))
    return r

def pinyin_fenci(s):
    sf = ' '.join(jieba.cut(s))
    r = Pinyin().get_pinyin(sf, splitter='')
    return r

def matching_by_hand(strings1, strings2, common_filter = None, only_charactors = True):
    """
    以strings1为标准，输出strings2元素的标号，不在strings1中则为nan
    common_filter:
        int: k
        [int, int]: k1 k2
        [list, list]: ce1 ce2
    
    """
    from Levenshtein import distance
    strings1 = np.array(strings1)
    strings2 = np.array(strings2)
    
    if only_charactors:
        strings1 = np.array([_only_char(si) for si in strings1])
        strings2 = np.array([_only_char(si) for si in strings2])

    
    if not(common_filter is None):
        if len(common_filter) == 2 and type(common_filter[0]) == list:
            ce1, ce2 = common_filter
        else:
            if len(common_filter) == 1:
                k1 = k2 = common_filter
            else:
                k1, k2 = common_filter
                
            ce1 = _common_elements(strings1, k = k1)
            ce2 = _common_elements(strings2, k = k2)
        s1 = _del_elements(strings1, ce1)
        s2 = _del_elements(strings2, ce2)
        print("ce1: ", ce1)
        print("ce2: ", ce2)
    else:
        s1 = strings1
        s2 = strings2
    
    
    str2ind = []
    for i,n in enumerate(s2):    
        if n in s1:
            j = np.argwhere(s1 == n)[0,0]
            str2ind.append(j)
        else:
            dt = [distance(n, en) for en in s1]
            js = np.argsort(dt)
            restart = True
            while restart:
                for j in js:
                    print(i,"/",len(s2), "[",strings2[i], ']', " ==> [", n, "] is [", s1[j],"]", "<== [", strings1[j],"]")
                    ipt = input("y/n/i/h?")
                    if ipt == "y":
                        str2ind.append(j)
                        restart = False
                        break
                    
                    elif ipt == "n":
                        pass
                    
                    elif ipt == "i":
                        str2ind.append(np.nan)
                        restart = False
                        break
                    elif len(ipt) == "h":
                        h = input("input:")
                        str2ind = h
                        restart = False
                        break
                    else:
                        restart = True
                        break
    assert(len(str2ind) == len(strings2))
    return str2ind

######################################

# def comparison(label,string):
def isinstring(label, string):
    """
    judge if label in string

    """
    
    label = str(label)
    string = str(string)
    _len = len(label)
    if _len < len(string):
        decompose = [string[i:i+_len] for i in range(len(string) - _len+1)]
        return (label in decompose)
    else:
        return (label == string)
    

def onlynumber(string):
    return ''.join(list(filter(str.isdigit, string)))



def random_string(len_):
    """
    生成一个指定长度的随机字符串
    """
    random_str =''
    # base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    base_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&_><*()"

    length =len(base_str) -1
    for i in range(len_):
      random_str +=base_str[random.randint(0, length)]
    return random_str


    

def month_str(x):
    x = int(x)
    assert(1<=x<=12)
    if x<10:
        return "0"+str(x)
    else:
        return str(x)


# def month_list(start, end):
#     """
#     start format: '201101'
#     end same
    
#     生成月份的string列表
#     [start, end)    
    
#     example:
#         [201101, 201102,....]
#     """
#     _f = month_str
    
#     ms =[]
#     start_year = int(start[:4])
#     start_month = int(start[4:])
    
#     end_year = int(end[:4])
#     end_month = int(end[4:])
    
#     if start_year == end_year:
#         for m in range(start_month,end_month):
#             _m = str(start_year) + _f(m)
#             ms.append(_m)
#         return ms
    
#     else:
#         for m in range(start_month,13):
#             _m = str(start_year) + _f(m)
#             ms.append(_m)
            
#         for y in range(start_year+1, end_year):
        
#             _ms = [str(y) + _f(_m) for _m in range(1,13)]
#             ms = ms + _ms
            
#         for m in range(1, end_month):
#             _m = str(end_year) + _f(m)
#             ms.append(_m)
            
        
#         ms = np.array(ms)
#         return ms
    
    
    
def text(string, path):
    with open(path,"a") as f:
        f.write(string)
    return
    
    

def fill0forstockcode(string):
    string = str(string)
    if len(string) > 6:
        return "NaN"
        # raise ValueError(f"len of {string} > 6")
    elif len(string)==6:
        return string
    else:
        _ = ["0"] * (6-len(string))
        return "".join(_) + string
    
def random_string_list(len_ = 20, num = 20):
    import random
    # random.seed(0x1010)  #设置随机种子数
        #设置种子选择空间
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&_><*()"
    ls = [] #存取密码的列表
    FirstPsw = "" #存取第一个密码的字符
     
    while len(ls)<num:  #十个随机密码
        pwd = ""
        for i in range(len_):
            pwd += s[random.randint(0,len(s)-1)]
        if pwd[0] in FirstPsw:
            continue
        else:
            ls.append(pwd)
            FirstPsw +=pwd[0]
    return ls
    

if __name__ == "__main__":
    # a = fill0forstockcode("3")
    # print(a)
    # print(onlynumber('2022-08-15'))
    # print(month_list("201305", "202005"))
    # text("abc \n d", "./text.txt")
    # r = matching_by_hand(["1s co ele","waq co ele", "fine co ele"], ["wa co ele", "wine ele co"], common_filter=[1,1])
    # a = pinyin_fenci("贵阳农村商业银行股份有限公司")
    print(isinstring("31", "3211"))