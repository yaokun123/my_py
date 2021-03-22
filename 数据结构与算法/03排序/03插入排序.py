# coding:utf-8

"""

"""


def insert_sort(li):
    for i in range(1, len(li)):
        j = i-1
        select_val = li[i]
        while j >= 0 and select_val < li[j]:
            li[j+1] = li[j]
            j -= 1

        li[j+1] = select_val
    return li


li = [2, 5, 9, 4, 6, 4, 7, 8, 1]
print(insert_sort(li))
