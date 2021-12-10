# coding:utf-8

"""
__getattribute__抛出异常
"""
class TestMain:
    def __init__(self):
        print('TestMain:__init__')
        self.a = 1

    def __getattr__(self, item):
        print('TestMain:__getattr__')
        return 2

    def __getattribute__(self, item):
        print('TestMain:__getattribute__')
        if item == 'c':
            raise AttributeError
        return 3


if __name__ == '__main__':
    t = TestMain()
    print(t.a)
    print(t.b)
    print(t.c)

    # TestMain:__init__
    # TestMain:__getattribute__
    # 3
    # TestMain:__getattribute__
    # 3
    # TestMain:__getattribute__
    # TestMain:__getattr__
    # 2

    # 也就是说，如果__getattribute__抛出了AttributeError异常，那么会继续访问__getattr__函数的

    """
    总结：
    1、如果定义了__getattribute__，那么无论访问什么属性，都是通过这个函数获取，包括方法，t.f()这种也是访问的这个函数，此时这个函数应该放回一个方法，如果像例子中，仍然返回一个数字，你会获得一个TypeError: 'int' object is not callable错误
    
    2、只要定义了__getattribute__方法，不管你访问一个存在的还是不存在的属性，都由这个方法返回，比如访问t.a，虽然a存在，但是只要定义了这个访问，那么就不是访问最开始的a了
    
    3、如果__getattribute__抛出了AttributeError异常，并且定了了__getattr__函数，那么会调用__getattr__这个函数，不论这个属性到底是不是存在
    
    4、也就是说属性访问的一个大致优先级是：__getattribute__ > __getattr__ > __dict__
    """