# -*- coding: utf-8 -*-
"""
# 作者：wanglei5205
# 邮箱：wanglei5205@126.com
# 博客：http://cnblogs.com/wanglei5205
# github：http://github.com/wanglei5205
"""
### 导入模块
from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.externals import joblib

iris = load_iris()
x,y = iris.data,iris.target

model = svm.SVC()
model.fit(x,y)

joblib.dump(model,'dump_model.pkl')

model_new = joblib.load('dump_model.pkl')