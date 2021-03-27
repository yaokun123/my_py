# coding: utf-8

"""
计数排序改进：

1、在计数排序中，如果元素的范围比较大(比如在1到1亿之间)，如何改造算法
2、桶排序：首先将元素分在不同的桶中，再对每个桶中的元素排序
"""


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]    # 创建桶

    for val in li:
        i = min(val // (max_num//n), n-1)     # 几号桶
        buckets[i].append(val)

        # 放进去的过程就排序。。。
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j-1] > buckets[i][j]:
                buckets[i][j - 1], buckets[i][j] = buckets[i][j], buckets[i][j-1]
                j -= 1
            else:
                break
    new_li = []
    for buc in buckets:
        new_li += buc

    return new_li


import random
li = [random.randint(0, 100000) for _ in range(100)]
print li
print bucket_sort(li)



