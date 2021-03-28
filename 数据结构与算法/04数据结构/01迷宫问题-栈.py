# coding:utf-8
"""
深度优先搜索（回朔法）

缺点：路径不一定是最短的
"""

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1)
]


def maze_path(x1, y1, x2, y2):
    """
    :param x1: 起点位置
    :param y1:
    :param x2: 终点位置
    :param y2:
    :return:
    """

    stack = []
    stack.append((x1, y1))

    while len(stack) > 0:
        curNode = stack[-1]

        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点
            for p in stack:
                print p
            return True

        # x,y 四个方向 上(x-1,y),右(x,y+1),下(x+1,y),左(x,y-1)
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # 如果下一个节点能走
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2      # 标记已经走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print "没有路"
        return False


maze_path(1, 1, 8, 8)
