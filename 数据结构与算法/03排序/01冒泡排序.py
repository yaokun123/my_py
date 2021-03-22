# coding:utf-8

"""
1、列表每两个相邻的数，如果前面比后面大，则交换这两个数。
2、一趟排序完成后，则无序区减少一个数，有序区增加一个数。

代码关键点：趟、无序区范围
"""


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li


def bubble_sort2(li):
    """
    优化：每一趟判断是否发生了交换，如果没有交换则不需要再进行交换了
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return li
    return li


li = [2, 5, 9, 4, 6, 4, 7, 8]
print(bubble_sort(li))

li2 = [2, 5, 9, 4, 6, 4, 7, 8]
print(bubble_sort(li2))

