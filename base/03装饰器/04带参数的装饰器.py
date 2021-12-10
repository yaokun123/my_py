# coding:utf-8

def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            print(contry + ":")
            func(*args, **kwargs)
        return deco
    return wrapper


@say_hello("china")
def xiaoming():
    print "你好"

xiaoming()