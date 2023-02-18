# coding:utf-8

"""
一个类只要实现了__get__，__set__，__delete__中任意一个方法，我们就可以叫它描述器(descriptor)。
"""

# 描述器的创建 - 方式二


# 描述age的类
class Age(object):
    def __get__(self, instance, owner):
        print "get"

    def __set__(self, instance, value):
        print "set"

    def __delete__(self, instance):
        print "delete"


class Person(object):
    age = Age()


if __name__ == "__main__":
    # 使用实例调用，会调用__get__/__set__/__delete__
    p = Person()
    print p.age
    p.age = 10
    del p.age

    # 使用类调用，只调用__get__
    print Person.age
    Person.age = 19
    del Person.age