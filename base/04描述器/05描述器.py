# coding:utf-8

"""
一个类只要实现了__get__，__set__，__delete__中任意一个方法，我们就可以叫它描述器(descriptor)。

如果只定义了__get__我们叫非资料描述器(non-data descriptor)
如果__set__，__delete__任意一个/或者同时出现，我们叫资料描述器(data descriptor)

首先明确一点，拥有这个方法的类，应该(也可以说是必须)产生一个实例，并且这个实例是另外一个类的类属性(注意一定是类属性，通过self的方式产生就不属于__get__范畴了)。
"""

# 也就是说拥有这个方法的类，那么它的实例应该属于另外一个类/对象的一个属性。 直接看代码吧：
# 其中，__get__方法的第一个参数是实际拥有者的实例，如果没有则为None，第二个参数是实际所属的类。


class TestDes:
    def __get__(self, instance, owner):
        print(instance, owner)
        return 'TestDes:__get__'


class TestMain:
    des = TestDes()


if __name__ == '__main__':
    t = TestMain()
    print t
    print(t.des)
    print(TestMain.des)

