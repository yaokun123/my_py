# coding:utf-8


class Classmate(object):
    """
    可迭代对象的类
    """
    def __init__(self):
        self.names = list()

    def add(self, name_):
        self.names.append(name_)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):
    """
    迭代器的类
    """
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def next(self):
        if self.current_num >= len(self.obj.names):
            # for只判断了StopIteration的异常，没有判断其他异常，所以这里只能抛出StopIteration的异常
            raise StopIteration
        res = self.obj.names[self.current_num]
        self.current_num += 1
        return res


classmate = Classmate()
classmate.add('test1')
classmate.add('test2')
classmate.add('test3')

for name in classmate:
    print(name)

print "================================================"
# 每次获取迭代器的时候都获取的是新的迭代器对象（迭代器的计数器都是新的）所以可以多次迭代
for name in classmate:
    print(name)
