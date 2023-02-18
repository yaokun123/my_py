# coding:utf-8


class Age(object):
    def __init__(self):
        self.__age = 0

    def __get__(self, instance, owner):
        return instance.__age

    def __set__(self, instance, value):
        # self 指向同一个Age实例
        # instance 指向不同的Person实例
        # 解决值存储问题：将属性绑定到instances上
        print "set", self, instance, value
        instance.__age = value

    def __delete__(self, instance):
        print "delete"


class Person(object):
    age = Age()


if __name__ == "__main__":
    p1 = Person()
    p1.age = 10

    p2 = Person()
    p2.age = 20

    print p2.age    # 20
    print p1.age    # 10，被p2的age影响了