# coding:utf-8
from collections import Iterable,Iterator
nums = list()

a = 0
b = 1
i = 0

while i < 10:
    nums.append(a)
    a, b = b, a+b
    i += 1
print "nums is a list check is Iterable:", isinstance(nums, Iterable)
print "nums is a list check is Iterator:", isinstance(nums, Iterator)
print "=============================================================="
print "可迭代对象（非迭代器对象）可以任意迭代"
str1 = ""
for num in nums:
    str1 += str(num) + ','
print(str1)
str1 = ""
for num in nums:
    str1 += str(num) + ','
print str1
print "=============================================================="


print("使用迭代器")
# 使用迭代器


class Fib(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        if self.current_num >= self.all_num:
            raise StopIteration
        res = self.a
        self.a, self.b = self.b, (self.a + self.b)
        self.current_num += 1
        return res


fibo = Fib(10)
print "check fibo is Iterable:", isinstance(fibo, Iterable)
print "check fibo is Iterator:", isinstance(fibo, Iterator)
str1 = ""
for num in fibo:
    str1 += str(num) + ','
print str1

# print("第二次迭代：")
# str1 = ""
# fibo.current_num = 0
# fibo.a = 0
# fibo.b = 1
# for num in fibo:
#     str1 += str(num) + ','
# print str1


# list()和tuple()底层就是使用迭代器

