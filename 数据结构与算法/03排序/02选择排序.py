# coding:utf-8

"""
时间复杂度：
最坏情况：O(n**2)
平均情况：O(n**2)
最好情况：O(n**2)

空间复杂度：O(1)

稳定性：不稳定
"""


def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    for i in range(len(li) - 1):
        for j in range(i+1, len(li)):
            if li[j] < li[i]:
                li[j], li[i] = li[i], li[j]
    return li


li = [2, 5, 9, 4, 6, 4, 7, 8]
print(select_sort_simple(li))

li2 = [2, 5, 9, 4, 6, 4, 7, 8]
print(select_sort(li2))
