# coding:utf-8

"""
非资料描述器，也就是只有__get__，不管是类还是实例去访问，默认都获得的是__get__的返回值，
但是，如果中间有任何一次重新赋值，那么，这个实例获得的是新的值(对象)，已经和原来的描述器完全脱离了关系
"""


class TestDes:
    def __get__(self, instance, owner):
        print('TestDes:__get__', instance, owner)
        return 'TestDes:__get__'


class TestMain:
    des = TestDes()


if __name__ == '__main__':
    t = TestMain()
    print(t.des)        # TestDes:__get__ <__main__.TestMain object at 0x000002C9BCCF0080> <class '__main__.TestMain'>
                        # TestDes:__get__
    print(TestMain.des) # TestDes:__get__ None <class '__main__.TestMain'>
                        # TestDes:__get__
    print()

    t.des = 1           # 非资料描述器的重新赋值

    print(t.des)        # 1
    print(TestMain.des) # TestDes:__get__ None <class '__main__.TestMain'>
                        # TestDes:__get__

    print()

    TestMain.des = 1    # 非资料描述器的重新赋值
    print(t.des)        # 1
    print(TestMain.des) # 1
