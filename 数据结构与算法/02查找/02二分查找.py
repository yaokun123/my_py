# coding:utf-8

"""
二分查找：又叫折半查找，从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，
可以使候选区减少一半。

前提：有序
时间复杂度O(logn)
"""


def binary_search(li, val):
    left = 0
    rigth = len(li) - 1

    while left <= rigth:
        mid = (left + rigth) // 2

        if li[mid] == val:
            return mid
        elif li[mid] > val:
            rigth = mid - 1
        elif li[mid] < val:
            left = mid + 1
    return None
