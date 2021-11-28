# coding:utf-8

from collections import Iterator, Iterable
"""
生成器是一种特殊的迭代器，没有next和__iter__方法
"""

"""
生成器的第一种方法（使用较少）
"""
nums = [x*2 for x in range(10)]
print "使用列表："
print nums
print type(nums)
print "check is Iterable:", isinstance(nums, Iterable)
print "check is Iterator:", isinstance(nums, Iterator)
print "=================================================="

# 将[]换为()得到可迭代对象
nums_2 = (x*2 for x in range(10))
print "使用元组："
print nums_2
print type(nums_2)
print "check is Iterable:", isinstance(nums_2, Iterable)
print "check is Iterator:", isinstance(nums_2, Iterator)
print "=================================================="


"""
生成器的第二种方法：使用yield关键字
如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板。
如果在调用fib的时候，发现函数中有yield，那么此时不是调用函数，而是创建一个生成器对象
"""


def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, (num1 + num2)
        current += 1
        yield num
    # return 'ok'
    # python3可以return

str_1 = ""
for x in fib(10):
    str_1 += str(x) + ","
print str_1
print "=================================================="

obj = fib(10)
str_2 = ""
while True:
    try:
        res = next(obj)
        str_2 += str(res) + ","
    except Exception as ret:
        break
        # ret.value
print str_2

print "=================================================="
# send方法，可以传送参数，接受方法：result = yield num
obj2 = fib(10)

re = next(obj2)
print(re)
r = obj2.send(None)
print(r)
