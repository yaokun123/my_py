# coding: utf-8

import os


def main_1():
    pid = os.fork()
    if pid < 0:
        print "fork fail"
    elif pid == 0:
        print "子进程 进程号%d" % os.getpid()
    elif pid > 0:
        print "父进程 进程号%d" % os.getpid()


main_1()
