# coding:utf-8


class A(object):
    def __init__(self):
        print "A类中的====="


class B(A):
    def __init__(self):
        print "B类中的====="
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print "C类中的====="
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print "D类中的====="
        super(D, self).__init__()


if __name__ == "__main__":
    d = D()

    # 在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照MRO（Method Resolution Order）：方法解析顺序 进行的。
    # D类中的 == == =
    # B类中的 == == =
    # C类中的 == == =
    # A类中的 == == =
    print D.__mro__
