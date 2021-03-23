# coding:utf-8
import time
from collections import Iterable, Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """
        如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法
        :return:(需要是一个对迭代器的引用)
        """
        return self

    def next(self):
        if self.current_num >= len(self.names):
            raise StopIteration
        res = self.names[self.current_num]
        self.current_num += 1
        return res


classmate = Classmate()
classmate.add('test1')
classmate.add('test2')
classmate.add('test3')


# 一个对象是迭代器那么它一定可以迭代
# 一个对象可以迭代，不一定是迭代器
print "判断classmate是不是可迭代对象", isinstance(classmate, Iterable)
print "判断classmate是不是迭代器", isinstance(classmate, Iterator)
print "============================================================"

for name in classmate:
    print(name)
    time.sleep(1)

print "============================================================"
# 迭代器呢，一次for循环就没有了，而可迭代对象呢，任你for一万次都会输出
# classmate是可迭代对象（但同时也是迭代器），所以不能多次迭代
for name in classmate:
    print(name)
    time.sleep(1)


# range(10)返回的是一个列表，占用空间大，存储的是数据
# xrange(10)返回的是一个迭代器，占用空间较小，存储的是生成数据的方式，而不是数据
