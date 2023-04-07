# coding:utf-8
import time
from collections import Iterable, Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        print "[迭代器被创建。。。]"
        """
        如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法
        :return:(需要是一个对迭代器的引用)
        """
        return ClassIterator()


class ClassIterator(object):
    """
    迭代器必须实现__iter__和next方法
    """
    def __iter__(self):
        pass

    def next(self):
        return 11


classmate = Classmate()
classmate.add('test1')
classmate.add('test2')
classmate.add('test3')

print "判断classmate是否是可迭代对象：", isinstance(classmate, Iterable)
print "判断classmate是否是迭代器:", isinstance(classmate, Iterator)
print "=============================================="

# iter()方法会获取到迭代器对象，调用一次返回一个对象
class_iterator = iter(classmate)    # 迭代器被创建
class_iterator2 = iter(classmate)   # 迭代器被创建
print "classmate的迭代器是class_iterator:", class_iterator
print "classmate的迭代器是class_iterator:", class_iterator2
print "判断classmate_iterator是否是可迭代对象：", isinstance(class_iterator, Iterable)
print "判断classmate_iterator是否是迭代器：", isinstance(class_iterator, Iterator)
print "=============================================="

# next()方法会调用迭代器的next()方法
print next(class_iterator)

# next()方法参数必须是迭代器，不能是可迭代对象
# print next(classmate)

print "=============================================="

# for 的本质
# 1、调用可迭代对象的__iter__()方法拿到迭代器对象
# 2、调用迭代器的next方法，直到迭代器的next方法抛出异常（for会自动捕获异常）
i = 0
for name in classmate:
    if i >= 5:
        break
    print name
    i += 1

# 由于class_iterator2是一个迭代器，且没有定义__iter__()方法所以拿不到迭代器，从而报错
# for name in class_iterator2:
#     print name
