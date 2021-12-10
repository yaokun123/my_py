# coding:utf-8

"""
元类实战：ORM

使用过Django ORM的人都知道，有了ORM，使得我们操作数据库，变得异常简单。
ORM的一个类(User)，就对应数据库中的一张表。id,name,email,password 就是字段。
"""
import numbers
class Field(object):
    pass

class IntField(Field):
    def __init__(self, name):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        self._value = value

class StrField(Field):
    def __init__(self, name):
        self.name = name
        self._value = None
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        self._value = value


class BaseModel():
    pass


class User(BaseModel):
    id = IntField('id')
    name = StrField('uaername')
    email = StrField('email')
    password = StrField('password')

    class Meta:
        db_table = "user"

# 实例化成一条记录
# u = User(id=20180424, name="xiaoming", email="xiaoming@163.com", password="abc123")
User.id = "test"
print(User.id)

# 保存这条记录
# u.save()
