# coding:utf-8

"""
__getattribute__这个函数
"""


class TestMain:
    def __init__(self):
        print('TestMain:__init__')
        self.a = 1

    def __getattr__(self, item):
        print('TestMain:__getattr__')
        return 2

    # python2.7有问题
    def __getattribute__(self, item):
        print('TestMain:__getattribute__')
        return 3


if __name__ == '__main__':
    t = TestMain()
    print(t.a)
    print(t.b)

    # 打印结果是：
    # TestMain:__init__
    # TestMain:__getattribute__
    # 3
    # TestMain:__getattribute__
    # 3

    # 可以看到，无论是访问存在的t.a还是不存在的t.b，
    # 都访问到了__getattribute__这个函数，也就是说，
    # 只要定义了这个函数，那么属性的访问，都会走到这个函数里面。

