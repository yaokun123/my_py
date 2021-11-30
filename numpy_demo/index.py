# coding:utf-8
"""
为什么要用NumPy
eg1:已知若干家跨国公司的市值（美元），将其转化为人民币
eg2:已知购物车中每件商品的价格与商品件数，求总金额

array():    将列表转换为数组，可选择显式指定dtype
arange():   range的numpy版，支持浮点数
linspace(): 类似arange()，第三个参数为数组长度
zeros():    根据指定形状和dtype创建全0数组  zeros(10, dtype='int')
ones():     根据指定形状和dtype创建全1数组
empty():    根据指定形状和dtype创建空数组（随机值）
eye():      根据指定边长和dtype创建单位矩阵
reshape(n,m):  根据给定的维度重新生成数组

数组和标量之间的计算：a+1    a*3    1//a    a**0.5    a>5
同样大小数组之间的运算：a+b    a/b    a**b    a%b    a==b
一维数组的索引：a[5]
多维数组的索引：a[2][3] a[2,3](新式写法)

一维数组的切片：a[5:8]    a[4:]    a[2:10] = 1
多维数组的切片：a[1;2,3:4]    a[:,3:5]    a[:,1]
数组切片与列表切片的不同：数组切片时并不会自动复制（而是创建一个视图），在切片数组上的修改会影响到原数组
        copy()方法可以创建数组的深拷贝
"""
import numpy as np
import random

a = [random.uniform(100.0, 200.0) for i in range(10)]
x = 6.8

# 原始用法
b = []
for ele in a:
    b.append(ele*x)
print a
print b

# 将列表转化为数组
a = np.array(a)
print a
# 数组 * 数字 = 数组（数组中每个元素都会乘上这个数字）
print a * x

print "================================="

a1 = [random.uniform(100.0, 200.0) for i in range(10)]
a2 = [random.randint(5, 10) for i in range(10)]

# 将列表转化为数组
a1 = np.array(a1)
a2 = np.array(a2)
print a1
print a2

# 两个数组相乘 = 数组中对应的每个元素相乘
print a1 * a2

# 使用sum()计算数组中元素的和
print (a1 * a2).sum()

# 打印数组中存放的类型（数组中的元素是相同类型、数组的长度不可改变）
print a1.dtype
print a2.dtype

print "================================="
# 使用多纬数组
b1 = np.array([[1, 2, 3], [4, 5, 6]])
print b1
print b1.dtype

# 二维数组中元素个数
print b1.size

# n * m 数组(2, 3)//2行3列
print b1.shape

# 转换行列
print b1.T

print "================================="
# 画一下x**2 在-10-10之间的图像
x = np.linspace(-10, 10, 1000)
y = x**2
print x
print y
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
