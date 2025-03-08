# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:14:42 2024

@author: qiyu

Reference
----------
[1] 隋聪, 王宪峰, 王宗尧, 2017. 银行间网络连接倾向异质性与风险传染. 
    国际金融研究 44–53. https://doi.org/10.16475/j.cnki.1006-1029.2017.07.005
    
[2] Anand, K., Van Lelyveld, I., Banai, Á., Friedrich, S., Garratt, 
    R., Hałaj, G., Fique, J., Hansen, I., Jaramillo, S.M., Lee, H., 
    Molina-Borboa, J.L., Nobili, S., Rajan, S., Salakhova, D., Silva, 
    T.C., Silvestri, L., De Souza, S.R.S., 2018. The missing links:
    A global study on uncovering financial network structures from 
    partial data. Journal of Financial Stability 35, 107–119.
    https://doi.org/10.1016/j.jfs.2017.05.012

[3] Soramaki K., Bech M., Arnold J., Glass R., Beyeler W. The Topology of 
    Interbank Payment Flows[J]. Physica A,  2007, 379 (1): 317-333
    
"""
import pandas as pd
import numpy as np
from MinDensity import MDEstimate
from MaxEntropy import SRAS
import random
import networkx as nx
from itertools import permutations, combinations
from qytoolspkg.basicfunc import random_num_sum_static
# from imblearn.over_sampling import SMOTE
# from index_construct import pqc_vul_sample_gen
  

def concentrated_topN(x, N):
    assert(len(x) > N)
    top = (np.sort(x)[-N:]).sum()
    c = top / x.sum()
    return c

def self_developed_ratio(x):
    if x == 2:
        return np.random.uniform(0.5,0.8)
    elif x==3:
        return np.random.uniform(0.4,0.7)
    elif x==4:
        return np.random.uniform(0.2,0.5)
    else:
        return 0

def outsourcing_num(x):
    if x["outsourcing_type"] == 2:
        return 1
    else:
        if x["Bnature"] == 2:
            return np.random.choice(range(5,10))
        elif x["Bnature"] == 3:
            return np.random.choice(range(3,8))
        elif x["Bnature"] == 4:
            return np.random.choice(range(2,5))
        else:
            return np.random.choice(range(1,3))
            
            
def outsourcing_type(x):
    """
    0 外包建设，自行运维
    1 外包建设运维
    2 托管
    
    假定大型银行和股份制都采用0的方式
    城商行01
    农商行012
    """
    if x == 2:
        return 0
    elif x==3:
        return 0
    elif x==4:
        return np.random.choice([0,1], p = [0.5,0.5])
    else:
        return np.random.choice([0,1,2], p = [0.1,0.6,0.3])

def custodian_bank(cb,p, x):
    if x!=2:
        return 0
    else:
        return np.random.choice(cb, p = p)
# 
# def PQC_VUL(x):
#     if x == 2:
#         return 0.1
#     elif x==3:
#         return 0.2
#     elif x==4:
#         return 0.3
#     else:
#         return 0.4

def gamma_b(x):
    #银行的恢复速度
    return np.random.uniform(0.3,0.7)


def upsampling(n, ta, bnature, banks):
    upassets = random_num_sum_static(n, ta)
    tamp = banks[banks["Bnature"] == bnature].index
    # tamp_p = np.array(banks[banks["Bnature"] == bnature]["ib2"])
    # tamp_p = range_norm(tamp_p) * 100
    # tamp_p =(1- range_norm(tamp_p))
    # tamp_p = tamp_p/tamp_p.sum()
    
    for a in upassets:
        # idx = np.random.choice(tamp, p = tamp_p)    
        idx = np.random.choice(tamp)
        tp = banks.loc[idx]
        r = a/tp["total_assets"]
        dic = {"Bankcd":"upsample",
               "total_assets":a,
               "Bnature":bnature}
        for k in ["capital","risk_weighted_assets",
                  "ia1","ia2","ia3","ib1","ib2","ib3"]:
            dic[k] = tp[k] * r
        
        banks.loc[len(banks)] = dic
    return banks

def redist_ib2(banks):
    """
    按ib2 拆借关系重新分配，平衡资产负债
    按upsample银行的资产加ib2 
    """
    banks = banks.copy()
    banks_copy = banks.copy()
    gap = banks["ia2"].sum() - banks["ib2"].sum()
    if gap > 0:
        col = "ib2"
    else:
        col = "ia2"

    samples = banks[banks["Bankcd"] == "upsample"].copy()
    sum_ = samples["total_assets"].sum()
    samples["share"] = samples["total_assets"].apply(lambda x: x/sum_)
    samples["e"] = samples.apply(lambda x: x[col] + x["share"] * gap, axis = 1)
    for idx in samples.index:
        banks_copy.at[idx, col] = samples.at[idx,"e"]
    return banks_copy
    
    
def node_degree_by_strength(s, alpha = 1, beta = 1/1.9, basevalue = 3):
    return int(np.power(s/alpha, beta)) + basevalue


def gen_banks(seed_banks):
# if 1:
    """
    生成N家银行，资产规模呈现幂律分布
    ia1 长期同业
    ia2 短期同业
     
    Parameters
    ----------
    N : 
    
    Returns
    -------
    Dataframe columns = [bankname, 
                         assets, 
                         interbank assets(ia1), 
                         interbank debt(ib1), 
                         self_developed_ratio,]
    """
    
    # path = PROCESS + "./bankcontagion/"
    # banks = pd.read_csv(path + "bank_data_2022_all.csv")
    
    banks = seed_banks
    
    info = pd.read_excel(path + "info_new.xlsx",
                         # index_col="Bankcd",
                         usecols=["Bankcd","Bnature"])
    
    
    
    banks = pd.merge(banks, info,how = "inner",on ="Bankcd")
    # 1.政策性银行
    
    # 2.国有控股大型商业银行 5/6 少邮储
    # 3.股份制商业银行 12 全
    # 4.城市商业银行 55/130
    # 5.农村商业银行 23/1569 
    
    # 6.外资银行
    # 7.其他
    # 8.农合行
    # 9.农信社
    # 10.三类新型农村金融机构
    
    # 2021年 股份制商业银行12家、国有大型商业银行6家、村镇银行1642家、
    # 农村商业银行1569家，农村信用社609家、 企业集团财务公司257家、
    # 城市商业银行130家、金融租赁公司71家、信托公司68家、农村资金互助社41家、
    # 外资法人银行41家、农村合作银行26家、 汽车金融公司25家、消费金融公司29家
    
    #upsample 

    banks = upsampling(75, 119499, 4, banks)#货币单位(亿元)
    banks = upsampling(1546, 367888, 5, banks)
    banks = redist_ib2(banks)
    
    # a = banks[["ia1","ia2","ia3"]]
    # print(a.sum())
    # print(a.sum().sum())
    # b = banks[["ib1","ib2","ib3"]]
    # print(b.sum())
    # print(b.sum().sum())
        
    bankid = ["b" + str(i) for i in banks.index]
    banks.index = bankid
    banks["self_developed_ratio"] =\
        banks["Bnature"].apply(self_developed_ratio)
    banks["outsourcing_type"] = \
        banks["Bnature"].apply(outsourcing_type)
    
    cb = banks[banks["Bnature"].isin([2,3])].index
    a_ = np.array(banks.loc[cb]["total_assets"])
    p_ = a_/a_.sum()
    _f = lambda x: custodian_bank(cb, p_, x)
    banks["custodian_bank"] = \
        banks["outsourcing_type"].apply(_f)
    banks["outsourcing_num"] = \
        banks.apply(outsourcing_num, axis = 1)
    # banks["PQC_VUL"] = \
    #     banks["Bnature"].apply(PQC_VUL)
    banks = pqc_vul_sample_gen(banks)
    banks["gamma_b"] = \
        banks["Bnature"].apply(gamma_b)
        
    # md = MDEstimate()
    # net = md.fit(ia, ib)
    
    # 最大熵估计，debtrank适用最大熵见文献 2
    # 我们先用最大熵，然后把最大熵估计作为连边概率，按资产大小选连边数量，
    # 再用一次最小kl散度
    # 连边数量见文献 1
    
    ia = np.array(banks.loc[bankid]["ia2"])
    ib = np.array(banks.loc[bankid]["ib2"])
    
    net,_ = SRAS(ia, ib)

    dim = 0#按负债方分配节点数
    ks = [node_degree_by_strength(s,
                                  alpha=0.01,#越大 density越小
                                  beta=1/1.9,#银行间 集中度
                                  basevalue=3)\
          for s in net.sum(dim)]
    adj0 = np.zeros(net.shape, dtype = bool)
    for i, n in enumerate(net.T):
        idx = np.random.choice(range(len(n)),size = ks[i], p= n/n.sum())
        adj0[idx,i] = True

    dim = 1#按资产方分配节点数
    ks = [node_degree_by_strength(s,
                                  alpha=0.01,#越大 density越小
                                  beta=1/1.9,#银行间 集中度
                                  basevalue=3)\
          for s in net.sum(dim)]
    adj1 = np.zeros(net.shape, dtype = bool)
    for i, n in enumerate(net):
        idx = np.random.choice(range(len(n)),size = ks[i], p= n/n.sum())
        adj1[i,idx] = True

    adj = (adj0 + adj1).astype(bool)
    
    # plt.figure(figsize=(6, 4))
    # sea.heatmap(pd.DataFrame(1-adj, columns=banks.index, index = banks.index), 
    #             cmap='gray', cbar=False, square=True, linewidths=0.)
    # plt.show()
    # print("adj density:",adj.sum()/len(adj)**2)
    
    net,e = SRAS(ia, ib, q=adj)
    # print("epsilon:", e)
    net = pd.DataFrame(net, index=bankid, columns=bankid)
    
    return banks, net
   
def supcorr(supinfo, net = "ER", params = {"p": 0.3}):
    supid = supinfo.index
    num_sup = len(supid)
    if net == "ER":
        er_graph = nx.erdos_renyi_graph(num_sup, **params)
        adj = nx.to_numpy_array(er_graph)
        return pd.DataFrame(adj, columns=supid, index = supid)


def biosc(banks:pd.DataFrame, 
          M = 50, 
          k = 1e-5,
          M0 = 1):
    """
    # Bank Information System Outsourcing Company
    M = 50 #供应商家数
    k = 1e-5 #调供应商集中度的参数
    
    """
    banks = banks.copy()
    oscomp = np.ones(M)*M0

    bw = []
    idx = []
    
    def _f(x):
        if x==2:
            return np.nan
        else:
            return False
    banks["os_type_is_2"] = banks["outsourcing_type"].apply(_f)
    banks=banks.dropna()
    
    bankid = banks.index
    N = len(bankid)

    for i,b in enumerate(bankid):
        asset = banks.loc[b]["total_assets"]
        num_supplier_b = banks.loc[b]["outsourcing_num"]
        #银行供应商家数和银行类型有关
        bw = bw + [asset * k] * num_supplier_b
        idx = idx + [i] * num_supplier_b
    
    supplier_net = np.zeros((N, M)) #num_banks, num_suppliers
    
    shf = np.arange(len(bw))
    np.random.shuffle(shf)
    
    for i in shf:
        s = np.random.choice(range(M), p = oscomp/oscomp.sum())
        oscomp[s] += bw[i]
        supplier_net[idx[i],s] += bw[i]
    
    # print("concentration top10: ", concentrated_topN(oscomp, 10))
    concent = concentrated_topN(oscomp, 10)
    oscomp_share = oscomp/ oscomp.sum()
    
    _sup = np.array([supplier_net[i] * \
                     (1 - banks.loc[k]["self_developed_ratio"])\
                    for i,k in enumerate(bankid)])
    bankinfosysco = (_sup @ _sup.T) *  10
    # supco =  (_sup.T @ _sup)
    supid = ["s" + str(i) for i in range(M)]
    sup_attr = pd.DataFrame(columns=["scale", "PQC_VUL"], index=supid)
    sup_attr["scale"] = supplier_net.sum(axis = 0)
    sup_corr = supcorr(sup_attr)

    supplier_net = pd.DataFrame(supplier_net, index=bankid, columns = supid)
    bank_corr = pd.DataFrame(bankinfosysco, columns=bankid, index=bankid)
    
    # sup_corr = pd.DataFrame(supco, columns=supid, index = supid)
    # return bank_corr, oscomp_share, supplier_net
    return supplier_net, sup_corr, sup_attr, concent


class SIRContagion:
    def __init__(self, 
                 banks,
                 supplier_net, 
                 supplier_corr, 
                 supplier_attr, 
                 supplier_contagion = True
                 ):
        """
        Parameters
        ----------
        banks : 
        supplier_net : num_banks * num_suppliers
        supplier_corr: num_suppliers * num_suppliers
        supplier_attr
        """
        self.banks = banks
        self.supnet = supplier_net
        self.supcor = supplier_corr
        self.bankid = list(self.banks.index)
        self.supid = list(self.supcor.index)
        self.bankid_ = list(self.supnet.index)
        self.infected_bank = {}
        self.infected_sup = {}
        self.immune_list = []
        
        self.sup_size = self.supnet.sum(axis = 0) + 0.1
        
        self.num_banks = len(self.bankid)
        self.num_suppliers = len(self.supid)
        self.round = 0
        self.ksi = 0.1
        self.supplier_attr = supplier_attr#目前没什么用
        self.cus_dic = self.type2supdic()
        self.global_sup_fragility = 0.2 if supplier_contagion else 0
        self.label = None
        self.label_list = []
        _, self.ce = self.cont_net(False)
        self.get_bankloss_label = None
        
        
    def type2supdic(self):
        """
        创建一个字典，将每个保管银行（custodian bank）与其对应的外包银行（outsourcing bank）关联起来。
        
        Returns
        -------
        dic : dict
            一个字典，键为保管银行 ID，值为外包银行的 ID 列表。
        """
        dic = {}
        for b in self.bankid:
            if self.banks.loc[b]["outsourcing_type"] == 2:
                cb = self.banks.loc[b]["custodian_bank"] 
                if cb in dic.keys():
                    dic[cb].append(b)
                else:
                    dic[cb] = [b]
        return dic
    
    def node_scale(self, x):
        if x["type"]=="bank":
            return sum(self.supnet.loc[x["id"]])
        else:
            return sum(self.supnet[x["id"]])
        
    def cont_net(self, output = False):
        """
        构建传染网络gephi file，包括节点和边的信息。
        """
        nodes = [str(i) for i in self.bankid_] + \
            [str(i) for i in self.supid]
        if output:
            node_type = ["bank"] * len(self.bankid_) + \
                ["supplier"] * len(self.supid)
            nodes = pd.DataFrame(np.array([nodes, node_type]).T,\
                                 columns=["id","type"])
            nodes["scale"] = nodes.apply(self.node_scale,axis = 1)
            nodes = nodes.set_index("id")
            
        edges = pd.DataFrame(columns=\
                             ["source","target","target_type",
                              "Type","weight"])
        
        for s in self.supid:
            source =  str(s)
            for i,w in enumerate(self.supnet[s]):
                target = str(self.bankid_[i])
                weight = w
                if weight > 0:
                    edges.loc[len(edges)] = \
                        [source, target,"bank","directed",weight]
                else:
                    pass
        
        for c in combinations(self.supid, 2):
            s, t = c
            w = self.supcor.loc[s][t]
            source =  str(s)
            target =  str(t)
            if w > 0:
                if output:
                    edges.loc[len(edges)] = \
                        [source, target,"soc","undirected",w]
                else:
                    edges.loc[len(edges)] = \
                        [source, target,"soc","directed",w] 
                    edges.loc[len(edges)] = \
                        [target, source,"soc","directed",w] 
        edges.index.name = "id"
        return nodes, edges
        
    def attack(self, sid = None, bid = None, level = 0.1, label = "attack"):
        """
        开始攻击过程，感染指定的供应商。
        
        Parameters
        ----------
        sid : list
            需要感染的供应商 ID 列表。
        bid : list
            感染银行列表
        level : float, optional
            攻击的强度，默认为 0.2。
        """
        self.bankloss = self.banks.copy()[["total_assets", "capital"]]
        self.level = level
        self.label = f"{label}_lv{level}"
        if self.label in self.label_list:
            self.label = self.label + "_"
        self.label_list.append(self.label)
        
        if not(sid is None):
            for s in sid:
                self.infected_sup[s] = 0
       
        if not(bid is None):
            self.step0(bid)
        
        return 
    
    def step0(self, bid):
        """
        若开始感染的是银行则执行step0, 银行->供应商
        """
        for b in bid:
            self.infected_bank[b] = 0     
        rl = f"{self.label}_rd{self.round}"
        self.bankloss = pd.concat([self.bankloss,
                                   pd.DataFrame(np.zeros(self.num_banks), 
                                                index = self.bankid,
                                                columns=[rl])], axis=1)
        for sb in self.infected_bank:
            l = self.infected_loss(sb)
            self.bankloss.at[sb,rl] = l
            self.type2loss(sb, rl, l)
        
        for b in list(self.infected_bank.keys()):
            suss = list(self.ce[(self.ce["target"] == b)\
                               &(self.ce["target_type"] =="bank")]\
                       ["source"])
            for s in suss:
                a = np.random.uniform()
                if a < self.sup2bank_fragility(s, b):
                    self.infected_sup[s] = 0
        return
    
    def sustained_loss(self, b):
        # 持续性损失, 感染损失的ksi倍，默认0.1
        return self.ksi * self.infected_loss(b)
    
    def infected_loss(self, b):
        # 感染损失，总资产1% * pqc_vul
        ta = self.banks.loc[b]["total_assets"]
        f = self.banks.loc[b]["PQC_VUL"]
        # return ta * np.sqrt(f) * 0.01
        return ta * f * self.level * 1e-2
    
    def bank_fragility(self, b, s):
        w = self.supnet.loc[b][s]/sum(self.supnet.loc[b])
        #该供应商在银行外包中占的比例 
        # f = self.banks.loc[b]["fragility"]
        #银行自身的脆弱性 
        # print( w * self.level)
        return w * self.level
    
    def sup2bank_fragility(self, s, b):
        w = self.supnet.loc[b][s]/sum(self.supnet[s])
        return w * self.level
    
    def sup_fragility(self,s0,s1):
        #from s0 s1 #供应商关联就是0/1
        # print(self.supcor.loc[s0][s1] * self.level)
        return self.global_sup_fragility * self.supcor.loc[s0][s1] * self.level 
    
    def type2loss(self, b, r, l):
        """
        托管银行的损失
        """
        # 
        if b in self.cus_dic.keys():#b大银行
            for bb in self.cus_dic[b]:#bb小银行
                a0 = self.banks.loc[b]["total_assets"]
                a1 = self.banks.loc[bb]["total_assets"]
                self.bankloss.at[bb,r] = (l * (a1/a0))
        return 
    
    def step(self):
        self.round += 1
        # 银行损失
        for k in self.infected_bank:
            self.infected_bank[k] += 1
        for k in self.infected_sup:
            self.infected_sup[k] += 1
        
        rl = f"{self.label}_rd{self.round}"
        self.bankloss = pd.concat([self.bankloss,
                                   pd.DataFrame(np.zeros(self.num_banks), 
                                                index = self.bankid,
                                                columns=[rl])], axis=1)
        # self.bankloss[rl] = np.zeros(self.num_banks)
        for sb in self.infected_bank:
            l = self.sustained_loss(sb)
            self.bankloss.at[sb,rl] = l
            self.type2loss(sb, rl, l)
                
        # 传染, 先往银行传,再传其他供应商
        for s in list(self.infected_sup.keys()):
            susb = list(self.ce[(self.ce["source"] == s)\
                               &(self.ce["target_type"] =="bank")]\
                       ["target"])
            for sb in susb:
                if not(sb in list(self.infected_bank.keys())\
                       + self.immune_list):
                    a = np.random.uniform()
                    # print(a, self.bank_fragility(sb, s))
                    if a < self.bank_fragility(sb, s):
                        l = self.infected_loss(sb)
                        self.infected_bank[sb] = 0
                        self.bankloss.at[sb,rl] = l
                        self.type2loss(sb, rl, l)
                        
            suss = list(self.ce[(self.ce["source"] == s)\
                               &(self.ce["target_type"] =="soc")]\
                       ["target"])    
            for ss in suss:
                if not(ss in list(self.infected_sup.keys())\
                       + self.immune_list):
                    a = np.random.uniform()
                    if a < self.sup_fragility(s, ss):
                        self.infected_sup[ss] = 0
        # 康复 recov
        for sb in list(self.infected_bank.keys()):
            a = np.random.uniform()
            if a > 1- self.banks.loc[sb]["gamma_b"] \
                * self.infected_bank[sb]:
            # if a > 0:
                del self.infected_bank[sb]
                self.immune_list.append(sb)
        for ss in list(self.infected_sup.keys()):
            a = np.random.uniform()
            if a >  1 - self.sup_size[ss] \
                * self.infected_sup[ss]:#gamma_c
                del self.infected_sup[ss]
                self.immune_list.append(ss)
        return
    
    def get_bankloss(self, threshold = 1):
        """
        返回上次调取get_bankloss本函数后所有的bankloss
        """
        cols = self.bankloss.columns[2:]
        if self.get_bankloss_label is None:
            c = cols
            self.get_bankloss_label = cols[-1]
        else:
            idx = np.argwhere(np.array(cols) == self.get_bankloss_label)[0,0]
            if idx == len(cols):
                # _ = pd.Series(np.zeros(len(self.banks.index)), index=self.banks.index)
                return {}
            c = cols[idx + 1 :]
            self.get_bankloss_label = cols[-1]
        bl = self.bankloss[c].sum(axis = 1)
        
        sk = {}
        for i in bl.index:
            if bl.loc[i] >= threshold:
                sk[i] = bl.loc[i]
        
        return sk
    
    def finish(self):
        _ = (len(self.infected_bank) + len(self.infected_sup))==0
        # print(len(self.infected_bank),len(self.infected_sup))
        # print(self.infected_bank)
        # print(self.infected_sup)
        return (_ and self.round >=1)
        
    
# def DR_osc(sir, i, level):
        


if __name__ == "__main__":
    from DebtRank import DebtRankContagion
    
    banks, net = gen_banks()
    bankid = list(banks.index)

    supplier_net, sup_corr, sup_attr,_ = biosc(banks, M = 100, k = 1e-4)
    sirc = SIRContagion(banks, supplier_net, sup_corr, sup_attr, supplier_contagion = False)
    # drc = DebtRankContagion(banks, net)
    
    # a,b = sirc.cont_net(True)
    # a.to_csv("G:/gephi_files/sirdr/nodes.csv")
    # b.to_csv("G:/gephi_files/sirdr/edges.csv")
    
    sirc.attack(["s0"],["b1"],level = 1)
    sirc.step()
    


    
    