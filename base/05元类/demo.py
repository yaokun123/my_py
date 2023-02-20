# coding:utf-8

"""
元类实战：ORM

使用过Django ORM的人都知道，有了ORM，使得我们操作数据库，变得简单。
ORM的一个类(User)，就对应数据库中的一张表。id,name,email,password 就是字段。
"""
import numbers
class Field(object):
    pass

# 数字描述器
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
# 字符串描述器
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

class ModelMetaClass(type):
    """
    所以在创建一个普通类时，其实会走元类的 __new__
    """
    def __new__(cls, name, bases, attrs):
        if name == "BaseModel":
            # 第一次进入__new__是创建BaseModel类，name="BaseModel"
            # 第二次进入__new__是创建User类及其实例，name="User"
            return super().__new__(cls, name, bases, attrs)

        # 根据属性类型，取出字段
        fields = {k:v for k,v in attrs.items() if isinstance(v, Field)}

        # 如果User中有指定Meta信息，比如表名，就以此为准
        # 如果没有指定，就默认以 类名的小写 做为表名，比如User类，表名就是user
        _meta = attrs.get("Meta", None)
        db_table = name.lower()
        if _meta is not None:
            table = getattr(_meta, "db_table", None)
            if table is not None:
                db_table = table

        # 注意原来由User传递过来的各项参数attrs，最好原模原样的返回，
        # 如果不返回，有可能下面的数据描述符不起作用
        # 除此之外，我们可以往里面添加我们自定义的参数
        attrs["db_table"] = db_table
        attrs["fields"] = fields
        return super().__new__(cls, name, bases, attrs)

class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kw):
        for k,v in kw.items():
            # 这里执行赋值操作，会进行数据描述符的__set__逻辑
            setattr(self, k, v)
        return super().__init__()

    def save(self):
        db_columns = []
        db_values = []
        for column, value in self.fields.items():
            db_columns.append(str(column))
            db_values.append(str(getattr(self, column)))
        sql = "insert into {table} ({columns}) values({values})".format(
            table=self.db_table, columns=','.join(db_columns),
            values=','.join(db_values))
        print(sql)


class User(BaseModel):
    # 创建一些描述器
    id = IntField('id')
    name = StrField('uaername')
    email = StrField('email')
    password = StrField('password')

    class Meta:
        db_table = "tb_user"

# 实例化成一条记录
u = User(id=20180424, name="xiaoming", email="xiaoming@163.com", password="abc123")

# 保存这条记录
u.save()
