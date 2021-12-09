# coding:utf-8

"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
__init__：接收被装饰函数
__call__：实现装饰逻辑
"""


class Logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before...")
        return self.func(*args, **kwargs)

@Logger
def say():
    print "hello world"

say()