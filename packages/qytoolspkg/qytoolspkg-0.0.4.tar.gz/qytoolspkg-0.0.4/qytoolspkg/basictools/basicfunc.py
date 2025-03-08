# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:47:38 2022

@author: win10
"""
import numpy as np
import os
import sys

def mymkdir(path:str):
    if os.path.exists(path):
        return
    path_list = path.split("/")
    path_list = path_list + [""]
    for p in range(1, len(path_list)):
        pth = '/'.join(path_list[:p])
        if not(os.path.exists(pth)):
            os.mkdir(pth)
    return    

    
# class remember:
#     def __init__(self, func):
#         """
#         一个装饰器，可以记住类内的函数值
#         """
#         self.func = func

#     def __get__(self, instance, cls = None):
#         def wrapper(*args, **kwargs):
#             n = '_' + self.func.__name__
#             if not hasattr(instance, n):
#                 r = self.func(instance, *args, **kwargs) 
#                 setattr(instance, n, r)
#             return getattr(instance, n)
#         for attr in "__module__", "__name__", "__doc__":
#             setattr(wrapper, attr, getattr(self.func, attr))
#         return wrapper
class remember:
    def __init__(self, func):
        """
        一个装饰器，可以记住类内的函数值，只能用于不能传递参数的函数
        """
        self.func = func

    def __get__(self, instance, cls = None):
        def wrapper():
            n = '_' + self.func.__name__
            if not hasattr(instance, n):
                r = self.func(instance) 
                setattr(instance, n, r)
            return getattr(instance, n)
        for attr in "__module__", "__name__", "__doc__":
            setattr(wrapper, attr, getattr(self.func, attr))
        return wrapper 
    
    
    
def softmax(x):
    """
    Paramters
    ---------
    x : np.ndarray
        len(x) = number of categories
        
    Returns
    -------
    y : np.ndarray
        sum(y) = 1.
    """
    c = np.max(x)
    exp_x = np.exp(x - c) # 溢出对策
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y


def AUC(ob,pre):
    """
    (ob观测值, pre预测值)
    """
    thresholds=np.arange(-0.00,1.001,1e-3)
    thr=0.5
    TPRate=np.zeros(len(thresholds))
    FPRate=np.zeros(len(thresholds))
    for i in range(len(thresholds)):
        TP,FN,FP,TN=0,0,0,0
        for k in range(len(ob)):
#            print(ob[k],pre[k])
            if ob[k]>thr and pre[k]>thresholds[i]:
                TP=TP+1
            if ob[k]>thr and pre[k]<thresholds[i]:
                FN=FN+1
            if ob[k]<thr and pre[k]>thresholds[i]:
                FP=FP+1
            if ob[k]<thr and pre[k]<thresholds[i]:
                TN=TN+1
        TPRate[i]=float(TP)/(TP+FN+0.000001)
        FPRate[i]=float(FP)/(FP+TN+0.000001)
    def calarea(x,y):
        area=0
        for i in range(len(x)-1):
            area=area+(y[i+1]+y[i])*(x[i]-x[i+1])/2
        return area
    AUCResult=calarea(FPRate,TPRate)

    return FPRate,TPRate,AUCResult


def confusion_matrix(ob, pre, verbose = True):
    """
    TP(True Positive)：将正类预测为正类数，真实为0，预测也为0
    FN(False Negative)：将正类预测为负类数，真实为0，预测为1
    FP(False Positive)：将负类预测为正类数， 真实为1，预测为0
    TN(True Negative)：将负类预测为负类数，真实为1，预测也为1
    """
    assert(len(ob) == len(pre))
    ob = [bool(i) for i in ob]
    pre = [bool(i) for i in pre]
    
    tp, fn, fp, tn = 0,0,0,0
    for i,obi in enumerate(ob):
        if (obi == True) and (pre[i] == True):
            tp += 1
        if (obi == True) and (pre[i] == False):
            fn += 1
        if (obi == False) and (pre[i] == True):
            fp += 1
        if (obi == False) and (pre[i] == False):
            tn += 1 
    if verbose:
        tpr=float(tp)/(tp+fn+0.000001)
        fpr=float(fp)/(fp+tn+0.000001)
        
        _ = f"""
        confusion matrix
        ------------------
        samples: {len(ob)}
        precision:{float(tp)/(tp+fp+0.000001)}
        recall:{float(tp)/(tp+fn+0.000001)}
        ------------------
           ob  T   F      
         pre
         T      {tp}   {fp}
         
         F      {fn}   {tn}
        """
        print(_)

    return tp, fp, fn, tn


def pdiv(a, b, verbose = False, inf = None):
    """
    protected division
    
    Return a/b if legal, else np.nan
    """
    # print(a,b)
    a,b = float(a),float(b)
    try:
        return a/b
    except(ZeroDivisionError):
        if verbose:
            print("num:",a,"den:",b)
        if inf is None:
            return np.nan
        else:
            return inf
    # else:
    #     raise Exception(f"{a} {b}")
    
    
def aroundzero(x, dec = 8):
    return -10**(-dec)<x<10**(-dec)
    




class TwoNomal():
    def __init__(self,mu1,mu2,sigma1,sigma2, weight):
        self.mu1 = mu1
        self.sigma1 = sigma1
        self.mu2 = mu2
        self.sigma2 = sigma2
        _weight = np.array([1, weight])
        self.weight = _weight/ _weight.sum()
    def doubledensity(self,x):
            mu1 = self.mu1
            sigma1 = self.sigma1
            mu2 = self.mu2
            sigma2 = self.sigma1
            N1 = np.sqrt(2 * np.pi * np.power(sigma1, 2))
            fac1 = np.power(x - mu1, 2) / np.power(sigma1, 2)
            density1=np.exp(-fac1/2)/N1

            N2 = np.sqrt(2 * np.pi * np.power(sigma2, 2))
            fac2 = np.power(x - mu2, 2) / np.power(sigma2, 2)
            density2=np.exp(-fac2/2)/N2
            #print(density1,density2)
            density=self.weight[0]*density1+self.weight[1]*density2
            return density


def getsizeof_recursively(obj, seen=None):
    """Recursively finds size of objects in bytes."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0  # Avoid double counting
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum([getsizeof_recursively(v, seen) for v in obj.values()])
        size += sum([getsizeof_recursively(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += getsizeof_recursively(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([getsizeof_recursively(i, seen) for i in obj])
    return size


def binary_solve(func, left, right, tol = 1e-5, max_iter = 99999):
    # https://zhuanlan.zhihu.com/p/136823356
    error = tol + 1  # 循环开始条件
    cur_root = left
    count = 1
    if func(left) * func(right) > 0:
        _ = ''.join(["func(", str(left) ,") = ", str(func(left)) ,'\n',
                     "func(", str(right),") = ", str(func(right))])
        raise ValueError(_)
    while count < max_iter:
        if error < tol:
            return left
        else:
            middle = (left + right) / 2
            if (func(left) * func(middle)) < 0:
                right = middle
            else:
                left = middle
            cur_root = left
        error = abs(func(cur_root))
        count += 1
    raise Exception(f"error = {error}")

from sklearn.metrics import roc_curve,auc
import matplotlib.pyplot as plt

def plot_roc_curves(yobs, ypres, labels, title):
    fig = plt.figure(figsize=(3,3))
    ax = fig.add_subplot(111)
    colors = ["blue","red","yellow","green","pink","purple"]
    ax.plot([0,1],[0,1],"--",color = "gray")
    for i,yp in enumerate(ypres):
        yb = yp[:,1]
        a,b,c = roc_curve(yobs, yb)
        ax.plot(a,b, color = colors[i], label = labels[i]+ " auc = %.2g"%auc(a,b))
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel("FPR")
    ax.set_ylabel("TPR")
    ax.legend(loc = "lower right",frameon=False)
    # plt.title(f"ROC Curve: {title}")
    plt.show()
        

def out_of_time(Y, years, test_year):
    _mask = lambda index: np.array([True if i in index else False for i in range(len(Y))])
    alpha = 1
    train_year = np.arange(len(Y))[years < test_year]  
    test_year = np.arange(len(Y))[years == test_year]       
    pos_ = np.arange(len(Y))[Y == 1]
    neg_ = np.arange(len(Y))[Y == 0]    
    
    train_pos = np.array(list(set(train_year)&set(pos_)))
    train_neg = np.array(list(set(train_year)&set(neg_)))
    train_neg = np.random.choice(train_neg, int(alpha*len(train_pos)), replace = False)
    test_pos = np.array(list(set(test_year)&set(pos_)))
    test_neg = np.array(list(set(test_year)&set(neg_)))
    test_neg = np.random.choice(test_neg, int(alpha*len(test_pos)), replace = False)
    
    train_mask = _mask(set(train_pos) | set(train_neg))
    test_mask = _mask(set(test_pos) | set(test_neg))
    return train_mask, test_mask

    

def out_of_sample(Y):
    _mask = lambda index: np.array([True if i in index else False for i in range(len(Y))])
    alpha = 1 # pos-neg比例
    beta = 0.8 #train-test比例
    pos_ = np.arange(len(Y))[Y == 1]
    neg_ = np.arange(len(Y))[Y == 0]
    neg_ = np.random.choice(neg_, alpha * len(pos_), replace = False)
    num_train = int(beta* len(pos_))    
    train_pos = np.random.choice(pos_, num_train, replace = False)
    test_pos = np.array(list(set(pos_) - set(train_pos)))
    train_neg = np.random.choice(neg_, num_train, replace = False)
    test_neg = np.array(list(set(neg_) - set(train_neg)))


    train_mask = _mask(set(train_pos) | set(train_neg))
    test_mask = _mask(set(test_pos) | set(test_neg))
    return train_mask, test_mask



def random_num_sum_static(n,sum_ = 1):

    """
    生成n个数，使它们的和为sum_
    且n个数同分布 期望都是 n/sum_
    """
    arr = np.random.uniform(0, 1, size = n)
    arr = np.sort(arr)
    arr = [0] + list(arr) + [1]
    arr = np.diff(arr)
    r = arr[0] + arr[-1]
    arr = np.array(list(arr[1:-1]) + [r])
    return arr * sum_
    
    

def sort_request_by_target(request, target):
    """
    按照 target 列表的顺序对 request 列表进行排序。

    参数:
        request (list): 需要被排序的列表。
        target (list): 指定排序顺序的列表。

    返回:
        list: 根据 target 排序后的 request 列表。
    """
    # 创建一个字典，将 target 中的元素映射到它们的索引 (用于确定顺序)
    target_order = {item: index for index, item in enumerate(target)}

    # 定义排序的关键规则
    def sort_key(x):
        # 如果 x 在 target_order 中，返回对应的索引；否则返回一个较大的值（让它排在后面）
        return target_order.get(x, float('inf'))

    # 根据排序规则对 request 排序
    sorted_request = sorted(request, key=sort_key)

    return sorted_request




class ConditionalSampler:
    def __init__(self, kde):
        """
        初始化条件采样器。

        Parameters
        ----------
        kde : gaussian_kde
            已经拟合好的二维核密度估计对象。
        """
        self.kde = kde

    def sample_given_dim0(self, fixed_value, size=1):
        """
        根据给定的第一个维度值，从条件分布中采样第二个维度的值。

        Parameters
        ----------
        fixed_value : float
            第一个维度的固定值。
        size : int, optional
            采样数量，默认为 1。

        Returns
        -------
        np.ndarray
            从条件分布中采样的第二个维度的值。
        """
        # 创建条件分布采样点
        num_points = 1000
        fixed_points = np.full(num_points, fixed_value)
        other_var_values = np.linspace(self.kde.dataset[1].min(), self.kde.dataset[1].max(), num_points)
        
        samples = np.vstack([fixed_points, other_var_values])
        
        # 计算联合概率密度
        joint_probs = self.kde(samples)
        
        # 计算条件概率密度
        conditional_probs = joint_probs / joint_probs.sum()
        
        # 从条件分布中进行采样
        sampled_indices = np.random.choice(num_points, size=size, p=conditional_probs)
        sampled_values = other_var_values[sampled_indices]
        if size == 1 :
            return sampled_values[0]
        else:
            return sampled_values






if __name__ == "__main__":
    # confusion_matrix([1,0,0,1,0,0,1,0,1,0,1,1], [1,0,0,1,0,1,1,1,1,0,0,0])
    # print(aroundzero(0.0000000002))
    
    N2 = TwoNomal(-69.28,-17.71,18.8,62.78,0.24)

    #创建等差数列作为X
    X = np.arange(-150,150,0.05)
    #print(X)
    Y = N2.doubledensity(X)
    import matplotlib.pyplot as plt
    #print(Y)
    plt.plot(X,Y,'b-',linewidth=3)

    plt.show()
    