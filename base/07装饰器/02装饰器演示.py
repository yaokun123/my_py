# coding:utf-8


def set_func(func):
    def call_func():
        print("这是权限验证")
        func()
    return call_func


def test1():
    print("==========test1===========")


@set_func   # 等见于test2 = set_func(test2)
def test2():
    print("==========test2===========")


test1()
test2()  # 相当与set_func(test2)()
