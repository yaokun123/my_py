# coding:utf-8

"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
__init__：接收传入参数
__call__：接受被装饰函数，实现装饰逻辑
"""


class Logger(object):
    def __init__(self, level='INFO'):
        print "__init__"
        self.level = level

    def __call__(self, func):   # 接受函数
        print "__call__"

        def wrapper(*args, **kwargs):
            print self.level + ":" + "before:"
            func(*args, **kwargs)
        return wrapper          # 返回函数


@Logger("notice")       # 等见于say = Logger("notice")()
def say():
    print "hello world"

# 此时的say是一个函数<function wrapper at 0x10aff5320>
print say

say()
