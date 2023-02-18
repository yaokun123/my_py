# coding:utf-8

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

    """
    总结：
    
    1、如果通过实例对描述器进行赋值操作，又有资料和非资料描述器的区分，如果定义了__set__，那么此方法生效，并且仍然是原始的资料描述器，否则被赋值为新对象
    
    2、描述器赋值如果是通过类的属性方式赋值，而不是类的实例方式赋值，描述器失效

    """
