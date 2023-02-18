# coding:utf-8

"""
作用：描述器的本质是一个对象，当对次对象进行增删该查操作时，会受到描述器的限制，比如更改的值不能为负等。
"""

# 描述器的创建 - 方式一
# 缺陷：1个age属性就需要定义3个方法来控制，那么3个属性就需要9个方法


class Person(object):
    def __init__(self):
        self.__age = 10

    @property
    def age(self):                  # 声明age作为Person类的一个属性。
        return self.__age

    @age.setter
    def age(self, value):           # 修改age属性会调用。
        if value < 0:
            value = 0
        self.__age = value

    @age.deleter
    def age(self):                  # 删除age属性会调用。
        print "del age"
        del self.__age


if __name__ == "__main__":
    p = Person()
    print p.age

    p.age = 19
    print p.age

    del p.age
    # print p.age                   # 此时已经没有age属性了，再访问会报错。