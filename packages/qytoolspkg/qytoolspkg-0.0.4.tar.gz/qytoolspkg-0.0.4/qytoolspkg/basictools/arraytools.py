# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:06:54 2022

@author: win10
"""

from qytoolspkg.basictools.normalization import cdf_norm
from qytoolspkg.basictools.mytypes import scalar_types, vector_types, \
    int_types, matrix_types, float_types, missvalue
import numpy as np
from itertools import product


def canning(x, partition):
    """
    对输入向量 x 进行分段标记，根据 partition 来决定如何分段。

    Parameters
    ----------
    x : array-like, shape (n,)
        输入的一维向量，表示要被分段的数据。
    partition : scalar or array-like
        嵌套的分界值，用于划分 x 的不同段。可以是一个标量，表示二分法，或是一个向量。

    Returns
    -------
    x_canned : np.ndarray, shape (n,)
        分段后的标记，每个元素的值表示其所在的段，最大值为 len(partition)，最小值为 0。

    Examples
    --------
    1. 使用标量作为 partition：
    >>> x = [1, 2, 3, 4, 5]
    >>> partition = 3
    >>> canning(x, partition)
    array([0, 0, 1, 1, 1])  # 小于 3 的为 0，其他为 1

    2. 使用向量作为 partition：
    >>> x = [1, 2, 3, 4, 5]
    >>> partition = [2, 4]
    >>> canning(x, partition)
    array([0, 1, 1, 2, 2])  # 小于 2 的为 0，2 到 4 为 1，大于等于 4 为 2
    """
    x = np.array(x)
    if type(partition) in scalar_types:
        _di_ = True
    elif((type(partition) in vector_types) and (len(partition) == 1)):
        _di_ = True
    else: 
        _di_ = False
    
    ng = len(partition) + 1
    if _di_:
        x_canned = np.array([int(xi > partition) for xi in x]) * 1
    else:
        partition = np.array(partition)[np.argsort(partition)]
        xc_min = np.array([int(i >= partition[-1]) for i in x]) * ng
        xc_max = np.array([int(i < partition[0]) for i in x]) * 1
        x_canned = xc_max + xc_min
        for i in range(ng)[1:-1]:
            xc_middle = np.array([int(partition[i - 1] <= j \
                                      < partition[i]) for j in x]) * (i + 1)
            x_canned += xc_middle
        x_canned -= 1
    return x_canned

# def canning(x, partition):    
#     return np.digitize(x, partition)

def range_equally_canning(x, num):
    _max = max(x)
    _min = min(x)
    if not((type(num) in int_types) and (num > 1)):
        raise ValueError(f"{num} error!")
    partition = np.linspace(_min, _max, num + 1, endpoint = True)
    x_canned = canning(x, partition[1:-1])
    return x_canned

def cdf_canning(x, partition):
    if max(partition) >= 1:
        raise ValueError(f"max of partition:{partition} must < 1.")
    if max(partition) <= 0:
        raise ValueError(f"min of partition:{partition} must > 0.")

    x_ = cdf_norm(x)
    x_canned = canning(x_, partition)
    return x_canned

def cdf_equally_canning(x, num):
    """
    Returns
    -------
    x_canned 
        equipartition, the numbers of xi in each groups are approximatly equal.
    """
    x_ = cdf_norm(x)
    x_canned = range_equally_canning(x_, num)
    
    # partition = np.linspace(0, 1, num + 1, endpoint = True)
    # partition = [np.quantile(x, n) for n in partition]
    # print(partition)
    # x_canned = np.digitize(x, partition)
    return x_canned


def sickle(x: matrix_types,
           threshold: float_types = 0.0,
           x_subtract = False
           ):
    """
    Parameters
    ----------
    x: ndarray
        data you want to cut.
    threshold: float
        ...
    x_subtract:
        if True, return x - thres where x > thres.
    Example
    -------
    if x_subtract == False:
        sickle([1,-0.5, 6, 0.9, 0.1....]) = [1, 0, 6, 0.9, 0.1....]
    else:
        sickle([1,-0.5, 6, 0.9, 0.1....],0.1) = [0.9, 0, 5.9, 0.8, 0.0....]

    """
    if type(x) in float_types:
        x = float(x)
    else:
        x = np.array(x)
    
    if x_subtract:
        return ((x - threshold) > 0) * 1 * (x - threshold)
    else:    
        return ((x - threshold) > 0) * 1 * x

def shuffle_n_round(x,n):
    """
    To shuffle x for n round.
    return a list, includes n shuffled series.
    """
    x_s=[]
    for i in range(n):
        _ = x.copy()
        np.random.shuffle(_)
        x_s.append(_)
    return x_s 

def exist_npnan(xi):
    return np.isnan(np.array(xi, dtype = float)).sum()

def all_npnan(xi):
    _xi = np.array(xi, dtype = float).reshape(1,-1)[0]
    if np.isnan(_xi).sum() == len(_xi):
        return True
    else:
        return False
    
def discard(x, exist = True):
    """
    Parameters
    ----------
    exist : bool, optional
        if true, discard every x[i] with nan in it. 
        if false, only discard x[i] all nan.
        The default is True.
        
    Returns
    -------
    TYPE
        DESCRIPTION.
    """
    if exist:
        return np.array([xi for xi in x if not exist_npnan(xi)])
    else:
        return np.array([xi for xi in x if not all_npnan(xi)])

# def fill(x, fillwith:float = 0):
#     for _i,xo in enumerate(x):
#         if not (all_npnan(xo)):
#             _shape = np.array(xo, dtype = float).shape
#     fillwith = np.zeros(_shape) + fillwith
    
    
def difference(x,with_nan = True):
    """
    Parameters
    ----------
    with_nan
    
    Returns
    -------
    x_d : ndarray, dtype = float
        len(x_d) = len(x)
    """
    if with_nan:
        x_d = []
        for _i,xo in enumerate(x):
            if not (all_npnan(xo)):
                _shape = np.array(xo, dtype = float).shape
                break
        for i,xi in enumerate(x):
            if i <= _i:
                x_d.append(np.zeros(_shape) * np.nan)
            else:
                if not (all_npnan(xi)):
                    x_d.append(np.array(xi,dtype = float) - \
                               np.array(xo, dtype = float))
                    xo = xi
                else:
                    x_d.append(np.zeros(_shape) * np.nan)
        x_d = np.array(x_d, dtype = float)
    else:
        _shape = np.array(x[0], dtype = float).shape
        x_d = [np.zeros(_shape) * np.nan]
        _ = [np.array(x, dtype=float)[i] - \
             np.array(x, dtype=float)[i-1] for i in range(1,len(x))]
        x_d += _
        x_d = np.array(x_d, dtype = float)
    return x_d

def fill_equal_to_former(x):
    _x = x.copy()
    x_o = np.nan
    for i,xi in enumerate(x):
        if missvalue(xi):
            _x[i] = x_o
        else:
            x_o = xi
    return _x

def equal_len(*x):
    if len(list(set([len(xi) for xi in x]))) == 1:
        return True
    else:
        return False
     
def roll(x:np.array, y:np.array, lw:int, dt=1):#TODO: 改用discard函数写，多变量
    """
    由两个array生成 滑动时间窗口样本
    """
    _index = ~(np.isnan(x) | np.isnan(y))#mytypes.missvalue_series
    _x = x[_index]
    _y = y[_index]
    samples = list()
    for i in range(lw,len(_x)):
        x_ = _x[i-lw:i]
        y_ = _y[i-lw:i]
        samples.append((x_,y_))
    samples = np.array(samples)[::dt]
    return samples
    


def matrix_block(m:np.array,
                 points,
                 apply_func = np.mean) -> np.array:
    """
    矩阵分块操作
    
    m: np.array
        dim = (N * N)
    
    point: 1darray
        indexes of split point, not include.
        
    apply: function applied on every block
        to sum: np.sum
    
        
    Return
    ------
    bm: np.array
        dim  = (len(points) + 1, len(points) + 1)
        
        
    Example
    -------
    
    a =  array([[0, 1, 2, 3],
                [2, 3, 4, 5],
                [3, 4, 5, 6],
                [4, 5, 6, 7]])
    
    matrix_block(a,[1])
    array([[0., 2.],
           [3., 5.]])
    
    matrix_block(a,[2]) 
    array([[1.5, 3.5],
           [4. , 6. ]])
    """
    
    gs = len(points) + 1
    points = np.hstack([[0],points,[len(m[0])]])
    bm = np.zeros((gs,gs))

    for j,k in product(set(range(gs)),repeat=2):
        block = m[points[j]:points[j+1],points[k]:points[k+1]]
        bm[j,k] = apply_func(block)
    return bm
    
    
def getmax(x, q, sort=False):
    """
    Parameters
    ----------
    x : 1d array
    q : int or float
        int: q >= 1, returns the top q elements
        float: 0 < q < 1, returns elements greater than or equal to the q-th quantile
    sort : bool, optional
        If True, returns the result in sorted order. Default is False.

    Returns
    -------
    x_max: 1d array
    """
    x = np.array(x)
    if x.shape != (len(x),):
        raise ValueError("x must be a 1-dimensional array")
    
    if not isinstance(q, (int, float)):
        raise TypeError("q must be an int or float")
    
    if q >= 1:
        if not isinstance(q, int):
            raise ValueError("q must be an integer when q >= 1")
        if q > len(x):
            raise ValueError("q cannot be greater than the length of x")
        max_index = np.argsort(x)[-q:]
        if not sort:
            max_index.sort()
        return x[max_index]
    else:
        if not (0 < q < 1):
            raise ValueError("q must be between 0 and 1 when q is a float")
        threshold = np.quantile(x, q)
        max_index = x >= threshold
        if sort:
            return np.sort(x[max_index])
        else:
            return x[max_index]
        
        
def getmin(x, q, sort=False):
    """
    Parameters
    ----------
    x : 1d array
    q : int or float
        int: q >= 1, returns the smallest q elements
        float: 0 < q < 1, returns elements less than or equal to the q-th quantile
    sort : bool, optional
        If True, returns the result in sorted order. Default is True.

    Returns
    -------
    x_min: 1d array
    """
    x = np.array(x)
    if x.shape != (len(x),):
        raise ValueError("x must be a 1-dimensional array")

    if not isinstance(q, (int, float)):
        raise TypeError("q must be an int or float")

    if q >= 1:
        if not isinstance(q, int):
            raise ValueError("q must be an integer when q >= 1")
        if q > len(x):
            raise ValueError("q cannot be greater than the length of x")
        min_index = np.argsort(x)[:q]
        if not sort:
            min_index.sort()
        return x[min_index]
    else:
        if not (0 < q < 1):
            raise ValueError("q must be between 0 and 1 when q is a float")
        threshold = np.quantile(x, q)
        min_index = x <= threshold
        if sort:
            return np.sort(x[min_index])
        else:
            return x[min_index]
        
        
def cutmax(x,q):
    x = np.array(x)
    assert(x.shape == (len(x),))
    if q >= 1:
        assert(q<=len(x))
        q = int(q)
        max_index = np.argsort(x)[:-q]
        max_index.sort()
        return x[max_index]
    else:
        max_index = x < np.quantile(x, q)
        return x[max_index]
 
    
def cutmin(x, q):
    x = np.array(x)
    assert(x.shape == (len(x),))
    if q >= 1:
        assert(q<=len(x))
        q = int(q)
        max_index = np.argsort(x)[q:]
        max_index.sort()
        return x[max_index]
    else:
        max_index = x > np.quantile(x, q)
        return x[max_index]    

    
    
def label01(len1, len0, _1first = True):
    _ = np.array([int(i) for i in np.hstack([np.ones(len1), 
                                             np.zeros(len0)])]).reshape(len1 + len0)
    return _
if __name__ == "__main__":
    x = [1,3,6,1,4,5,1,5,1,1,3,2]
    # print(sickle(x,3,True))
    # x = [np.nan,[4,2],[5,8],np.nan,[3,5]]
    # p = [2.5,5]
    # print(canning(x, p))
    # print(cdf_equally_canning(x, num = 3))
    # print(difference(x))
    # a = np.hstack([np.ones(10), np.zeros(10)])
    # b = np.random.randn(20)
    # print(dummy(a))
    # print(len(roll(a,b,3)))
    # print(label01(2, 3))
    1