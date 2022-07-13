# coding:utf-8


def foo():
    print('foo')


print foo  # 表示是函数
foo()  # 表示执行foo函数


def foo():
    print('foo')


foo = lambda x: x+1

print foo(1)  # 执行lambda表达式，而不再是原来的foo函数，因为foo这个名字被重新指向了另外一个匿名函数

