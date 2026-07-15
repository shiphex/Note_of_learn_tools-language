# 内建函数
Python 提供了大量内置函数（Built-in Functions），无需导入任何库即可直接使用。 这些函数覆盖了数据类型转换、数学计算、迭代操作、反射机制等常见场景，是每个 Python 初学者必须掌握的基础工具。

为什么要掌握内置函数？
- 减少代码量：一行顶多行（例如 sum()、max()）
- 提升可读性：语义明确，比手写逻辑更清晰
- 性能更优：底层 C 实现，通常比 Python 循环更快

常见分类：
- 数值计算：abs()、round()、min()、max()、sum()
- 类型转换：int()、float()、str()、list()、tuple()
- 迭代与函数式：code>map()、filter()、zip()、enumerate()
- 反射与对象：type()、isinstance()、getattr()、setattr()
- 输入输出：print()、input()、open()


## getattr() 函数
getattr() 是 Python 中用于获取对象属性值的内置函数。

getattr() 允许我们动态地访问对象的属性，而不是使用点号（.）静态访问。这在处理未知属性的情况下非常有用。

单词释义： getattr 是 get attribute（获取属性）的缩写。

### 基本语法与参数
语法格式：
- getattr(object, name)
- getattr(object, name, default)

参数说明：
- 参数 object：
  - 类型： 任意对象
  - 描述： 要获取属性的对象。
- 参数 name：
  - 类型： 字符串
  - 描述： 属性名称。
- 参数 default（可选）：
  - 类型： 任意值
  - 描述： 如果属性不存在，返回的默认值。

函数说明：
- 返回值： 返回属性的值。
- 异常： 如果属性不存在且没有默认值，会抛出 AttributeError。

示例：
```python
class Person:
    def __init__(self):
        self.name = "Tom"

p = Person()

# 获取存在的属性
print(getattr(p, "name", "未知"))  # 输出: Tom

# 获取不存在的属性（带默认值）
print(getattr(p, "age", 0))        # 输出: 0
print(getattr(p, "city", "北京"))  # 输出: 北京

# 获取不存在的属性（不带默认值）
try:
    print(getattr(p, "gender"))
except AttributeError as e:
    print(f"属性不存在: {e}")

################
# 动态选择属性
data = {"name": "Tom", "age": 20}
field = "name"
print(getattr(data, field))  # 通过字符串访问

# 与 setattr 配合
class Person:
    pass

p = Person()

# 动态设置属性
fields = ["name", "age", "city"]
values = ["Tom", 20, "Beijing"]

for field, value in zip(fields, values):
    setattr(p, field, value)

# 动态获取所有属性
for field in fields:
    print(f"{field}: {getattr(p, field)}")

# hasattr 配合 getattr
if hasattr(p, "name"):
    print(f"名字是: {getattr(p, 'name')}")
```


## .iterdir() 方法
.iterdir()：Path 的内置方法，遍历该目录下所有直接子项（文件 + 文件夹）；

返回迭代器，里面每个元素依然是 Path 对象；


## sorted(...) 函数
sorted() 接收返回的路径对象列表，默认按照路径字符串字典序排序（文件名按字母顺序）；