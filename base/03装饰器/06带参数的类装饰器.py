# coding:utf-8

"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
__init__：接收传入参数
__call__：接受被装饰函数，实现装饰逻辑
"""


class Logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):   # 接受函数
        def wrapper(*args, **kwargs):
            print self.level + ":" + "before:"
            func(*args, **kwargs)
        return wrapper          # 返回函数


@Logger("notice")
def say():
    print "hello world"

say()
