# coding:utf-8
import time
from collections import Iterable,Iterator


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
            # 抛出异常通知迭代结束，for循环自动就停止了
            raise StopIteration
        res = self.names[self.current_num]
        self.current_num += 1
        return res


classmate = Classmate()
classmate.add('test1')
classmate.add('test2')
classmate.add('test3')

# for一个可迭代对象，会去调用迭代器的next()方法
for name in classmate:
    print(name)
    time.sleep(1)


# 一个对象是迭代器那么它一定可以迭代
# 一个对象可以迭代，不一定是迭代器