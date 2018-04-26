# -*- coding: utf-8 -*-
# 创建dataframe
import pandas as pd
s = pd.DataFrame(['a,b,c','c,d,e'])
print(s,'\n')
"""
       0
0  a,b,c
1  c,d,e
"""
# 字符串拆分--expend = False
temp_expend_False = s[0].str.split(',')
print(temp_expend_False,'\n')
"""
0    [a, b, c]
1    [c, d, e]
"""

# 字符串拆分--expend = True
temp_expend_True = s[0].str.split(',',expand = True)
print(temp_expend_True,'\n')
"""
   0  1  2
0  a  b  c
1  c  d  e
"""

