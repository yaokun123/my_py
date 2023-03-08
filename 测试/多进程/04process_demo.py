# coding:utf-8

import os
import time
from multiprocessing import Pool


def work(i):
    print "[%d]子进程 进程号%d" % (i, os.getpid())
    time.sleep(1000)


def main_1():
    print "父进程 进程号%d" % os.getpid()
    ps = Pool(processes=5)
    for i in range(10):
        ps.apply(work, args=(i,))               # 同步执行，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不在出现

    ps.close()
    ps.join()                     # 主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。


def main_2():
    print "父进程 进程号%d" % os.getpid()
    ps = Pool(processes=5)
    for i in range(10):
        ps.apply_async(work, args=(i,))         # 异步执行，它是非阻塞且支持结果返回进行回调
    print "迭代结束"

    ps.close()
    ps.join()  # 主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。


def main_3():
    print "父进程 进程号%d" % os.getpid()
    ps = Pool(processes=5)
    ps.map(work, [1, 2, 3, 4, 5, 6, 7, 7, 9, 10])

    ps.close()
    ps.join()  # 主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。


# main_1()
# main_2()
main_3()


