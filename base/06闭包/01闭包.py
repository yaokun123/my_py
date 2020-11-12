# coding:utf-8

# 以y = k*x + b为例，请计算一条线上的n个点

"""
第1种
k = 1
b = 2
y = k*x + b
缺点：如果需要多次计算，那么就要写多次y = k*x + b这样的式子
"""

"""
第2种:
缺点：如果需要多次计算，那么就要多次传k,b的值，麻烦
"""


def lin_2(k, b, x):
    print(k*x + b)


lin_2(1, 2, 0)
lin_2(1, 2, 1)
lin_2(1, 2, 2)
print("第2种")
print("-"*50)


"""
第3种:
缺点：如果需要计算多条线，需要修改全局变量k,b的值
"""

k = 1
b = 2


def lin_3(x):
    print(k * x + b)


lin_3(0)
lin_3(1)
lin_3(2)
k = 11
b = 22
lin_3(0)
lin_3(1)
lin_3(2)
print("第3种")
print("-"*50)


"""
第4种:缺省参数
优点：比全局变量的方式好在，k,b是函数的一部分，而不是全局变量，因为全局变量可以任意的被其他函数所修改
缺点：如果需要计算多条线，还是需要再调用的时候修改参数，麻烦
"""


def lin_4(x, k=1, b=2):
    print(k*x + b)


lin_4(0)
lin_4(1)
lin_4(2)

lin_4(0, k=11, b=22)
lin_4(1, k=11, b=22)
lin_4(2, k=11, b=22)
print("第4种")
print("-"*50)


"""
第5种:实力对象
缺点：为了计算多条线，用了很多实力对象，浪费资源
"""


class Line5(object):
    def __init__(self, k , b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


lin_5_1 = Line5(1, 2)
lin_5_1(0)
lin_5_1(1)
lin_5_1(2)
lin_5_2 = Line5(11, 22)
lin_5_2(0)
lin_5_2(1)
lin_5_2(2)
print("第5种")
print("-"*50)


"""
第6种:闭包
"""


def line_6(k, b):
    def create_y(x):
        print(k*x+b)
    return create_y


line_6_1 = line_6(1, 2)
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_2 = line_6(11, 22)
line_6_2(0)
line_6_2(1)
line_6_2(2)

# 闭包修改变量使用 nonlocal关键字
