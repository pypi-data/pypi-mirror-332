# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:46:17 2025

@author: qiyu
"""

import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import norm
import pandas as pd
import networkx as nx
# from matplotlib import rcParams
import statsmodels.api as sm
import altair as alt
from scipy.stats import rankdata
from statsmodels.distributions.copula.api import ClaytonCopula, GumbelCopula, IndependenceCopula, StudentTCopula
from itertools import combinations

# import numpy as np
# import pandas as pd
# from scipy.stats import rankdata
# from statsmodels.distributions.copula.api import ClaytonCopula, GumbelCopula, StudentTCopula, IndependenceCopula

def copula_tail_dependence_graph(data: pd.DataFrame, copula_type="clayton"):
    """
    基于 Copula 模型计算输入 DataFrame 中两两列之间的尾部依赖系数矩阵。

    参数:
        data (pd.DataFrame): 输入数据，行表示样本，列表示变量。
        copula_type (str): 使用的 Copula 类型，可选 "clayton", "gumbel", "student_t", "independence"。
    
    返回:
        tuple: (下尾部依赖系数矩阵, 上尾部依赖系数矩阵)
    """
    # 确保数据中不存在空值
    data = data.dropna()

    # 标准化数据为 U(0, 1)（边际分布）
    u_data = data.apply(lambda col: rankdata(col) / (len(col) + 1), axis=0)

    # 初始化尾部依赖矩阵
    num_cols = data.shape[1]
    lower_tail_matrix = np.zeros((num_cols, num_cols))
    # upper_tail_matrix = np.zeros((num_cols, num_cols))

    # 定义 Copula
    if copula_type.lower() == "clayton":
        copula_model = ClaytonCopula
    # elif copula_type.lower() == "gumbel":
    #     copula_model = GumbelCopula
    # elif copula_type.lower() == "student_t":
    #     copula_model = StudentTCopula
    # elif copula_type.lower() == "independence":
    #     copula_model = IndependenceCopula
    else:
        raise ValueError("Unsupported copula type. Choose from 'clayton', 'gumbel', 'student_t', 'independence'.")

    # 遍历每一对变量组合
    for i, j in combinations(range(num_cols), 2):
        u = u_data.iloc[:, i]
        v = u_data.iloc[:, j]

        # 创建 Copula 实例
        copula = copula_model()

        # 使用 fit_corr_param 拟合 Copula 参数
        uv_data = np.column_stack([u, v])
        theta = copula.fit_corr_param(uv_data)  # 拟合相关参数

        # 计算下尾部和上尾部依赖系数
        lambda_lower = copula.tau(theta) if (theta > 0) else 0
        # lambda_upper = copula.upper_tail_dependence(theta)
# 
        # 存入矩阵
        lower_tail_matrix[i, j] = lambda_lower
        lower_tail_matrix[j, i] = lambda_lower
        # upper_tail_matrix[i, j] = lambda_upper
        # upper_tail_matrix[j, i] = lambda_upper

    # 转换为 DataFrame 格式
    columns = data.columns
    lower_tail_df = pd.DataFrame(lower_tail_matrix, columns=columns, index=columns)
    # upper_tail_df = pd.DataFrame(upper_tail_matrix, columns=columns, index=columns)

    return lower_tail_df

# np.random.seed(42)
# data = pd.DataFrame({
#     "A": np.random.normal(0, 1, 1000),
#     "B": np.random.normal(0, 1, 1000),
#     "C": np.random.normal(0, 1, 1000),
# })

# # 计算尾部依赖矩阵（使用 Clayton Copula）
# lower_matrix = compute_tail_dependence_with_copula(data, copula_type="clayton")

# print("下尾部依赖矩阵:")
# print(lower_matrix)

# sys.exit()


def granger_causality_graph(data, max_lag=5, significance_level=0.05):
    """
    计算两两之间的格兰杰因果关系。
    返回一个邻接矩阵（0 或 1），表示因果关系是否显著。
    
    Parameters:
        data: pandas.DataFrame, 包含时间序列数据
        max_lag: int, 格兰杰因果检验的最大滞后阶数
        significance_level: float, 显著性水平
    
    Returns:
        adjacency_matrix: pandas.DataFrame, 因果关系矩阵（0 或 1）
    """
    companies = data.columns
    n = len(companies)
    adjacency_matrix = pd.DataFrame(0, index=companies, columns=companies)
    
    # 两两公司之间计算格兰杰因果关系
    for i in range(n):
        for j in range(n):
            if i != j:  # 自己与自己之间不计算
                try:
                    test_result = sm.tsa.stattools.grangercausalitytests(
                        data[[companies[j], companies[i]]], max_lag
                    )
                    # 取最小滞后阶数的 P 值
                    p_values = [round(test_result[lag][0]['ssr_chi2test'][1], 4) for lag in range(1, max_lag + 1)]
                    min_p_value = min(p_values)
                    
                    # 如果 P 值小于显著性水平，认为存在因果关系
                    if min_p_value < significance_level:
                        adjacency_matrix.iloc[i, j] = 1
                except Exception as e:
                    print(f"Error processing {companies[j]} -> {companies[i]}: {e}")
    
    return adjacency_matrix

# def plot_granger_graph(adjacency_matrix):
#     rcParams['font.sans-serif'] = ['SimHei']  # 黑体显示中文
#     rcParams['axes.unicode_minus'] = False   # 防止负号显示异常
    
#     # max_lag = 5
#     # significance_level = 0.01
#     # adjacency_matrix = granger_causality(rtdf, max_lag=max_lag, significance_level=significance_level)

#     G = nx.from_pandas_adjacency(adjacency_matrix, create_using=nx.DiGraph)
    
#     # 自定义椭圆布局
#     def elliptical_layout(graph, scale_x=2, scale_y=1):
#         """
#         生成椭圆形布局的节点位置。
        
#         Parameters:
#             graph: networkx.Graph, 输入的网络图
#             scale_x: float, 椭圆的水平伸缩比例
#             scale_y: float, 椭圆的垂直伸缩比例
        
#         Returns:
#             pos: dict, 节点的坐标字典
#         """
#         nodes = list(graph.nodes)
#         n = len(nodes)
#         pos = {}
#         for i, node in enumerate(nodes):
#             angle = 2 * np.pi * i / n  # 每个节点的角度
#             x = scale_x * np.cos(angle)  # 椭圆的 x 坐标
#             y = scale_y * np.sin(angle)  # 椭圆的 y 坐标
#             pos[node] = (x, y)
#         return pos
    
#     # 获取椭圆布局位置
#     pos = elliptical_layout(G, scale_x=3, scale_y=1.5)
    
#     # 绘制网络图
#     plt.figure(figsize=(12, 8))
#     nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
#     nx.draw_networkx_edges(G, pos, edge_color="gray", arrowsize=20)
#     nx.draw_networkx_labels(G, pos, font_size=12, font_color="black")
#     plt.title("上市公司之间的信息溢出网络", fontsize=16)
#     plt.axis('off')  # 关闭坐标轴
#     plt.show()
#     return 
def plot_granger_graph(adjacency_matrix, engine="altair"):
    """
    绘制基于 Granger 因果关系的网络图，支持 Matplotlib 和 Altair 绘图引擎。

    参数:
        adjacency_matrix (pd.DataFrame): Granger 因果关系的邻接矩阵。
        engine (str): 绘图引擎，可选 "matplotlib" 或 "altair"（默认 "matplotlib"）。
    """
    import networkx as nx
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import altair as alt

    # 配置字体以支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体显示中文
    plt.rcParams['axes.unicode_minus'] = False   # 防止负号显示异常

    # 创建有向图
    G = nx.from_pandas_adjacency(adjacency_matrix, create_using=nx.DiGraph)

    # 定义椭圆布局
    def elliptical_layout(graph, scale_x=2, scale_y=1):
        """
        生成椭圆形布局的节点位置。
        
        Parameters:
            graph: networkx.Graph, 输入的网络图
            scale_x: float, 椭圆的水平伸缩比例
            scale_y: float, 椭圆的垂直伸缩比例
        
        Returns:
            pos: dict, 节点的坐标字典
        """
        nodes = list(graph.nodes)
        n = len(nodes)
        pos = {}
        for i, node in enumerate(nodes):
            angle = 2 * np.pi * i / n  # 每个节点的角度
            x = scale_x * np.cos(angle)  # 椭圆的 x 坐标
            y = scale_y * np.sin(angle)  # 椭圆的 y 坐标
            pos[node] = (x, y)
        return pos

    # 使用 Matplotlib 绘图
    if engine == "matplotlib":
        # 获取椭圆布局位置
        pos = elliptical_layout(G, scale_x=3, scale_y=1.5)

        # 绘制网络图
        plt.figure(figsize=(12, 8))
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
        nx.draw_networkx_edges(G, pos, edge_color="gray", arrowsize=20)
        nx.draw_networkx_labels(G, pos, font_size=12, font_color="black")
        plt.title("上市公司之间的信息溢出网络", fontsize=16)
        plt.axis('off')  # 关闭坐标轴
        plt.show()

    # 使用 Altair 绘图
    elif engine == "altair":
        # 获取节点的椭圆布局位置
        pos = elliptical_layout(G, scale_x=3, scale_y=1.5)

        # 构造节点数据框
        nodes_df = pd.DataFrame({
            "node": list(pos.keys()),
            "x": [pos[node][0] for node in pos],
            "y": [pos[node][1] for node in pos],
        })

        # 构造边数据框
        edges_df = pd.DataFrame([
            {"source": u, "target": v}
            for u, v in G.edges
        ])
        edges_df["x_start"] = edges_df["source"].map(lambda node: pos[node][0])
        edges_df["y_start"] = edges_df["source"].map(lambda node: pos[node][1])
        edges_df["x_end"] = edges_df["target"].map(lambda node: pos[node][0])
        edges_df["y_end"] = edges_df["target"].map(lambda node: pos[node][1])

        # 绘制边
        edge_chart = alt.Chart(edges_df).mark_line(stroke="gray", opacity=0.7).encode(
            x="x_start:Q",
            y="y_start:Q",
            x2="x_end:Q",
            y2="y_end:Q"
        )

        # 绘制节点
        node_chart = alt.Chart(nodes_df).mark_circle(size=200, color="skyblue").encode(
            x="x:Q",
            y="y:Q",
            tooltip=["node:N"]  # 鼠标悬停显示节点信息
        )

        # 绘制节点标签
        label_chart = alt.Chart(nodes_df).mark_text(align="center", baseline="middle", fontSize=12).encode(
            x="x:Q",
            y="y:Q",
            text="node:N"
        )

        # 合并图表
        chart = (edge_chart + node_chart + label_chart).properties(
            title="上市公司之间的信息溢出网络",
            width=800,
            height=600
        )

        # 显示 Altair 图表
        chart.save("irf/graph.png")

    else:
        raise ValueError("Unsupported engine. Please choose 'matplotlib' or 'altair'.")


  # VAR 模型估计函数
def _estimate_var(source, target, data, max_lag):
    """
    对给定的两个公司（source -> target）估计 VAR 模型。
    
    Parameters:
        source: str, 源公司名称
        target: str, 目标公司名称
        data: pandas.DataFrame, 时间序列数据
        max_lag: int, 最大滞后阶数
    
    Returns:
        result: dict, 包含滞后阶数和系数矩阵的字典
    """
    try:
        # 选取源和目标公司的数据
        sub_data = data[[source, target]]
        # 建立 VAR 模型
        model = sm.tsa.VAR(sub_data)
        # 根据 AIC/BIC 选择最优滞后阶数
        selected_lag = model.select_order(maxlags=max_lag).aic
        # 拟合模型
        results = model.fit(selected_lag)
        # 提取系数矩阵
        coefficients = results.params.to_dict()  # 转换为字典
        return {"lag": selected_lag, "coefficients": coefficients}
    except Exception as e:
        print(f"Error estimating VAR model for {source} -> {target}: {e}")
        return None

def LocalVAR(data,
             adjacency_matrix,
             max_lag = 5):
    
    # adjacency_matrix = granger_causality_graph(data, max_lag=max_lag, significance_level=significance_level)
    
    # 构建网络
    G = nx.from_pandas_adjacency(adjacency_matrix, create_using=nx.DiGraph)
    
    # 存储每条边信息的列表
    edges_info = []
    
    # 遍历有向边，估计 VAR 模型并存储信息
    for source, target in G.edges:
        var_result = _estimate_var(source, target, data, max_lag=max_lag)
        if var_result:
            edge_data = {
                "source": source,
                "target": target,
                "lag": var_result["lag"],
                "coefficients": var_result["coefficients"]
            }
            edges_info.append(edge_data)
    
    # # 将结果保存为 JSON 格式
    # output_file = "var_model_edges.json"
    # with open(output_file, "w", encoding="utf-8") as f:
    #     json.dump(edges_info, f, ensure_ascii=False, indent=4)
    
    # # 打印 JSON 数据（可选）
    # print(json.dumps(edges_info, ensure_ascii=False, indent=4))
    
    num = len(data.columns)
    names = data.columns
    # data_ = data.iloc[-max_lag:]
    # data_ = data_.reset_index(drop = True)
    # t = data_.index[-1]
    # sigma = data.std(axis = 0)
    
    COEF = []
    for i in range(1, max_lag + 1):
        coef = pd.DataFrame(np.zeros((num, num)), columns=names, index = names)
        
        for e in edges_info:
            if e["lag"] < i:
                continue
            src = e["source"]
            tgt = e["target"]
            eff = e["coefficients"][tgt][f"L{i}.{src}"]
            coef.loc[src][tgt] = eff
        COEF.append(coef)
    # steps = 5
    # for i in range(1,steps+1):
    #     Mean = np.zeros(num)
    #     ct = t+i
    #     for s in range(1, max_lag + 1):
    #         tt = ct-s
    #         x = data_.loc[tt]
    #         A = COEF[s]
    #         v = x @ A
    #         Mean += v
        
    #     di = Mean + np.random.randn(num) * sigma
    #     data_.loc[ct] = di
    return np.array(COEF)


from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler

def LassoVAR(data, max_lag=5, alpha_values=None, cv=5):
    """
    使用 Lasso 方法估计 VAR 模型。

    参数:
        data (pd.DataFrame): 输入数据，行表示时间，列表示变量（如公司或股票）。
        max_lag (int): 最大滞后阶数。
        alpha_values (list or np.array): Lasso 的正则化参数候选值。如果为 None，自动选择。
        cv (int): 交叉验证的折数，用于选择最佳正则化参数。
    
    返回:
        coefficients (np.array): 估计的系数矩阵，形状为 (max_lag, n_features, n_features)。
        intercepts (np.array): 每个回归方程的截距项，形状为 (n_features,)。
        best_alphas (np.array): 每个变量的最佳正则化参数。
    """
    # 检查输入数据有效性
    if not isinstance(data, pd.DataFrame):
        raise ValueError("输入数据必须是 pd.DataFrame")
    
    # 数据形状
    n_time, n_features = data.shape

    if n_time <= max_lag:
        raise ValueError("时间序列长度必须大于最大滞后阶数 max_lag")
    
    # 构造滞后变量矩阵
    lagged_data = []
    for lag in range(1, max_lag + 1):
        lagged_data.append(data.shift(lag))
    lagged_data = pd.concat(lagged_data, axis=1)

    # 移除 NaN 行（由于滞后导致的）
    lagged_data = lagged_data.iloc[max_lag:]
    target_data = data.iloc[max_lag:]

    # 将数据从 DataFrame 转换为 NumPy 数组
    X = lagged_data.values  # 自变量（滞后项）
    Y = target_data.values  # 因变量（当前值）

    # 标准化 X（对滞后项进行标准化）
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 存储结果
    coefficients = np.zeros((max_lag, n_features, n_features))
    intercepts = np.zeros((n_features,))
    best_alphas = np.zeros((n_features,))

    # 针对每个目标变量（每列）单独回归
    for i in range(n_features):
        # 当前的目标变量
        y_i = Y[:, i]

        # 使用 LassoCV 自动选择正则化参数（alpha）
        lasso = LassoCV(alphas=alpha_values, cv=cv, random_state=0).fit(X, y_i)

        # 提取截距和系数
        intercepts[i] = lasso.intercept_
        best_alphas[i] = lasso.alpha_

        # 将系数分配到对应的滞后阶数
        coef_i = lasso.coef_.reshape(max_lag, n_features)
        coefficients[:, i, :] = coef_i

    return coefficients, intercepts, best_alphas




# def impulse_response_function(coefficients, X, cov_matrix, shock, horizon, confidence=0.95, n_simulations=1000):
#     """
#     计算VAR模型的脉冲响应函数。

#     参数:
#         coefficients (np.array): VAR模型的系数矩阵，形状为 (n_lag, n_feature, n_feature)。
#         X (np.array): 历史状态矩阵，形状为 (n_lag, n_feature)，按时间顺序。
#         cov_matrix (np.array): 残差的协方差矩阵，形状为 (n_feature, n_feature)，假设是对角阵。
#         shock (np.array): 冲击向量，形状为 (n_feature,)。
#         horizon (int): 分析的时间步长（脉冲响应的范围）。
#         confidence (float): 置信度（默认 0.95）。
#         n_simulations (int): 用于蒙特卡罗模拟的样本数量。

#     返回:
#         irf_mean (np.array): 脉冲响应的均值，形状为 (horizon, n_feature)。
#         irf_lower (np.array): 置信区间的下界，形状为 (horizon, n_feature)。
#         irf_upper (np.array): 置信区间的上界，形状为 (horizon, n_feature)。
#     """
#     n_lag, n_feature, _ = coefficients.shape
    
#     # 初始化脉冲响应
#     irf_mean = np.zeros((horizon, n_feature))
#     irf_simulations = np.zeros((n_simulations, horizon, n_feature))
    
#     # 初始化当前状态
#     current_state = X.copy()
    
#     # 填充初始冲击
#     current_response = np.zeros((n_feature,))
#     current_response += shock  # 添加冲击
    
#     # 模拟脉冲响应的均值
#     for t in range(horizon):
#         irf_mean[t] = current_response
        
#         # 更新历史状态
#         current_state = np.roll(current_state, shift=-1, axis=0)
#         current_state[-1] = current_response
        
#         # 更新下一步状态
#         next_state = np.zeros((n_feature,))
#         for lag in range(n_lag):
#             next_state += current_state[-(lag + 1)] @ coefficients[lag] 
#         current_response = next_state
        
#     # 模拟置信区间（蒙特卡罗模拟）
#     for i in range(n_simulations):
#         current_state = X.copy()
#         current_response = np.zeros((n_feature,))
#         current_response += shock  # 初始冲击

#         for t in range(horizon):
#             irf_simulations[i, t] = current_response
            
#             # 更新历史状态
#             current_state = np.roll(current_state, shift=-1, axis=0)
#             current_state[-1] = current_response

#             # 更新下一步状态
#             next_state = np.zeros((n_feature,))
#             for lag in range(n_lag):
#                 next_state += current_state[-(lag + 1)] @ coefficients[lag] 
            
#             # 添加随机扰动
#             noise = np.random.multivariate_normal(mean=np.zeros(n_feature), cov=cov_matrix)
#             current_response = next_state + noise

#     # 计算置信区间
#     alpha = 1 - confidence
#     lower_quantile = alpha / 2
#     upper_quantile = 1 - alpha / 2

#     irf_lower = np.percentile(irf_simulations, lower_quantile * 100, axis=0)
#     irf_upper = np.percentile(irf_simulations, upper_quantile * 100, axis=0)

#     return irf_mean, irf_lower, irf_upper

def impulse_response_function(coefficients, X=None, cov_matrix=None, shock=None, horizon=10, confidence=0.95, n_simulations=1000):
    """
    计算VAR模型的脉冲响应函数。

    参数:
        coefficients (np.array): VAR模型的系数矩阵，形状为 (n_lag, n_feature, n_feature)。
        X (np.array): 历史状态矩阵，形状为 (n_lag, n_feature)，按时间顺序。如果为 None，默认为零矩阵。
        cov_matrix (np.array): 残差的协方差矩阵，形状为 (n_feature, n_feature)，假设是正定矩阵。
        shock (np.array): 冲击向量，形状为 (n_feature,)。
        horizon (int): 分析的时间步长（脉冲响应的范围）。
        confidence (float): 置信度（默认 0.95）。
        n_simulations (int): 用于蒙特卡罗模拟的样本数量。

    返回:
        irf_mean (np.array): 脉冲响应的均值，形状为 (horizon, n_feature)。
        irf_lower (np.array): 置信区间的下界，形状为 (horizon, n_feature)。
        irf_upper (np.array): 置信区间的上界，形状为 (horizon, n_feature)。
    """
    # 确定滞后阶数和特征数量
    n_lag, n_feature, _ = coefficients.shape

    # 如果 X 是 None，初始化为零矩阵
    if X is None:
        X = np.zeros((n_lag, n_feature))
    
    # 检查冲击向量是否提供
    if shock is None:
        raise ValueError("必须提供冲击向量 shock")
    
    # 检查协方差矩阵是否提供
    if cov_matrix is None:
        raise ValueError("必须提供协方差矩阵 cov_matrix")
    
    # 初始化模拟存储矩阵
    irf_simulations = np.zeros((n_simulations, horizon, n_feature))
    
    # 蒙特卡罗模拟
    for i in range(n_simulations):
        # 当前状态初始化
        current_state = X.copy()
        current_response = np.zeros((n_feature,))
        current_response += shock  # 初始冲击
        
        # 模拟脉冲响应
        for t in range(horizon):
            # 添加随机扰动
            noise = np.random.multivariate_normal(mean=np.zeros(n_feature), cov=cov_matrix)
            current_response = current_response + noise

            irf_simulations[i, t] = current_response
            
            # 更新历史状态
            current_state = np.roll(current_state, shift=-1, axis=0)
            current_state[-1] = current_response
            
            # 更新下一步状态
            current_response = np.zeros((n_feature,))
            for lag in range(n_lag):
                current_response += current_state[-(lag + 1)] @ coefficients[lag]
            

    # 计算均值
    irf_mean = np.mean(irf_simulations, axis=0)
    
    # 计算置信区间
    alpha = 1 - confidence
    lower_quantile = alpha / 2
    upper_quantile = 1 - alpha / 2
    irf_lower = np.percentile(irf_simulations, lower_quantile * 100, axis=0)
    irf_upper = np.percentile(irf_simulations, upper_quantile * 100, axis=0)

    return irf_mean, irf_lower, irf_upper



# def plot_single_impulse_response(mean, lower, upper, horizon, shock_name, response_name, history=None):
#     """
#     绘制单个变量对的脉冲响应，同时支持绘制历史步，并以不同颜色区分历史和预测数据。
#     历史和预测数据通过一条线自然连接。

#     参数:
#         mean (np.array): 脉冲响应的均值，形状为 (horizon,)。
#         lower (np.array): 置信区间的下界，形状为 (horizon,)。
#         upper (np.array): 置信区间的上界，形状为 (horizon,)。
#         horizon (int): 时间步长（脉冲响应的预测范围）。
#         shock_name (str): 冲击变量的名称。
#         response_name (str): 响应变量的名称。
#         history (np.array, optional): 历史响应数据，形状为 (history_len,)。
#             如果提供，将在图中以不同颜色绘制历史数据，并连接历史与预测。
#     """
#     plt.figure(figsize=(8, 4))
    
#     # 如果提供了历史数据
#     if history is not None:
#         history_len = len(history)
        
#         # 横轴范围
#         history_times = range(-history_len, 0)  # 历史部分的时间点
#         prediction_times = range(horizon)      # 预测部分的时间点

#         # 绘制历史数据（橙色）
#         plt.plot(history_times, history, label="Historical Data", color="orange", lw=2, linestyle="--")

#         # 绘制连接点（历史的最后一个点与预测的第一个点）
#         plt.plot([history_times[-1], prediction_times[0]],
#                  [history[-1], mean[0]], color="orange", lw=2, linestyle="--")

#         # 绘制预测数据（蓝色）
#         plt.plot(prediction_times, mean, label="Impulse Response (Prediction)", color="blue", lw=2)
        
#         # 填充置信区间（仅绘制预测部分）
#         plt.fill_between(prediction_times, lower, upper, color="blue", alpha=0.3, label="Confidence Interval")
        
#     else:
#         # 如果没有历史数据，直接绘制预测数据
#         prediction_times = range(horizon)
#         plt.plot(prediction_times, mean, label="Impulse Response (Prediction)", color="blue", lw=2)
#         plt.fill_between(prediction_times, lower, upper, color="blue", alpha=0.3, label="Confidence Interval")

#     # 水平线，表示零响应
#     plt.axhline(0, color="black", linestyle="--", linewidth=0.8)

#     # 图表标题和标签
#     plt.title(f"Impulse Response: {shock_name} → {response_name}", fontsize=14)
#     plt.xlabel("Time (Horizon)", fontsize=12)
#     plt.ylabel("Response", fontsize=12)

#     # 图例
#     plt.legend()

#     # 网格与布局
#     plt.grid()
#     plt.tight_layout()

#     # 显示图表
#     plt.show()
    



def plot_single_impulse_response(
    mean, lower, upper, horizon, shock_name, response_name, history=None, engine="altair"
):
    """
    绘制单个变量对的脉冲响应，同时支持绘制历史步，并以不同颜色区分历史和预测数据。
    历史和预测数据通过一条线自然连接，并在时间为 0 的位置添加红色标注。

    参数:
        mean (np.array): 脉冲响应的均值，形状为 (horizon,)。
        lower (np.array): 置信区间的下界，形状为 (horizon,)。
        upper (np.array): 置信区间的上界，形状为 (horizon,)。
        horizon (int): 时间步长（脉冲响应的预测范围）。
        shock_name (str): 冲击变量的名称。
        response_name (str): 响应变量的名称。
        history (np.array, optional): 历史响应数据，形状为 (history_len,)。
            如果提供，将在图中以不同颜色绘制历史数据，并连接历史与预测。
        engine (str): 绘图引擎，可选 "matplotlib" 或 "altair"（默认 "altair"）。
    """
    title = f"Impulse Response {shock_name} to {response_name}"
    if engine == "matplotlib":
        # 使用 matplotlib 绘图
        plt.figure(figsize=(8, 4))

        # 如果提供了历史数据
        if history is not None:
            history_len = len(history)

            # 横轴范围
            history_times = range(-history_len, 0)  # 历史部分的时间点
            prediction_times = range(horizon)      # 预测部分的时间点

            # 绘制历史数据（橙色）
            plt.plot(history_times, history, label="Historical Data", color="orange", lw=2, linestyle="--")

            # 绘制连接点（历史的最后一个点与预测的第一个点）
            plt.plot([history_times[-1], prediction_times[0]],
                     [history[-1], mean[0]], color="orange", lw=2, linestyle="--")

            # 绘制预测数据（蓝色）
            plt.plot(prediction_times, mean, label="Impulse Response (Prediction)", color="blue", lw=2)

            # 填充置信区间（仅绘制预测部分）
            plt.fill_between(prediction_times, lower, upper, color="blue", alpha=0.3, label="Confidence Interval")

        else:
            # 如果没有历史数据，直接绘制预测数据
            prediction_times = range(horizon)
            plt.plot(prediction_times, mean, label="Impulse Response (Prediction)", color="blue", lw=2)
            plt.fill_between(prediction_times, lower, upper, color="blue", alpha=0.3, label="Confidence Interval")

        # 水平线，表示零响应
        plt.axhline(0, color="black", linestyle="--", linewidth=0.8)

        # 添加红色向下箭头和文字标注
        plt.annotate("Attack", xy=(0, 0), xytext=(0, max(mean)*0.5),
                     arrowprops=dict(facecolor='red', shrink=0.05),
                     fontsize=12, color="red", ha='center')

        # 图表标题和标签
        plt.title(title, fontsize=14)
        plt.xlabel("Time (Horizon)", fontsize=12)
        plt.ylabel("Response", fontsize=12)

        # 图例
        plt.legend()

        # 网格与布局
        plt.grid()
        plt.tight_layout()

        # 显示图表
        plt.show()

    elif engine == "altair":
        # 构造历史数据表（包含预测的第一个点）
        if history is not None:
            history_len = len(history)
            history_time = np.arange(-history_len, 1)  # 历史时间点，含预测的第一个点
            history_response = np.append(history, mean[0])  # 添加预测的第一个点
            history_data = pd.DataFrame({
                "Time": history_time,
                "Response": history_response,
                "Type": ["Historical"] * (history_len + 1),
            })
        else:
            history_data = pd.DataFrame(columns=["Time", "Response", "Type"])  # 空历史数据表

        # 构造预测数据表（从第一个点开始）
        prediction_time = np.arange(horizon)
        prediction_response = mean
        pred_data = pd.DataFrame({
            "Time": prediction_time,
            "Response": prediction_response,
            "Type": ["Prediction"] * horizon,
        })

        # 构造置信区间表（只包含预测部分）
        ci_data = pd.DataFrame({
            "Time": prediction_time,
            "Lower": lower,
            "Upper": upper,
        })

        # 绘制历史数据线条
        history_line = alt.Chart(history_data).mark_line(color="orange", strokeDash=[4, 2]).encode(
            x=alt.X("Time:Q", title="Time (Horizon)"),
            y=alt.Y("Response:Q", title="Response"),
            tooltip=["Time", "Response"]
        )

        # 绘制预测数据线条
        prediction_line = alt.Chart(pred_data).mark_line(color="blue").encode(
            x=alt.X("Time:Q"),
            y=alt.Y("Response:Q"),
            tooltip=["Time", "Response"]
        )

        # 绘制置信区间带
        confidence_band = alt.Chart(ci_data).mark_area(opacity=0.3, color="blue").encode(
            x=alt.X("Time:Q"),
            y=alt.Y("Lower:Q"),
            y2=alt.Y2("Upper:Q"),
        )

        # 添加红色向下箭头标注
        annotation_data = pd.DataFrame({
            "Time": [0],
            "Response": [0],
            "Text": ["Attack"]
        })

        arrow = alt.Chart(annotation_data).mark_point(shape="triangle-down", size=200, color="red").encode(
            x="Time:Q",
            y="Response:Q"
        )

        annotation_text = alt.Chart(annotation_data).mark_text(
            align="center", baseline="bottom", dy=-10, color="red", fontSize=12
        ).encode(
            x="Time:Q",
            y="Response:Q",
            text="Text:N"
        )

        # 水平线表示零响应
        zero_line = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(strokeDash=[4, 4], color="black").encode(y="y:Q")

        # 合并图表
        chart = (confidence_band + history_line + prediction_line + zero_line + arrow + annotation_text).properties(
            title=title,
            width=800,
            height=400
        )

        # 保存图表为图片（如果需要）
        chart.save(f"irf/{title}.png")
        return chart

    else:
        raise ValueError("Unsupported engine. Please choose 'matplotlib' or 'altair'.")

def plot_coshock_chart(coshock, feature_names):
    """
    使用 Altair 绘制柱状图。

    参数:
        data (list or np.array): 一维数组，包含数值数据。
        feature_names (list): 特征名称列表，长度应与 data 相同。

    返回:
        alt.Chart: 绘制的柱状图。
    """

    
    if len(coshock) != len(feature_names):
        raise ValueError("数据和特征名称的长度必须相同。")

    # 创建 DataFrame
    df = pd.DataFrame({
        '银行': feature_names,
        '冲击': coshock
    })

    # 使用 Altair 创建柱状图
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('银行', sort=None),  # 保持特征顺序
        y='冲击',
        tooltip=['银行', '冲击']   # 添加悬停提示
    ).properties(
        title='共同冲击',
        width=400,    # 图表宽度
        height=200    # 图表高度
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    )

    return chart


def plot_coshock_impulse_responses(coefficients, X, cov_matrix, granger_graph, rho,shock_idx, shock_scale, feature_names, 
                                    horizon=10, confidence=0.95, n_simulations=1000):
    """
    循环计算并绘制所有变量对的脉冲响应图。

    参数:
        coefficients (np.array): 模型的系数矩阵。
        X (np.array): 当前状态变量。
        cov_matrix (np.array): 协方差矩阵，用于随机误差模拟。
        rho: 相关系数矩阵，用来算共同冲击
        shock_names (list): 冲击变量的名称。
        response_names (list): 响应变量的名称。
        horizon (int): 时间步长，脉冲响应的预测范围。
        confidence (float): 置信水平，用于计算置信区间。
        n_simulations (int): 用于生成置信区间的模拟次数。
    """
    
    n_features = len(feature_names)
    shock = rho[shock_idx] * shock_scale
    mean, lower, upper = impulse_response_function(
        coefficients, X, cov_matrix, shock, horizon, confidence, n_simulations)
    shock_name = feature_names[shock_idx]
    for response_idx in range(n_features):
        # 获取冲击和响应变量的名称
        response_name = feature_names[response_idx]
        # 调用绘图函数
        plot_single_impulse_response(mean[:,response_idx], 
                                     lower[:,response_idx], 
                                     upper[:,response_idx], 
                                     horizon, shock_name, response_name,
                                     X[:,response_idx])
        
def plot_indepshock_impulse_responses(coefficients, X, cov_matrix, granger_graph, shock_idx, shock_scale, feature_names, 
                                    horizon=10, confidence=0.95, n_simulations=1000):
    """
    循环计算并绘制所有变量对的脉冲响应图。

    参数:
        coefficients (np.array): 模型的系数矩阵。
        X (np.array): 当前状态变量。
        cov_matrix (np.array): 协方差矩阵，用于随机误差模拟。
        rho: 相关系数矩阵，用来算共同冲击
        shock_names (list): 冲击变量的名称。
        response_names (list): 响应变量的名称。
        horizon (int): 时间步长，脉冲响应的预测范围。
        confidence (float): 置信水平，用于计算置信区间。
        n_simulations (int): 用于生成置信区间的模拟次数。
    """
    
    n_features = len(feature_names)
    shock = np.zeros(n_features)
    shock[shock_idx] = shock_scale
    mean, lower, upper = impulse_response_function(
        coefficients, X, cov_matrix, shock, horizon, confidence, n_simulations)
    shock_name = feature_names[shock_idx]
    for response_idx in range(n_features):
        # 获取冲击和响应变量的名称
        response_name = feature_names[response_idx]
        # 调用绘图函数
        plot_single_impulse_response(mean[:,response_idx], 
                                     lower[:,response_idx], 
                                     upper[:,response_idx], 
                                     horizon, shock_name, response_name,
                                     X[:,response_idx])

# def plot_indepshock_impulse_responses_all(coefficients, X, cov_matrix, granger_graph,feature_names,
#                                     horizon=10, confidence=0.95, n_simulations=1000, shocks = None):
#     """
#     独立shock
#     即一次只影响一家公司
#     循环计算并绘制所有变量对的脉冲响应图。

#     参数:
#         coefficients (np.array): 模型的系数矩阵。
#         X (np.array): 当前状态变量。
#         cov_matrix (np.array): 协方差矩阵，用于随机误差模拟。
#         shock_names (list): 冲击变量的名称。
#         response_names (list): 响应变量的名称。
#         horizon (int): 时间步长，脉冲响应的预测范围。
#         confidence (float): 置信水平，用于计算置信区间。
#         n_simulations (int): 用于生成置信区间的模拟次数。
#     """
    
#     shock_names = feature_names
#     response_names = feature_names
#     n_features = len(shock_names)

#     for shock_idx in range(n_features):
#         for response_idx in range(n_features):
#             if granger_graph[shock_idx, response_idx] == 0:
#                 continue
#             # 构造冲击向量（仅对 shock_idx 变量施加冲击）
#             shock = np.zeros(n_features)
#             if shocks is None:
#                 shock[shock_idx] = -1  # 对第 shock_idx 个变量施加单位冲击
#             else:
#                 shock[shock_idx] = shocks[shock_idx]
#             # 调用脉冲响应函数，计算当前变量对的响应
#             mean, lower, upper = impulse_response_function(
#                 coefficients, X, cov_matrix, shock, horizon, confidence, n_simulations
#             )

#             # 获取冲击和响应变量的名称
#             shock_name = shock_names[shock_idx]
#             response_name = response_names[response_idx]

#             # 调用绘图函数
#             plot_single_impulse_response(mean[:,response_idx], 
#                                          lower[:,response_idx], 
#                                          upper[:,response_idx], 
#                                          horizon, shock_name, response_name,
#                                          X[:,response_idx])

def plot_weighted_impulse_responses(coefficients, X, cov_matrix, shock, shock_name,
                                    weight, horizon=10, confidence=0.95,
                                    n_simulations=1000, weight_norm = True):
    """
    循环计算并绘制所有变量对的脉冲响应图。

    参数:
        coefficients (np.array): 模型的系数矩阵。
        X (np.array): 当前状态变量。
        cov_matrix (np.array): 协方差矩阵，用于随机误差模拟。
        shock_names (list): 冲击变量的名称。
        response_names (list): 响应变量的名称。
        weight (list): 变量的权重
        impulse_response_function (function): 脉冲响应计算的核心函数。
        horizon (int): 时间步长，脉冲响应的预测范围。
        confidence (float): 置信水平，用于计算置信区间。
        n_simulations (int): 用于生成置信区间的模拟次数。
    """
    n_features = len(shock)
    weight = np.array(weight).reshape(n_features,1)
    if weight_norm:
        weight = weight/np.sum(weight)

    # 调用脉冲响应函数，计算当前变量对的响应
    mean, lower, upper = impulse_response_function(
        coefficients, X, cov_matrix, shock, horizon, confidence, n_simulations)

    plot_single_impulse_response((mean @ weight).reshape(-1), 
                                 (lower @ weight).reshape(-1),
                                 (upper @ weight).reshape(-1),
                                 horizon, 
                                 shock_name, 
                                 "market",
                                 (X @ weight).reshape(-1))

    return 






# 示例使用
if __name__ == "__main__":
    # 假设模型参数（以下为随机生成的示例数据）
    n_lag = 3
    n_features = 3
    horizon = 10
    confidence = 0.95
    n_simulations = 10000
    
    # 模拟系数矩阵和历史状态
    coefficients = np.random.rand(n_lag, n_features, n_features) * 0.1
    granger_graph = np.random.randint(0,2,size = (n_features, n_features))
    coefficients[0] = coefficients[0] * granger_graph
    coefficients[1] = coefficients[1] * granger_graph
    X = np.random.randn(n_lag, n_features)
    cov_matrix = np.diag([0.1, 0.2, 0.3])
    shock = np.array([-1.0, 0.0, 0.0])  # 冲击向量
    print(granger_graph)
    # 变量名称
    shock_names = ["GDP", "Interest Rate", "Inflation"]
    response_names = ["GDP", "Interest Rate", "Inflation"]
    
    mean, lower, upper = impulse_response_function(
        coefficients, X, cov_matrix, shock, horizon, confidence, n_simulations)

    # 打印结果
    print("脉冲响应均值：")
    print(mean)
    print("\n置信区间下界：")
    print(lower)
    print("\n置信区间上界：")
    print(upper)
     
    
    plot_single_impulse_response(mean[:,0], lower[:,0], upper[:,0], 10, "t", "a")
    
    # plot_variable_impulse_responses(coefficients, X, cov_matrix, granger_graph,shock_names,
    #                                 horizon=10, confidence=0.95, n_simulations=1000, shocks=[-1,-1.2,-3])
    
    
    
    
    
    
    
    
    
    
    