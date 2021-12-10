# coding:utf-8
class TestMain:
    def __init__(self):
        print('TestMain:__init__')
        self.a = 1


if __name__ == '__main__':
    t = TestMain()
    print(t.a)          # 在没有任何get函数的情况下很简单，打印结果是
    # TestMain:__init__
    # 1

    # 但是如果访问一个不存在的属性：
    print(t.b)  # 访问了一个不存在的属性,可以看见报错