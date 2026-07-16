
# 1. 单元测试的文件结构
在根目录下只需要留一个入口文件即可，即在根目录下创建一个叫 `tests` 的文件夹，里面专门用来放测试代码。该文件夹作为一个 package，里面同样有 `__init__.py` 文件。


使用标准库中的 `unittest` 模块启动测试，在项目根目录下运行命令以启动测试，python 会自动寻找测试并且运行测试：
``` shell
python -m unittest
```

# 2. 基础的测试写法
测试是检查程序运行的结果，即在写**测试前**必须知道正确答案。

## 2.1 测试文件的写法
1. 每一个测试文件必须以 `test_` 开头。
    - 例如：`test_moduleA.py`
2. 必须引用依赖：
   - 库 `import unittest`
   - 要测试的模块 `from myPackage import moduleA`
3. 撰写 `test class`，继承自 `unittest.TestCase`
4. 在 `test class` 中，编写测试方法，每个测试方法必须以 `Test` 开头或结尾。
5. 每一个 `test class` 中可以有若干个 `test method`，且这些 `test method` **必须**以 `test_` 开头。

示例：
``` python
import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def test_init(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)    
        self.assertEqual(v.y, 2)
```

## 2.2 常用的单元测试语句
[Unit testing framework](https://docs.python.org/3/library/unittest.html)
1. `assertEqual(actual, expected)` 断言 `actual` 等于 `expected`。
   - 例如：`self.assertEqual(x, 1)`
2. `assertTure(condition)` 断言 `condition` 为 `True`。
   - 例如：`self.assertTrue(x == 0)`、 `self.assertTrue(x > 0)`

`assertEqual` 和 `assertTure` 的对比：
- `assertEqual` 在 fail 时能给出更多的信息
- `assertTure` 在 fail 时只能给出 `AssertionError: False is not true`

> 注意：
> 每个 `test method` 只要有一个地方出现了 fail 就不会继续运行。

3. `assertRaises(exception, callable, *args, **kwargs)` 断言 `callable` 抛出 `exception`。
``` python
# vector.py
if isinstance(x,(int, float)) and isinstance(y,(int, float)):
    self.x = x
    self.y = y
else:
    raiseValueError("not a number")

# test_vector.py
with self.assertRaises(ValueError):     # 如果传入的参数不是数字，会输出 "OK"；若不合法，就会 fail 抛出 ValueError：“AssertionError: False is not true”
    Vector(1, 2)
```

## 2.3 常用 unittest 的 feature

### 2.3.1 在运行 test 前后执行代码
1. 运行 `test module` 前后执行代码  
在 `test class` 内定义 `setUp()` 和 `tearDown()` 方法，分别在每个 `test method` 前后执行。

2. 运行 `test class` 前后执行代码
在 `test class` 内定义 `setUpClass()` 和 `tearDownClass()` 方法,并使用 `@classmethod` 装饰器，分别在 `test class` 前后执行。


### 2.3.2 让某些测试在某些情况下不运行
使用 decorator `@unittest.skipIf(condition, reason)` 来实现。
- `condition`: 一个布尔表达式，当 `condition` 为 `True` 时，测试方法不会被运行。
  - 例如：`sys.platform == 'win32"`、 `sys.version_info < (3, 7)`
- `reason`: 测试方法不被运行的原因，用于在测试报告中显示。
  - 例如：`reason="Do not support Windows"`、 `reason="Python version support >= 3.7"`


# 3. 运行指定的测试方法
1. module 级（如 test_vector.py 文件）
2. class 级（如 TestVector 类）
3. test method 级（如 test_init、test_add 等 test 方法）

例如：
``` shell
# 运行 test_vector.py 文件中的 TestVector 类的 test_add 方法
python -m unittest tests.test_vector.TestVector.test_add

# 运行 test_vector.py 文件中的 TestVector 类的所有测试方法
python -m unittest tests.test_vector.TestVector
```