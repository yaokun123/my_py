# coding: utf-8

import os
import time
from multiprocessing import Process


class Demo(Process):
    def __init__(self):
        super(Demo, self).__init__()
        # self.fd = os.open("./readme.txt", os.O_RDONLY)

    def run(self):
        print "子进程 进程号%d" % os.getpid()
        time.sleep(1000)


if __name__ == "__main__":
    print "父进程 进程号%d" % os.getpid()
    for i in range(5):
        Demo().start()
