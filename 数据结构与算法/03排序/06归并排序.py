# coding:utf-8

"""
分解：将列表越分越小，直至分成一个元素
终止条件：一个元素使有序的
合并：将两个有序列表归并，列表越来越大


时间复杂度：
最坏情况：O(nlogn)
平均情况：O(nlogn)
最好情况：O(nlogn)

空间复杂度：O(n)

稳定性：稳定
"""


def merge(li, low, mid, high):
    i = low
    j = mid + 1

    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


li = [1, 8, 6, 4, 9, 3, 2]
# li = [2, 4, 5, 7, 1, 3, 6, 8]
# merge(li, 0, 3, 7)
merge_sort(li, 0, 6)
print(li)
