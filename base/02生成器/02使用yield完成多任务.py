# coding:utf-8

import time


def task1():
    while True:
        print("-----test1")
        time.sleep(1)
        yield


def task2():
    while True:
        print("-----test2")
        time.sleep(1)
        yield


def main():
    # 并发，不是并行
    t1 = task1()
    t2 = task2()

    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()

