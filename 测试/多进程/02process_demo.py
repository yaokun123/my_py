# coding:utf-8
import os
import time
from multiprocessing import Process


class Demo(object):
    def __init__(self):
        self.inc_process_num = 5

    def run(self):
        print "子进程 进程号%d" % os.getpid()
        time.sleep(1000)

    def main_1(self):
        print "父进程 进程号%d" % os.getpid()
        processes = []
        for i in range(0, self.inc_process_num):
            p = Process(target=self.run)
            processes.append(p)
        [x.start() for x in processes]


if __name__ == "__main__":
    Demo().main_1()
