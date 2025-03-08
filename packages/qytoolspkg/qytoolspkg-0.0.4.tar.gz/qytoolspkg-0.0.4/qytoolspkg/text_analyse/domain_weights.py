# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:48:05 2025

@author: qiyu
"""
import itertools
import jieba
from collections import defaultdict

def construct_domain_weights(base_weights, domain_dicts, domain_limit=99, mu=1.0):
    """
    构建领域组合权重
    返回格式: {frozenset(领域组合): 权重}
    """
    domains = list(domain_dicts.keys())
    combined_weights = {}

    # 生成所有组合
    for level in range(1, min(domain_limit, len(domains)) + 1):
        for combo in itertools.combinations(domains, level):
            combo_set = frozenset(combo)
            
            # 计算基础权重和
            weight_sum = sum(base_weights.get(d, 0) for d in combo)
            
            # 应用μ系数
            combined_weight = (mu ** (level-1)) * weight_sum
            combined_weights[combo_set] = combined_weight
            
    return combined_weights

def calculate_word_weights(combined_weights, domain_dicts):
    """
    计算词权重核心逻辑
    """
    # 构建反向索引
    word_domains = defaultdict(set)
    for domain, words in domain_dicts.items():
        for word in words:
            word_domains[word].add(domain)

    # 计算词权重
    word_weights = defaultdict(float)
    for word, domains in word_domains.items():
        total = 0.0
        # 遍历所有组合
        for combo, weight in combined_weights.items():
            if combo.issubset(domains):
                total += weight
        word_weights[word] = total
        
    return dict(word_weights)

def calculate_text_score(text, word_weights, stopwords):
    """文本评分实现"""
    words = [word for word in jieba.lcut(text) 
            if word.strip() and word not in stopwords]
    
    if not words:
        return {'total_score': 0.0, 'word_contribution': {}}
    
    total_weight = sum(word_weights.get(word, 0) for word in words)
    normalized_score = total_weight / len(words)
    
    contributions = defaultdict(float)
    for word in words:
        contributions[word] += word_weights.get(word, 0)
    
    contributions = {word: weight for word, weight in contributions.items() if weight > 0}
    
    return {'total_score': normalized_score, 'word_contribution': dict(contributions)}
