# coding:utf-8

# 类中的__call__函数，可以让类的实例像函数调用样被调用

"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
__init__：接收被装饰函数
__call__：实现装饰逻辑
"""
from collections import Callable


class Logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before...")
        return self.func(*args, **kwargs)


@Logger
def say():      # 等见于say = Logger(say)
    print "hello world"


print "===================================="
# 此时的say 其实是一个Logger对象，而不是函数
print say

# 实现__call__函数的类的对象是可调用对象，没有实现就是不可调用对象
print isinstance(say, Callable)
print "===================================="

# 之所以可以直接调用是因为实现了__call__函数。调用对象的时候会去找__call__函数
say()
