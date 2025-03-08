import networkx as nx
import community as community_louvain
import random
import matplotlib.pyplot as plt



def BA_graph(m0, n):
    # 创建一个空的无向图
    G = nx.Graph()
    
    # 使用Barabási-Albert模型添加节点和边
    G = nx.barabasi_albert_graph(n, m0)
    
    # 可视化网络（需要安装 matplotlib）
    nx.draw(G, with_labels=True)
    plt.show()
    return G


def community_graph(num_communities, num_nodes_per_community, intra_edges, inter_edges):
    # 创建一个空图
    G = nx.Graph()
    # 为每个社团添加节点和边
    for i in range(num_communities):
        # 计算每个社团的节点范围
        start_node = i * num_nodes_per_community
        end_node = start_node + num_nodes_per_community
        # 添加社团内部的节点
        G.add_nodes_from(range(start_node, end_node))
        # 添加社团内部的边
        intra_edges_list = [(u, v) for u in range(start_node, end_node) for v in range(start_node, end_node) if u != v]
        G.add_edges_from(random.sample(intra_edges_list, min(intra_edges, len(intra_edges_list))))
    # 添加社团之间的边
    for i in range(num_communities):
        for j in range(i + 1, num_communities):
            # 从两个社团中随机选择一个节点进行连接
            node_u = random.randint(i * num_nodes_per_community, (i + 1) * num_nodes_per_community - 1)
            node_v = random.randint(j * num_nodes_per_community, (j + 1) * num_nodes_per_community - 1)
            G.add_edge(node_u, node_v)
    return G


def match_dict(ni, ci):
    """
    要将两个字典 {ni: float} 和 {ci: float} 中的键值进行匹配，使得最大的 ni 匹配最大的 ci，最小的 ni 匹配最小的 ci
    """
    # 根据值进行排序
    sorted_ni = sorted(ni.items(), key=lambda item: item[1])
    sorted_ci = sorted(ci.items(), key=lambda item: item[1])

    # 建立新的匹配字典
    matched_dict = {n: c for (n, _), (c, _) in zip(sorted_ni, sorted_ci)}
    return matched_dict




if __name__ == "__main__":
    # 设置参数
    num_communities = 4          # 社团数量
    num_nodes_per_community = 5  # 每个社团的节点数量
    intra_edges = 20              # 每个社团内部的边数量
    inter_edges = 2              # 每个社团之间的边数量
    
    # 生成随机社团网络
    graph = community_graph(num_communities, num_nodes_per_community, intra_edges, inter_edges)
    
    # 绘制网络图
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 7))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700)
    plt.title("Random Community Network")
    plt.show()
    
    #match by size
    import numpy as np
    size = {"c" + str(n):np.random.uniform(0.5,1) for n in graph.nodes}
    
    degree = {n:graph.degree(n) for n in graph.nodes}
    
    match_dict(size, degree)
    
    
    
    
    
    
    