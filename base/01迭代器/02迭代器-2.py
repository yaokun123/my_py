# coding:utf-8
import time
from collections import Iterable,Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """
        如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法
        :return:(需要是一个对迭代器的引用)
        """
        return ClassIterator(self)


class ClassIterator(object):
    """
    迭代器必须实现__iter__和next方法
    """
    def __iter__(self):
        pass

    def next(self):
        if self.current_num >= len(self.obj.names):
            # 抛出异常通知迭代结束，for循环自动就停止了
            raise StopIteration
        res = self.obj.names[self.current_num]
        self.current_num += 1
        return res

    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0


classmate = Classmate()
classmate.add('test1')
classmate.add('test2')
classmate.add('test3')

print("判断classmate是否是可迭代对象：", isinstance(classmate, Iterable))

# iter()方法会获取到迭代器
classmate_iterator = iter(classmate)

print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))

# next()方法会调用迭代器的next()方法
print(next(classmate_iterator))

print("============开始迭代===============")
# for一个可迭代对象，会去调用迭代器的next()方法
for name in classmate:
    print(name)
    time.sleep(1)
