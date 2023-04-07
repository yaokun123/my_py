# coding:utf-8

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name_):
        self.names.append(name_)

    def __iter__(self):
        return self

    def next(self):
        if self.current_num >= len(self.names):
            raise StopIteration
        res = self.names[self.current_num]
        self.current_num += 1
        return res

    def reset(self):
        self.current_num = 0


classmate = Classmate()
classmate.add('test1')
classmate.add('test2')
classmate.add('test3')


for name in classmate:
    print(name)

print "============================================================"
# 每次获取迭代器的时候都获取的是自己（迭代器的计数器复用）所以不能多次迭代
class_iterator_1 = iter(classmate)
class_iterator_2 = iter(classmate)
print class_iterator_1
print class_iterator_2
print "不能多次迭代。。。"
for name in classmate:
    print(name)

print "============================================================"
print "重置计数器，可以再次迭代"
classmate.reset()
for name in classmate:
    print(name)


print "============================================================"
# range(10)返回的是一个列表，占用空间大，存储的是数据
range_list = range(10)
print range_list, type(range_list)

# xrange(10)返回的是一个可迭代对象，占用空间较小，存储的是生成数据的方式，而不是具体的数据
xrange_iterable = xrange(10)
print xrange_iterable, type(xrange_iterable)


class XrangeIterable(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return XrangeIterator(self.num)


class XrangeIterator(object):
    def __iter__(self):
        pass

    def __init__(self, num):
        self.pos = 0
        self.num = num

    def next(self):
        if self.pos < self.num:
            tmp = self.pos
            self.pos += 1
            return tmp
        else:
            raise StopIteration


def my_xrange(num):
    return XrangeIterable(num)


my_xrange_iterable = my_xrange(10)
print my_xrange_iterable, type(my_xrange_iterable)
