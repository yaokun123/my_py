# coding:utf-8

"""
快速排序思路：
1、取一个元素p(第一个元素)，使元素p归位；
2、列表被p分成两部分，左边都比p小，右边都比p大；
3、递归完成排序

时间复杂度：
一般：O(nlogn)
最坏：O(n*n)递归最大深度（随机化）
"""

# [5,7,4,6,3,1,2,9,8]


def position(li, left, right):
    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp

    return left


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print(position(li, 0, len(li)-1))


def quick_sort(li, left, right):
    if left < right:
        mid = position(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


li2 = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(li2, 0, len(li2)-1)
print(li2)
