# coding: utf-8


import os
import time
from multiprocessing import Process


def work_1():
    print "work_1子进程 进程号:%d" % os.getpid()
    time.sleep(10)
    print "work_1 结束"


def work_2():
    print "work_2子进程 进程号:%d" % os.getpid()
    time.sleep(15)
    print "work_2 结束"


def work_3():
    print "work_3子进程 进程号:%d" % os.getpid()
    time.sleep(20)
    print "work_3 结束"


def work_4():
    print "work_4子进程 进程号:%d" % os.getpid()
    time.sleep(25)
    print "work_4 结束"


def work_5():
    print "work_5子进程 进程号:%d" % os.getpid()
    time.sleep(30)
    print "work_5 结束"


def work_6():
    print "work_6子进程 进程号:%d" % os.getpid()
    time.sleep(35)
    print "work_6 结束"


def main():
    p1 = Process(target=work_1)
    p2 = Process(target=work_2)
    p3 = Process(target=work_3)
    p4 = Process(target=work_4)
    p5 = Process(target=work_5)
    p6 = Process(target=work_6)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()


print "父进程 进程号:%d" % os.getpid()
main()
# test = set()
# test.add("test1")
# test.add("test2")
# test.add("test3")
# test.add("test4")
# test.add("test5")
# for p in test:
#     print p