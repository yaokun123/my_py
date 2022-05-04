# coding:utf-8

"""
1、安装

pip install pytest
"""

"""
2、编写规则

测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可
"""

"""
3、运行
执行单个模块中的全部用例:pytest test_mod.py

执行指定路径下的全部用例:pytest somepath

执行字符串表达式中的用例:pytest -k stringexpr

运行指定模块中的某个用例，如运行 test_mod.py 模块中的 test_func 测试函数:
pytest test_mod.py::test_func

运行某个类下的某个用例，如运行 TestClass 类下的 test_method 测试方法:
pytest test_mod.py::TestClass::test_method
"""


"""
4、断言
通常情况下使用 assert 语句就能对大多数测试进行断言。
对于异常断言，可以使用上下文管理器 pytest.raises：
"""