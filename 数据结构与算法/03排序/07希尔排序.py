# coding:utf-8

"""
1、希尔排序是一种分组插入排序算法
2、首先取一个整数d1=n/2，将元素分为d1个组，每组相邻两元素之间距离为d1，在各组内进行直接插入排序。
3、取第二个整数d2=d1/2，重复上述分组排序过程，直到di=1，即所有元素在同一组内进行直接插入排序。
4、希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序，最后一趟排序使得所有数据有序。
"""


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        j = i-gap
        select_val = li[i]
        while j >= 0 and select_val < li[j]:
            li[j+gap] = li[j]
            j -= gap

        li[j+gap] = select_val


def shell_sort(li):
    d = len(li) // 2

    while d >= 1:
        insert_sort_gap(li, d)
        d = d // 2

