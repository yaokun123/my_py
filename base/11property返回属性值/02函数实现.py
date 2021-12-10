# coding:utf-8

# 将类方法转换为类属性，可以用 . 直接获取属性值或者对属性进行赋值


class Student(object):
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须0-100之间')
        self._score = value

    def del_score(self):
        del self._score

    score = property(get_score, set_score, del_score, "I'm the score property.")


if __name__ == "__main__":
    student = Student()
    print(student.score)
    student.score = 65
    print(student.score)
