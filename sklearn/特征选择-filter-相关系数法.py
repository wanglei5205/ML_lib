# -*- coding: utf-8 -*-
# 载入数据
from sklearn.datasets import load_iris
irisdata = load_iris()

# 特征选择（pearson相关系数法）
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr
from numpy import array
"""
# 函数返回值：特征选择后的k个最好的特征
# 第一个参数：计算相关系数的函数（输入特征矩阵和目标向量，输出二元组（评分，P），二数组第i项为第i个特征的评分和p值
# 第二个参数：特征选择后的特征个数k
"""
skb = SelectKBest(lambda X, Y: tuple(map(tuple,array(list(map(lambda x:pearsonr(x, Y), X.T))).T)), k=3)
skb = skb.fit_transform(irisdata.data, irisdata.target)