# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:57:09 2024

@author: qiyu
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

# matplotlib其实是不支持显示中文的 显示中文需要一行代码设置字体
mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）


# def setaxticks(ax, span=4, rotation = 60, fontsize = 20):
#     xt = ax.get_xticks()
#     xticks = ax.get_xticklabels()
#     xt_ = []
#     xtks_ = []
#     for i,x in enumerate(xticks):
#         if i%span != 0:
#             xticks[i] = ''
#         else:
#             xticks[i] = x.get_text()#[:10]
#     ax.set_xticklabels(xticks, rotation=rotation, fontsize = fontsize)
#     return ax
def setaxticks(ax, span=4, rotation = 60, fontsize = 20):
    xt = ax.get_xticks()
    xticks = ax.get_xticklabels()
    xt_ = []
    xtks_ = []
    for i,x in enumerate(xticks):
        if i%span == 0:
            xt_.append(xt[i])
            xtks_.append(xticks[i])
    ax.set_xticks(xt_)
    ax.set_xticklabels(xtks_, rotation=rotation, fontsize = fontsize)
    return ax




def heatmap(ax, x1, x2, y):
    # 生成网格数据进行插值
    grid_x1, grid_x2 = np.mgrid[min(x1):max(x1):100j, min(x2):max(x2):100j]
    grid_y = griddata((x1, x2), y, (grid_x1, grid_x2), method='cubic')
    
    # 创建热力图
    cont = ax.contourf(grid_x1, grid_x2, grid_y, levels=100, cmap='viridis')
    cbar = plt.colorbar(cont, ax=ax, label='Interpolated f(x1, x2)')
    
    # 添加标题和标签
    ax.set_title('Heatmap of Interpolated y = f(x1, x2)')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    
    return ax


def heatmap_cub(ax, x1, x2, y, x_lim=None, y_lim=None, method='gaussian'):
    # 如果x_lim或y_lim未提供，使用数据的范围
    if x_lim is None:
        x_lim = (min(x1), max(x1))
    if y_lim is None:
        y_lim = (min(x2), max(x2))
    
    # 在给定的x_lim和y_lim范围内生成网格数据
    grid_x1, grid_x2 = np.mgrid[x_lim[0]:x_lim[1]:100j, y_lim[0]:y_lim[1]:100j]
    
    # 初始化插值网格
    grid_y = np.zeros(grid_x1.shape)
    
    # 遍历网格每个点进行加权计算
    for i in range(grid_x1.shape[0]):
        for j in range(grid_x1.shape[1]):
            # 当前网格点坐标
            point = np.array([grid_x1[i, j], grid_x2[i, j]])
            
            # 计算权重，根据距离和选择的核函数
            if method == 'gaussian':
                # 使用高斯核
                distances = np.linalg.norm(np.vstack([x1, x2]).T - point, axis=1)
                weights = np.exp(-0.5 * (distances ** 2))
            else:
                # 使用距离的反比作为权重
                distances = np.linalg.norm(np.vstack([x1, x2]).T - point, axis=1)
                weights = 1 / (distances + 1e-5)  # 防止除以零

            # 进行加权平均
            grid_y[i, j] = np.sum(weights * y) / np.sum(weights)

    # 创建热力图
    cont = ax.contourf(grid_x1, grid_x2, grid_y, levels=100, cmap='viridis')
    cbar = plt.colorbar(cont, ax=ax, label='Weighted y = f(x1, x2)')
    
    # 添加标题和标签
    ax.set_title('Heatmap with Weighted Interpolation')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    
    return ax

def plot_matchstick(ax, timestamps, values,
                    threshold = np.inf, fontsize=15, grid = True,
                    alpha = 0.5):
    """
    在指定的 ax 上绘制火柴线图

    参数：
    ax (matplotlib.axes.Axes): 用于绘制的子图对象
    timestamps (list or array-like): 时间戳数据
    values (list or array-like): 值数据
    threshold (float): 阈值，超过该值的点将显示为红色
    fontsize (int): 字体大小，默认 15
    """
    ax.set_prop_cycle(color=['gray', 'black', 'red'])  # 设置颜色循环

    for t, v in zip(timestamps, values):
        # 绘制从0到数据点的线
        ax.plot([t, t], [0, v], color='gray', linestyle='-', linewidth=1, alpha = alpha)
        
        # 根据阈值条件设置标记颜色
        marker_color = 'red' if v > threshold else 'blue'
        
        # 绘制数据点
        ax.plot(t, v, marker='o', color=marker_color, alpha = alpha)
    
    # 设置标题和标签
    # ax.set_title('Matchstick Plot', fontsize=fontsize)
    # ax.set_xlabel('Timestamp', fontsize=fontsize)
    # ax.set_ylabel('Value', fontsize=fontsize)
    
    # 显示网格
    ax.grid(grid)
    return ax


def export_to_gephi(graph, pth = ".", label = "default", node_categories=None):
    """
    将图（可以是 DataFrame 邻接矩阵或 NetworkX 图对象）导出为 Gephi 支持的 CSV 格式文件，包含节点和边文件，并支持节点类别分类。

    参数：
        graph (pd.DataFrame 或 networkx.Graph): 图数据，可为 DataFrame 邻接矩阵或 NetworkX 图对象。
        pth (str): 输出文件的目录路径。
        label (str): 文件名中的标识标签。
        node_categories (dict, optional): 节点类别字典，键为节点，值为类别（如 {'A': 'type1', 'B': 'type2'}）。
        
    输出：
        - 节点文件 (label_nodes.csv)
        - 边文件 (label_edges.csv)
    """
    # 如果输入是邻接矩阵（DataFrame 格式）
    if isinstance(graph, pd.DataFrame):
        if graph is None or graph.empty:
            print("邻接矩阵为空，无法导出！")
            return
        # 根据邻接矩阵是否为对称矩阵判断是无向图还是有向图
        if (graph != graph.T).any().any():
            graph = nx.from_pandas_adjacency(graph, create_using=nx.DiGraph)
            graph_type = "directed"
        else:
            graph = nx.from_pandas_adjacency(graph, create_using=nx.Graph)
            graph_type = "undirected"
    # 如果输入是 NetworkX 图
    elif isinstance(graph, nx.Graph):
        if graph is None or len(graph.nodes) == 0:
            print("图为空，无法导出！")
            return
        graph_type = "directed" if graph.is_directed() else "undirected"
    else:
        print("输入类型不支持，请传入 DataFrame 邻接矩阵或 NetworkX 图对象！")
        return

    # 创建节点 DataFrame
    nodes_data = pd.DataFrame({
        'Id': list(graph.nodes),  # 节点 ID
        'Label': [str(node) for node in graph.nodes]  # 节点标签
    })

    # 如果提供了节点类别信息，将其加入到节点文件中
    if node_categories:
        nodes_data['Category'] = nodes_data['Id'].map(node_categories)
    else:
        nodes_data['Category'] = None  # 如果没有提供类别信息，则默认为空

    # 创建边 DataFrame
    edges_data = pd.DataFrame({
        'source': [u for u, v in graph.edges],  # 边的起点
        'target': [v for u, v in graph.edges],  # 边的终点
        'Type': [graph_type] * len(graph.edges),  # 边的类型（directed 或 undirected）
        'weight': [graph[u][v].get('weight', 1) for u, v in graph.edges]  # 边权重，默认值为 1
    })

    # 保存为 CSV 文件
    nodes_file = pth + f"/{label}_nodes.csv"
    edges_file = pth + f"/{label}_edges.csv"
    
    nodes_data.to_csv(nodes_file, index=False)
    edges_data.to_csv(edges_file, index=False)
    
    print(f"节点文件已保存到: {nodes_file}")
    print(f"边文件已保存到: {edges_file}")


# 示例用法
if __name__ == "__main__":
    # 创建测试邻接矩阵（有向图）
    data = {
        1: {1: 0, 2: 3, 3: 0},
        2: {1: 0, 2: 0, 3: 5},
        3: {1: 1, 2: 0, 3: 0},
    }
    adj_matrix_directed = pd.DataFrame(data)

    # 定义节点类别
    node_categories = {
        1: 'CategoryA',
        2: 'CategoryB',
        3: 'CategoryC'
    }

    # 导出为 Gephi 文件格式（输入为 DataFrame）
    export_to_gephi(adj_matrix_directed, "./output", "directed_example", node_categories)

    # 创建测试无向图
    G = nx.Graph()
    G.add_edge('A', 'B', weight=2)
    G.add_edge('B', 'C', weight=3)
    G.add_edge('A', 'C', weight=1)

    # 定义无向图的节点类别
    node_categories_undirected = {
        'A': 'Group1',
        'B': 'Group2',
        'C': 'Group1'
    }

    # 导出为 Gephi 文件格式（输入为 NetworkX 图）
    export_to_gephi(G, "./output", "undirected_example", node_categories_undirected)
