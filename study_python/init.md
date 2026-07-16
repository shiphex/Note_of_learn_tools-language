
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




## 2.1 module 和 package 的导入原理

### 2.1.1 module 和 package 的概念

1. module 在 python 中算一个组织单位，独立构成一个命名空间，本身是一个 Python object。
   - 在这个 Python object 中可以有其他 Python object。
   - 在实际应用中，一个 module 通常对应一个.py 文件。 
   - module 是一个运行时的 object，保存在**内存**里。
   - module 是 python 级别的概念，文件是操作系统级别的概念，需要通过 import 导入从一个文件中生成一个 module。

2. package 是一个特殊的 module，在 python 中和 module 的功能几乎一样，但多了一个 __path__ 属性。
   - package 在操作系统层级对应一个文件夹（目录），内部可有多个文件夹和文件，故其内部可有多个 subpackage 和 module。
   - 无论 package 中是否有 __init__.py 文件，它都是一个 package。


## 2.2 import module 语句

### 2.2.1 import 的作用
将文件或文件夹变成一个 python 的 module 或 package 的过程。


### 2.2.2 import module 的导入流程
目录结构：
``` shell
study_python\init_code\
├── expemple.py
├── test.py
└── 
```

例如：在 expemple.py 中，我们导入了 test.py 文件。通过 import test 将 test.py 变成一个 module。
``` python
# expemple.py
import test
```
``` python
# test.py
```

在 import test 时会发生如下操作：
1. 使用 `test` 这个字符串，作为名字来寻找 module。
2. 检查缓存中是否有叫 `test` 的 module 已经被读取。
   - 如果有，直接将该 module 赋值给 `test`。
   - 如果没有，就需要寻找名字叫 `test` 的 module。
3. 先检查该名字是否为一个 built-in module（python 自带的 module：sys、os、math、random 等）。
4. 如果不是 built-in module，就会在几个文件夹下寻找被 Load 成 test 的文件（最常见的是 test.py 文件）。
   - 这些文件被保存到了 sys.path 中（通过 sys.path 来查看）。
   - 在寻找时会按 sys.path 输出的顺序查找（故会先从当前目录查找）。
   - 一旦找到就不再寻找，需注意命名冲突问题。
   ``` python
   >>> sys.path                                                                  
   
   # 第一个 ' ' 是当前目录，其他目录是 python 安装目录下的文件夹。
   # site-packages 是 pip install 安装的 module 所在的文件夹。
   ['', 'D:\\APP\\Anaconda\\python311.zip', 'D:\\APP\\Anaconda\\DLLs', 'D:\\APP\\Anaconda\\Lib', 'D:\\APP\\Anaconda', 'D:\\APP\\Anaconda\\Lib\\site-packages', 'D:\\APP\\Anaconda\\Lib\\site-packages\\win32', 'D:\\APP\\Anaconda\\Lib\\site-packages\\win32\\lib', 'D:\\APP\\Anaconda\\Lib\\site-packages\\Pythonwin']
   ```
5. 在寻找到符合命名的文件后，就会在一个单独的命名空间中运行这个文件（建立一个 module，在 module 中定义并执行文件中的代码）。
6. 在 import test 语句后，就会在 test 的 module 中给全部的 object 定义自己的 module。
7. 更新缓存，未来若有其他的文件 import 这个 module，就会直接从缓存中获取（不会重复执行 test.py 中的代码）。
8. 把 module test 赋值给变量 test。
9. 可以在 expemple.py 中使用 test.A 来调用 test.py 中的 A 类。
   ``` python
   # expemple.py
   import test

   print(test)
   print(test.A)
   ```
10. 多次 import test 语句，不会重复执行 test.py 中的代码。

### 2.2.3 import module 的变量赋值

1. 在 `import test` 语句中，执行了这两个任务：
   - 根据字符串 `test` 来寻找 module。
   - 将这个 module 保存到变量 `test` 里。

2. `import test as t`：
   - 根据字符串 `test` 来寻找 module。
   - 将这个 module 保存到变量 `t` 里。

3. 对整个 module 不感兴趣，只要其中的一个 object（`from test import A`）：
   - 根据字符串 `test` 来寻找 module，并依然会 load 这个 module，并刷新缓存。
   - 但不会将这个 module 赋值给一个变量。
   - 在这个 module 中找到名字为 `A` 的 variable，把这个 variable 赋值给当前 module 下的变量 `A`。

4. `from test import A as MyA`：
   - 将 `A` 保存到 `MyA`。


## 2.3 导入 package

`mypackage` 是一个文件夹，通过使用 `import mypackage` 来导入 mypackage 这个 package。
- 在执行 `import mypackage` 时，解释器会在 `mypackage` 文件夹中寻找 `__init__.py` 文件。
- 如果没有就不会运行额外的代码，如果有就会运行 `__init__.py` 文件中的代码（也只会运行 __init__.py 文件中的代码）。

1. 
  ``` python 
  # expemple.py
  import mypackage
  print(mypackage)
  print(mypackage.B)
  print(dir(mypackage)) # 查看 mypackage 中的所有 object（只会有 __init__.py 文件中的 object）
  ```
- 即：在运行 `import mypackage` 就是在单独的命名空间里运行 `mypackage` 文件夹中的 `__init__.py` 文件。
- 然后用这个命名空间构成一个 module，这个 module 就是 mypackage。

2. import 一个 package 下的一个 module，需要通过目录 `import mypackage.mymodule` 来导入。
   - 若为多级目录，需要通过多个点来表示。例如：`import mypackage.subpackage.mymodule`。
   - 寻找过程与 `import test` 相同。
   - 这样做会 load 整个 mypackage 并更新缓存。
   - 并在 mypackage 中增加一个属性 `mymodule`，指向 mymodule 这个 module。
   ``` python
   # expemple.py
   import mypackage.mymodule
   print(mypackage.mymodule)
   print(dir(mypackage.mymodule))   # 这样可以查看 mymodule 中的所有 object，但不会查看 __init__.py 文件中的 object。
   print(mypackage)
   print(dir(mypackage))            # 查看 mypackage 中的所有 object（只会有 __init__.py 文件中的 object）
   ```
   - 会将 package 赋值给这个 package 名字的变量，


3. `import mypackage.mymodule as m`：
   - 会把最尾端的 module 赋值给变量 m。
   - **`mypackage` 这个变量并不存在**


absolute import：根据一个确定的 string 来导入 module。
relative import：根据当前 module 的位置来导入 module。


## 2.4 相对导入

在一个 package 下的不同 module 之间相互引用，可以使用相对导入来导入其他 module。这些 module 之间的相对关系比较稳定（package 可能会改名，package 可能被放到其他 package 下，导致 module 的绝对路径被改变）
- × `from mypackage.util import f` → 如果 `mypackage` 改名就没办法 import；或者如果这个 `util` 在package 下的多级目录中，就不好找到该 module。
- √ `from .util import f` → relative import：`.util` 就是在当前 module 所在的 package 中寻找 `util` module。
  - 原理：
    - 每一个 relative import 都是先找到它的绝对路径，然后再 import 这个 module。通过使用 import 的 module 的 package 计算绝对路径（`mypackage.mymodule.__package__`）。
    - 若直接运行 `python mypackage\mymodule.py`，则 `from .util import f` 会报错。因为此时 `mypackage\mymodule.py` 被当作 `main module` load 进来，它并不属于任何一个 package ，于是在 `relative import` 时没有办法转换成 `absolute import`。
    - `relative import` 只能在 package 里面使用；且必须在 package 里面的 module 使用时，并且这个 module 被导入的时候必须跟着 package 一起导入。否则会报错。
- 当想导入的 module 不在同一个文件夹下时，可使用两个点 `..` 来表示上一级目录。例如在 `mypackage\subpackage\submodule.py` 中使用：`from ..util import f`。



## 2.5 __ALL__ 属性

### 2.5.1 __ALL__ 属性的作用
1. 若在 `__init__.py` 文件中使用 `from .mymodule import f`，则 `f` 就会被导入到 `mypackage` 这个 module 中。
``` python
from .mymodule import f

```

在 `expemple.py` 中使用 `mypackage.f()` 来调用 `f` 函数。
``` python
import mypackage
print(mypackage.f())
```

2. 若在 `__init__.py` 文件中使用 `from .mymodule import f`，并使用 `__all__ = ['f']`。
``` python
from .mymodule import f
__all__ = ['f']
```

在 `expemple.py` 中使用 `*` 来导入 `__all__` 中的 object。
``` python
from mypackage import *
print(f())
```


### 2.5.2 __ALL__ 延迟加载
在运行项目之初一次性加载全部依赖将相当消耗时间，对于一些包，可以选择延迟加载：
``` python
# mypackage/_init_.py

all_=["User"]
def _getattr_(name):
   if name =="User":
      from.utils.modelimportUser
      returnUser
   raise AttributeError(f"No {name}")
```

