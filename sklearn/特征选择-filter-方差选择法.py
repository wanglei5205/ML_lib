# -*- coding: utf-8 -*-
# 载入数据
from sklearn.datasets import load_iris
iris = load_iris()
print("iris特征名称\n",iris.feature_names)
print("iris特征矩阵\n",iris.data)

# 特征选择--方差选择法
from sklearn.feature_selection import VarianceThreshold
vt = VarianceThreshold(threshold = 1)  # threshold为方差的阈值
vt = vt.fit_transform(iris.data)       # 函数返回值为特征选择后的数据
print("方差选择法选择的特征\n",vt)