
## 1.1 导入一个包的过程
- 搜寻模块
- 执行代码
- 封装模块
- 缓存模块
- 绑定变量


## 1.2 __init__.py 在何时被使用

### 1.1.1 包的初始化
当导入一个包 packageA 时，会自动执行 packageA/__init__.py 文件中的代码。
``` python
# main.py

import packageA
```
``` python
# packageA/__init__.py

print("packageA 初始化")
```
当执行 main.py 时，会输出 "packageA 初始化"。


### 1.1.2 管理包接口


``` python
# main.py
from packageA import x

print(x)
```
``` python
# packageA/__init__.py
from .moduleA import x

print("packageA 初始化")
```
``` python
# packageA/moduleA.py

print("moduleA 初始化")
```
当执行 main.py 时，会输出 "moduleA 初始化"。


在 main.py 中，我们可以使用 `from packageA import *` 来导入 packageA 中“所有”东西。  
“所有”通过 packageA/__init__.py 文件中的 `__all__` 列表来确定。
``` python
# packageA/__init__.py
from . import moduleA
from .moduleA import x

__all__ = ['x', 'moduleA']
```

### 1.1.3 包的信息
``` python
# packageA/__init__.py

__version__ = "1.0.0"
__author__ = "author_name"
```

``` python
# main.py
from packageA

print(packageA.__version__)
print(packageA.__author__)
```


## 1.3 案例

在 __init__.py 中加载其他模块的类方法（def），主要用于简化导入路径或统一接口。您需要在 __init__.py 中使用 from ... import ... 语法导入包含该类的模块，然后便可直接调用该 def。 [1, 2] 
以下是具体的加载与使用方式：
### 假设文件结构
假设您有一个名为 mypackage 的包，目录结构如下：
``` shell
mypackage/
├── __init__.py
└── mymodule.py   # 定义了 class MyClass 和 def my_method
```
### 1.3.1 核心加载步骤
在 mypackage/__init__.py 中，您可以通过以下方式加载和暴露该方法：
``` python
# 方法一：将该方法直接导入到 __init__.py 的命名空间中
from .mymodule import MyClass

# 提取 MyClass 中的 def (假设方法名为 my_method)
# 通常通过实例化类来调用
my_method = MyClass().my_method 
#或者如果 my_method 是类方法 (@classmethod) 或静态方法 (@staticmethod)
my_method = MyClass.my_method
```
### 1.3.2 实战应用示例
在 mymodule.py 中：
``` python
class MyClass:
    def my_method(self):
        print("执行了 my_method")
```
在 mypackage/__init__.py 中加载并重新导出：
``` python
# 1. 导入包内的模块
from .mymodule
import MyClass
# 2. 实例化类并直接暴露其中的 def (简化调用)
run_my_method = MyClass().my_method
```
在外部主程序中使用：
``` python
# 此时调用 mypackage 下的 def，不需要再逐层 import
from mypackage import run_my_method

run_my_method()  # 输出: 执行了 my_method
```
### 1.3.3 为什么这样做？

* 简化调用：隐藏深层的文件结构，提供类似 from mypackage import run_my_method 的扁平化引用。
* 控制接口：通过 __all__ 变量控制允许被 * 导入的内容。 [1, 3, 4] 






