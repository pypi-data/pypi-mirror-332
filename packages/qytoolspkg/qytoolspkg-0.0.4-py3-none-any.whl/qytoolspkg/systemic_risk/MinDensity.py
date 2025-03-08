# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:49:14 2024

@author: qiyu

Reference
----------
[1] Anand, K., Craig, B., Von Peter, G., 2015. Filling in the blanks: 
    network structure and interbank contagion. Quantitative Finance 
    15, 625–636. https://doi.org/10.1080/14697688.2014.968195

"""

import numpy as np
import itertools
from qytoolspkg.systemic_risk.MaxEntropy import SRAS
from scipy.special import softmax

def around0(x,dec = 0.0001):
    return -dec<x<dec

def pdiv_(a,b):
    if around0(a) and around0(b):
        return 0
    elif around0(b):
        return 99
    elif around0(a):
        return 0
    else:
        return a/b
    
class MDEstimate:
    """
    最小密度法估计银行关联网络,根据[1]给的伪代码写的。
    """
    def __init__(self, c=1):
        self.c = c
    
    def AD(self, a, z):
        ad = np.zeros(self.num_banks)
        for i in range(self.num_banks):
            ad[i] = max((a[i] - z.sum(axis = 1)[i]),0)
        return ad
    
    def LD(self, l, z):
        ld = np.zeros(self.num_banks)
        for i in range(self.num_banks):
            ld[i] = max((l[i] - z.sum(axis = 0)[i]),0)
        return ld
    
    def V(self, z, ad, ld):
        _ = -self.c * ((z>0).sum()) - \
            np.array([self.alpha[i] * (ad[i]**2)\
            + self.delta[i] * (ld[i]**2)\
            for i in range(self.num_banks)]).sum()
        return _
    
    def Qij(self, ad, ld, mu):
        q = {}
        for i,j in mu:
            q[(i,j)] = max(pdiv_(ad[i],ld[j]), pdiv_(ld[j],ad[i]))
        return q
    
    def choice_by_Qij(self, q):
    
        keys = list(q.keys())
        values = list(q.values())
        values = softmax(np.array(values) + 0.1)
        _ = np.random.choice(range(len(keys)), p = values)
        return keys[_]
        
    def error(self, ad, ld):
        e = np.array([(ad[i]**2) + (ld[i]**2)\
                      for i in range(self.num_banks)]).sum()
        return e
    
    def fit(self, 
            a, 
            l, 
            z = None, 
            epsilon = 0.1,
            lambda_ = 2,
            theta = 0.2,):
        
        # a = [7,5,3,1,3,0,1]
        # l = [4,5,5,0,0,2,4]
        if z is None:z = SRAS(a, l)
        # z = np.zeros((num_banks, num_banks))
        
        self.num_banks = len(a)
        
        self.alpha = np.ones(self.num_banks)
        self.delta = np.ones(self.num_banks)
        
        mu = list(itertools.permutations(range(self.num_banks),2))
        nu = list()

        ad = self.AD(a, z)
        ld = self.LD(l, z)
        
        tau = 1
        
        ad_0 = ad.copy()
        while (self.V(z, ad, ld) < (1 - epsilon) * ad_0.sum())\
            and len(mu)>0 :    
            rho = np.random.uniform()
            if (rho < epsilon) and (len(nu) >= 1):
                #remove link
                i,j = nu[np.random.choice(range(len(nu)))]
                ad[i] = ad[i] + z[i,j]
                ld[j] = ld[j] + z[i,j]
                z[i,j] = 0
                mu.append((i,j))
                nu.remove((i,j))
            else:
                #add link
                qij = self.Qij(ad,ld, mu)
                i,j = self.choice_by_Qij(qij)
                z_ = z.copy()
                z_[i,j] = lambda_ * min(ad[i], ld[j])
                phi = np.random.uniform()
                ad_ = self.AD(a, z_)
                ld_ = self.LD(l, z_)
                
                v_ = self.V(z_, ad_, ld_)
                v = self.V(z, ad, ld)
                if (v_ > v) or (phi < np.exp(theta * (v_ - v))):
                    z = z_
                    ad = ad_
                    ld = ld_
                    mu.remove((i,j))
                    nu.append((i,j))
            
            qij = self.Qij(ad, ld, mu)
            tau += 1                     
        e = self.error(ad, ld)
        return z,e
         
