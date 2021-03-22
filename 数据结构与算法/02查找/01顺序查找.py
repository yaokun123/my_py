# coding:utf-8


"""
顺序查找：也叫线性查找，从列表第一个元素开始，顺序进行搜索，知道找到元素或搜索到列表最后一个元素为止。
时间复杂度O(n)
"""


def liner_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None
