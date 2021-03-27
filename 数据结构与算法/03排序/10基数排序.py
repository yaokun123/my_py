# coding: utf-8


"""
多关键字排序：假如现在有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序
    先按照年龄进行排序，再按照薪资进行稳定的排序

对32，13，94，52，17，54，93排序，是否可以看作多关键字排序
"""


def radix_sort(li):
    max_num = max(li)   # 最大值99->2，888->3，10000->5

    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var//(10 ** it)) % 10
            buckets[digit].append(var)

        # 分桶完成
        del li[:]
        for buc in buckets:
            li += buc
        it += 1


import random
li = list(range(100))
random.shuffle(li)
print li

radix_sort(li)
print li


























