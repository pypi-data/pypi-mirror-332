# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:33:32 2024

@author: qiyu

Reference
---------
[1] Andrecut, M. 2016. “Systemic Risk, Maximum Entropy and Interbank Contagion.” 
    International Journal of Modern Physics C 27(12):1650148. doi: 10.1142/S0129183116501485.
"""
import numpy as np

def SRAS(a, l, q = None, dt = 1e-3):
       
    """
    a: 资产总计
    l: 负债总计
    q: 邻接矩阵，若为none则为去除对角元的全连接，即为RAS算法。
    
    a和l要做归一化
    所以sum(a)不一定严格等于sum(l)
    但是最终的矩阵用a的和，即total asset进行还原。
    """
    N = len(a)
    assert(len(a) == len(l))
    if q is None:
        q = np.ones((N,N)) - np.eye(N)
    
    a_ = np.array(a)
    l_ = np.array(l)
    # print(a)
    # print(l)
    # import sys
    # sys.exit()
    total_asset = a_.sum()

    
    a = a_/a_.sum()
    l = l_/l_.sum()
    
    psi = a.copy()
    phi = l.copy()
    
    eta = 999
    while np.sqrt(eta) > dt:
        eta = 0
        for i in range(N):            
            s = np.dot(q[i,:] , phi)
            ksi = a[i]/s
            eta = eta + (ksi - psi[i]) ** 2
            psi[i] = ksi
        for j in range(N):
            s = np.dot(q[:,j] , psi)
            # print(s)
            ksi = l[j]/s
            eta = eta + (ksi - phi[j]) ** 2
            phi[j] = ksi
    
    x = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            x[i,j] = q[i,j] * psi[i] * phi[j]
            
    x = x * total_asset
    
    u = np.sum((x.sum(1) - a_)**2) + np.sum((x.sum(0) - l_)**2)
    v = np.sum(a_**2) + np.sum(l_**2)
    epsilon = np.sqrt(u/v)    
    
    return x, epsilon




# 设定网络结构 (全连接 随机 中心外围 无标度 异配) -> 估计 -> 冲击设定 -> 传染设定 


if __name__ == "__main__":
    q = np.array([[1,1,0,0],[1,1,0,1],[0,1,1,0],[0,0,1,1]])
    
    m,e = SRAS(a = [10, 8, 5, 1], l = [10, 8, 5, 1],q = q)
    print(m,e)