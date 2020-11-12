# coding:utf-8


class A(object):
    def __init__(self):
        print "A类中的====="


class B(A):
    def __init__(self):
        print "B类中的====="
        A.__init__(self)


class C(A):
    def __init__(self):
        print "C类中的====="
        A.__init__(self)


class D(B, C):
    def __init__(self):
        print "D类中的====="
        B.__init__(self)
        C.__init__(self)


if __name__ == "__main__":
    D()
    # D类中的 == == =
    # B类中的 == == =
    # A类中的 == == =
    # C类中的 == == =
    # A类中的 == == =

    # 导致A类中的方法执行了两次
