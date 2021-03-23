# coding:utf-8
import random

import heapq   # 自带堆排序


"""
堆排序前传：二叉树的顺序存储方式
1、父节点和左孩子节点的编号下标有什么关系？i->2i+1
2、父节点和右孩子节点的编号下标有什么关系？i->2i+2

左右孩子与父节点的编号下标有什么关系？i->(i-1)/2
"""



"""
堆排序

堆：一种特殊的完全二叉树结构
大根堆：一颗完全二叉树，满足任一节点都比其孩子节点大
小根堆：一颗完全二叉树，满足任一节点都比其孩子节点小

堆的向下调整性质：
1、假设根节点的左右子树都是堆。但根节点不满足堆的性质
2、可以通过一次向下的调整来将其变成一个堆


堆排序过程
1、建立堆。
2、得到堆顶元素，为最大元素。
3、去掉堆顶，将堆最后一个元素放到堆顶，此时可以通过一次调整重新使堆有序。
4、堆顶元素为第二大元素。
5、重复步骤3，直到堆变空。


时间复杂度O(nlogn)
"""

def sift(li, low, high):
    """
    向下调整
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素位置
    :return:
    """
    i = low         # 最开始指向根节点
    j = 2 * i + 1   # 左
    tmp = li[low]   # 把堆顶存下来

    while j <= high:
        if j+1 <= high and li[j+1] > li[j]:     # 如果右孩子有，且比较大
            j = j + 1           # j指向右孩子

        if li[j] > tmp:
            li[i] = li[j]
            i = j               # 往下看一层
            j = 2 * i + 1
        else:                   # tmp更大，把tmp放到i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp     # 把tmp放到叶子节点上


def heap_sort(li):
    n = len(li)

    for i in range((n-2)//2,-1,-1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n-1)

    # 建堆完成
    print li

    # 排序
    for i in range(n-1,-1,-1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)


li = [i for i in range(100)]
random.shuffle(li)
print li
heap_sort(li)


print li

