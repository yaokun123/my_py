# coding:utf-8

"""
pandas是一个强大的Python数据分析工具包，是基于Numpy构建的

主要功能：
1、具备对其功能的数据结构DataFrame、Series
2、集成时间序列功能
3、提供丰富的数学运算和操作
4、灵活处理缺失数据


Series一维数据对象：
"""

import pandas as pd

# 创建
a = pd.Series([2, 3, 4, 5])
print a

b = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])
print b
print b.index
print b.values
# 依然可以通过索引访问
print b[1]

c = pd.Series({'a': 1})
print c
"""
Series支持array的特性（下标）
1、与标量运算sr*2
2、两个Series运算sr1 + sr2
3、索引(sr[0],sr[[1,2,4]])
4、切片(sr[0:2])
5、通用函数(np.abs(sr))
6、布尔值过滤(sr[sr>0])

Series支持字典的特性
1、in运算(a in sr)
2、键索引(sr['a'])

使用整数索引时最好使用sr.loc()/rc.iloc()
"""