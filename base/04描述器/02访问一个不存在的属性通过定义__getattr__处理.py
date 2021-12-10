# coding:utf-8

"""
测试一下__getattr__函数
"""


class TestMain:
    def __init__(self):
        print('TestMain:__init__')
        self.a = 1

    def __getattr__(self, item):
        print('TestMain:__getattr__')
        return 2


if __name__ == '__main__':
    t = TestMain()
    print(t.a)
    print(t.b)

    # 打印结果是：
    # TestMain:__init__
    # 1
    # TestMain:__getattr__
    # 2

    # 我们仍然访问了一个本来不存在的t.b，为什么这里没有报错呢，
    # 因为我们定义了__getattr__函数，而且让它直接返回了2，
    # 也就是说，如果定义了这个函数后，访问不存在的属性，会自动调用这个函数作为返回值。

