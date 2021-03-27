# coding:utf-8


"""
对列表进行排序，已知列表中的数范围都在0到100之间。设计时间复杂度为O(n)的算法。
"""


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]

    for val in li:
        count[val] += 1
    del li[:]
    # python 可用li.clear()

    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


import random
li = [random.randint(0, 100) for _ in range(100)]
print li
count_sort(li)
print li



