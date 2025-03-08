# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:00:03 2025

@author: qiyu
"""

import networkx as nx
import pandas as pd

def calculate_centrality(graph):
    """
    计算图的中心性指标，包括：
    - 度中心性
    - 介数中心性
    - 特征向量中心性
    - PageRank中心性

    参数：
    graph: 输入图，可以是 NetworkX 图对象（nx.Graph 或 nx.DiGraph），也可以是 Pandas DataFrame 邻接矩阵。

    返回：
    DataFrame，其中每一行表示一个节点，每列表示该节点的中心性指标。
    """

    # 如果输入是 Pandas DataFrame，则将其转换为 NetworkX 图
    if isinstance(graph, pd.DataFrame):
        if (graph.values != graph.values.T).any():
            # 如果邻接矩阵不对称，创建有向图
            G = nx.from_pandas_adjacency(graph, create_using=nx.DiGraph)
        else:
            # 对称邻接矩阵，创建无向图
            G = nx.from_pandas_adjacency(graph)
    elif isinstance(graph, (nx.Graph, nx.DiGraph)):
        G = graph
    else:
        raise ValueError("输入必须是 NetworkX 图对象或 Pandas DataFrame 邻接矩阵")

    # 判断是有向图还是无向图
    is_directed = G.is_directed()

    # 计算中心性指标
    degree_centrality = nx.degree_centrality(G)  # 度中心性
    betweenness_centrality = nx.betweenness_centrality(G)  # 介数中心性
    eigenvector_centrality = nx.eigenvector_centrality_numpy(G)  # 特征向量中心性
    pagerank_centrality = nx.pagerank(G)  # PageRank 中心性

    # 将结果整理为 Pandas DataFrame
    centrality_df = pd.DataFrame({
        'node': list(degree_centrality.keys()),  # 节点名称
        'degree_centrality': list(degree_centrality.values()),
        'betweenness_centrality': list(betweenness_centrality.values()),
        'eigenvector_centrality': list(eigenvector_centrality.values()),
        'pagerank_centrality': list(pagerank_centrality.values()),
    })

    # 将节点名称设置为 DataFrame 索引
    centrality_df.set_index('node', inplace=True)

    return centrality_df

# 示例用法
if __name__ == "__main__":
    # 示例 1：NetworkX 图对象
    G = nx.karate_club_graph()  # 空手道俱乐部图（无向图）
    print(calculate_centrality(G))

    # 示例 2：Pandas DataFrame 邻接矩阵（有向图）
    adjacency_matrix = pd.DataFrame({
        0: [0, 1, 0, 0],
        1: [0, 0, 1, 1],
        2: [1, 0, 0, 0],
        3: [0, 0, 1, 0]
    })
    print(calculate_centrality(adjacency_matrix))
