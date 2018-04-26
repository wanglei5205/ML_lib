# -*- coding: utf-8 -*-
# 载入数据
from sklearn.datasets import load_iris
iris = load_iris()

# 特征选择
from sklearn.feature_selection import SelectKBest # 移除topK外的特征
from sklearn.feature_selection import chi2        # 卡方检验

skb = SelectKBest(chi2,k=2)
new_data = skb.fit_transform(iris.data,iris.target)