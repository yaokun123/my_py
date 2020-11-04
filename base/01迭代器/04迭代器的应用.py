# coding:utf-8

nums = list()

a = 0
b = 1
i = 0

while i < 10:
    nums.append(a)
    a, b = b, a+b
    i += 1

for num in nums:
    print num


print("使用迭代器")
# 使用迭代器
class Fib(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        if self.current_num >= self.all_num:
            raise StopIteration
        res = self.a
        self.a, self.b = self.b, (self.a + self.b)
        self.current_num += 1
        return res


fibo = Fib(10)
for num in fibo:
    print num