# coding:utf-8

"""
如果只定义了__get__我们叫非资料描述器(non-data descriptor)
如果__set__，__delete__任意一个/或者同时出现，我们叫资料描述器(data descriptor)

优先级：资料描述器 > 实例属性 > 非资料描述器
"""


# 非资料描述器的优先级
class Age(object):
    def __get__(self, instance, owner):
        print "get"


class Person(object):
    age = Age()                     # 类属性

    def __init__(self):
        self.age = 10               # 实例属性


if __name__ == "__main__":
    p = Person()

    p.age = 11
    print p.age                     # 11，说明实例属性的优先级大于非资料描述器

    # del p.age

    print p.__dict__