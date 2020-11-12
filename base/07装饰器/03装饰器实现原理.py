# coding:utf-8


def set_func(func):
    def call_func():
        print("这是权限验证")
        func()
    return call_func


def test1():
    print("==========test1===========")


test1 = set_func(test1)
test1()
