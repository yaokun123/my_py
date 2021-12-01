# coding=utf-8

"""
DataFrame (数据框：二维表）

DataFrame是一个表格型的数据结构，含有一组有序的列。DataFrame可以被看作是由Series组成的字典，并且共用一个索引

常用属性：
index:          获取索引
T:              转置
columns:        获取列索引
values:         获取值数组
describe:       获取快速统计


索引和切片
DataFrame是一个二维数据类型，所以有行索引和列索引
DataFrame同样可以通过用标签和位置两种方法进行索引和切片
loc属性和iloc属性：
    使用方法：逗号隔开，前面是行索引，后面是列索引
    行/列索引部分可以是常规索引、切片、布尔索引、花式索引任意搭配
a[列][行]


DataFrame数据对齐与确实数据
DataFrame对象在运算时，同样会进行数据对齐，其行索引和列索引分别对齐
DataFrame处理缺失数据的相关方法：
    dropna(axis=0,where='any',...)
    fillna()
    isnull()
    notnull()


pandas其他常用函数
mean(axis=0,skipna=False):              对列（行）求平均值
sum(axis=1):                            对列（行）求和
sort_index(axis,...,ascending):         对列（行）索引排序
sort_values(by,axis,ascending):         按某一列（行）的值排序
NumPy的通用函数同样适用pandas
"""
import pandas as pd

# 创建方式
a = pd.DataFrame({'one': [1, 2, 3, 4], 'two': [4, 3, 2, 1]})
print a

b = pd.DataFrame({'one': [1, 2, 3, 4], 'two': [4, 3, 2, 1]}, index=['a', 'b', 'c', 'd'])
print b

c = pd.DataFrame({'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['b', 'a', 'c', 'd'])})
print c

# csv文件的读写
# pd.read_csv('filename.csv')
# pd.to_csv
