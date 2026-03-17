# <center>python语法学习笔记</center>
# 基础语法

## 注释
+ 单行注释，使用`#`
+ 多行注释，使用`'''`、`"""`
``` python
# 注释使用“# ”

"""
多行注释
"""
```


## 保留字符
||||
|:----:     |:----:     |:----: |
|and	    |exec	    |not    |
|assert	    |finally	|or     |
|break	    |for	    |pass   |
|class	    |from	    |print  |
|continue	|global	    |raise  |
|def	    |if	        |return |
|del	    |import	    |try    |
|elif	    |in	        |while  |
|else	    |is	        |with   |
|except	    |lambda	    |yield  |


## 行、缩进、控制类/代码块
不使用```{}```控制类/代码块，使用**缩进**写模块，但所有缩进个数得相同


## 空行
可任意空行，python中空行并不表示语法，仅仅为了代码易读性而空行


## 多行代码
使用``\``将一行语句分为多行显示
``` python
total = item_A + \
    item_B + \
    item_C
```
> note:  
一行代码多行显示的时候，不需要管缩进字符是否一致


## 字符串
可使用`'`、`"`、`'''`、`"""`表示字符串，引号开始与结束必须类型相同  
只有`"""`可以分行书写，其他需要使用`\`


## 一行显示多条语句
使用`;`分割一行中的多条语句
``` python
import sys; x = 'Hello, world!'; sys.stdout.write(x + '\n')
```

## print输出
+ 默认输出：不换行
+ 使用`,`输出：换行
``` python
# 换行输出
print A
print B

# 不换行输出
print A,
print B

# 不换行输出
print A, B
```


## 等待用户输入
输入任意
``` python
input_buffer = input('请输入一些内容,回车以结束：' + '\n')
print('你输入的内容是：', input_buffer)
input('按回车键以退出' + '\n')
```


## 多语句代码段
`if`、`while`、`def`和`class`的复合语句，首行以关键字开始，以冒号(`:`)结束，行后代码(块)构成代码组。
``` python
state_flag_A = input('请输入State A的状态（数字）：' + '\n')
if state_flag_A == 1:
    print("State A is 1")
    print("Executing code block for State A")
elif state_flag_A:
    print("State A is not 1, but it is not empty")
    print("Executing code block for State A")
else:
    print("State A is empty or zero")
    print("Executing code block for State A")
```


## 命令行参数
通过`python -h`查看


# 变量类型
## 变量赋值
+ python不需要给变量的类型声明
+ 变量在使用前必须被赋值，被赋值后才会被创建
``` python
counter = 100   # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"   # 字符串
 
print (counter)
print (miles)
print (name)
```


## 多变量赋值
``` python
a = b = c = 1

a, b, c = 1, 2000.0, "John"
```


## 标准数据类型
+ Numbers（数字）
+ String（字符串）
+ List（列表）
+ Tuple（元组）
+ Dictionary（字典）


## 查看变量类型
``` python
# 定义变量
x = 9               # 整形
y = 3.1415926       # 浮点型
name  = "Alice"     # 字符串
is_active = Ture    # 布尔型

# 查看数据类型
print(type(x))
print(type(y))
print(type(name))
print(type(is_active))
```

## Numbers（数字）
+ int
+ float
+ bool
+ complex(复数)

使用`type()`或`isinstance()`判断数字类型

``` python
a, b, c, d = 20, 5.5, True, 4+3j

# 查看数据类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(isinstance(a, int))   
```

## del语句删除一些对象引用
``` python
del var
del var_a, var_b
```

> note:  
> type()不会认为子类是一种父类类型。  
> isinstance()会认为子类是一种父类类型。  

## bool
+ Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加  

## 数值运算
```
>>> 5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32
```
+ 在混合计算时，Python会把整型转换成为浮点数
+ 一个变量可以通过赋值指向不同类型的对象

## complex(复数)
复数由实数部分和虚数部分构成，可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。


## 字符串
+ 字符串使用`'`或`"`括起来
+ 使用`\`反斜杠转义特殊字符

### 变量索引
||||||||
|   :---:   |:---:|:---:|:---:|:---:|:---:|:---:|
|从后面索引：|-6|-5|-4|-3|-2|-1|
|从前面索引：|0|1|2|3|4|5|
|字符串：    |`P`|`y`|`t`|`h`|`o`|`n`|
|从前面截取：|1|2|3|4|5|6|
|从后面截取：|-6|-5|-4|-3|-2|-1|

+ 字符串的截取语法格式`变量[头下标:尾下标]`
+ `头下标`为`索引值`，`尾下标`为`截取值`
+ `索引值`以 0 为开始值，-1 为从末尾的开始位置
+ 输出时不包含`截取值`的字符

``` python
str = "Python"

print(str)          # 打印整个字符串
print(str[0:-1])    # 打印字符串从第一个到倒数第二个字符（不包含倒数第一个字符，即索引为-1的字符）
print(str[0])       # 打印第一个字符
print(str[2:5])     # 打印第三个到第五个字符（不包含索引为5的字符）
print(str[2:])      # 打印从第三个字符开始到末尾
print(str * 2)      # 打印字符串两遍
print(str + "test") # 打印字符串和test拼接在一起
```

### 特殊字符
+ 反斜杠 \ 转义特殊字符
+ 在字符串前面添加一个 r，表示原始字符串
``` python
print('Py\nthon')
print(r'Py\nthon')
```

### 字符
+ Python 没有单独的字符类型，一个字符就是长度为1的字符串
``` python
word = 'Python'
print(word[0] + word[5])
print(word[-1], word[-6])
```

> note:
> Python 字符串不能被改变。  
> 向一个索引位置赋值，比如 word[0] = 'm' 会导致**错误**。  



## bool（布尔类型）
+ 布尔类型只有两个值：`True` 和 `False`
+ `bool` 是 `int` 的子类
+ 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 `True` 视为 `1``，False` 视为 `0`。
+ 可以和逻辑运算符一起使用，包括 `and`、`or` 和 `not`
+ 可以被转换成其他数据类型，比如整数、浮点数和字符串，`True` 会被转换成 `1`，`False` 会被转换成 `0`
+ `bool()`函数可将其他类型转换成布尔值。 `False`：`None`、`False`、零 `(0、0.0、0j)`、`空序列`（如 ''、()、[]）和`空映射`（如 {}）

``` python
# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))   # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2) # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")
   
if not False:
    print("This will also always print")
   
x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
```


## List（列表）(类似于结构体)
+ 列表中元素的类型可以不相同
+ 支持数字，字符串甚至可以包含列表（所谓嵌套）
+ 列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
+ 列表是写在方括号 [] 之间、用逗号分隔开的元素列表

``` python
变量[头下标:尾下标]
```

> note:  
> 操作与字符串一致
> 索引值以 0 为开始值，-1 为从末尾的开始位置。
> 加号 + 是列表连接运算符，星号 * 是重复操作。
> 与Python字符串不一样的是，列表中的元素是可以改变的

``` python
list = [ 'abcd', 786 , 2.23, 'Python', 70.2 ]  # 定义一个列表
tinylist = [123, 'Python']

print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist)  # 打印两个列表拼接在一起的结果

a = [1, 2, 3, 4, 5, 6]

a[0] = 9
a[2:5] = [13, 14, 15]
print(a)

a[2:5] = []   # 将对应的元素值设置为 []
print(a)
```

### 步长截取
列表截取可以接收第三个参数,第三个参数为截取的步长

``` python
letters = ['P', 'y', 't', 'h', 'o', 'n']
print(letters[1: 4: 2]) #从第二个参数到第五个参数，以二为步长截取输出
```


## Tuple元组
+ tuple的元素不可改变，但它可以包含可变的对象，比如list列表
+ 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
+ 元组写在小括号 () 里，元素之间用逗号隔开。
+ 元组也可以被索引和切片

``` python
tuple = ( 'abcd', 786 , 2.23, 'Python', 70.2  )
tinytuple = (123, 'Python')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
```

额外的语法规则:
``` python
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
```
> note:  
> string、list 和 tuple 都属于 sequence（序列）


## Set(集合)
+ 集合（Set）是一种**无序、可变**数据类型
+ 用于存储唯一的元素
+ **元素不会重复**，并且可以进行交集、并集、差集等常见的集合操作
+ 集合使用大括号 `{}` 表示，元素之间用逗号 `,` 分隔
+ 使用 set() 函数创建集合

> note:  
> 创建一个空集合必须用 `set()` 而不是 `{ }`，因为 `{ }` 是用来创建一个空字典

``` python
parame = {value01,value02,...}
# 或者
set(value)
```

``` python
sites = {'Google', 'Taobao', 'Tencent', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Tencent' in sites :
    print('Tencent 在集合中')
else :
    print('Tencent 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
```



## Dictionary（字典）
+ 字典是无序的对象集合
+ 无序的 `键(key) : 值(value) `的集合(`tinydict.keys()`:`tinydict.values()`)
+ 键(key)必须使用不可变类型
+ 键(key)必须是唯一的

``` python
dict = {}
dict['one'] = "1"
dict[2]     = "two"

tinydict = {'name': 'bing','code':1, 'site': 'www.bing.com'}

tinydict['name'] = 'wab'

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
```


## bytes类型
+ `bytes` 类型表示的是不可变的二进制序列
+ `bytes` 类型中的元素是整数值（0 到 255 之间的整数）
+ 可用`b`前缀创建 `bytes` 对象
+ 使用 `bytes()` 函数将其他类型的对象转换为 `bytes` 类型
+ `bytes()` 函数的第一个参数是要转换的对象，第二个参数是编码方式,，省略第二个参数，则默认使用 `UTF-8` 编码

``` python
x = bytes("hello", encoding="utf-8")
x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(z)

x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")
```

> note:  
> 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。  

# Python数据类型转换
|函数   |	描述|
|:---:|:---:|
|int(x [,base])|将x转换为一个整数|
|float(x)|将x转换到一个浮点数|
|complex(real [,imag])|创建一个复数|
|str(x)|将对象 x 转换为字符串|
|repr(x)|将对象 x 转换为表达式字符串|
|eval(str)|用来计算在字符串中的有效Python表达式,并返回一个对象|
|tuple(s)|将序列 s 转换为一个元组|
|list(s)|将序列 s 转换为一个列表|
|set(s)|转换为可变集合|
|dict(d)|创建一个字典。d 必须是一个 (key, value)元组序列。|
|frozenset(s)|转换为不可变集合|
|chr(x)|将一个整数转换为一个字符|
|ord(x)|将一个字符转换为它的整数值|
|hex(x)|将一个整数转换为一个十六进制字符串|
|oct(x)|将一个整数转换为一个八进制字符串|

## 隐式类型转换
自动完成，如整型、浮点型、复数型

## 显式类型转换
手动强制转换格式
``` python
num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))
```

# 运算符
+ 算术运算符
+ 比较（关系）运算符
+ 赋值运算符
+ 逻辑运算符
+ 位运算符
+ 成员运算符
+ 身份运算符
+ 运算符优先级

    - `:-`**海象运算符**，这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增运算符。
    ``` python 
    # 在这个示例中，赋值表达式可以避免调用 len() 两次:
    if (n := len(a)) > 10:
        print(f"List is too long ({n} elements, expected <= 10)")

    # 传统写法
    n = 10
    if n > 5:
        print(n)

    # 使用海象运算符
    if (n := 10) > 5:
        print(n)
    ```

## Python身份运算符
身份运算符用于比较两个对象的存储单元
+ `is` 是判断两个标识符是不是引用自一个对象，类似 `id(x) == id(y)`
+ `is not` 是判断两个标识符是不是引用自不同对象，类似 `id(x) != id(y)`

## Python运算符优先级
|运算符|描述|
|:---:|:---:|
|(expressions...), [expressions...], {key: value...}, {expressions...}|圆括号的表达式|
|x[index], x[index:index], x(arguments...), x.attribute|读取，切片，调用，属性引用|
|await x|await 表达式|
|**|乘方(指数)|
|+x, -x, ~x|正，负，按位非 NOT|
|*, @, /, //, %|乘，矩阵乘，除，整除，取余|
|+, -|加和减|
|<<, >>|移位|
|&|按位与 AND|
|^|按位异或 XOR|
|\||按位或 OR|
|in,not in, is,is not, <, <=, >, >=, !=, ==|比较运算，包括成员检测和标识号检测|
|not x|逻辑非 NOT|
|and|逻辑与 AND|
|or|逻辑或 OR|
|if -- else|条件表达式|
|lambda|lambda 表达式|
|:=|赋值表达式|



# 条件控制
+ if语句
``` python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
+ 每个条件后面要使用冒号 `:` 
+ 多重 if 语句逐级缩进
+ Python 中没有 `switch...case` 语句，但在 Python3.10 版本添加了 `match...case`
``` python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))
```

# 循环语句  

## `while` 循环
+ 一般形式
``` python
while 判断条件(condition)：
    执行语句(statements)……
循环外语句()……
```
+ 无限循环  
执行语句(statements)永远不会触及判断条件(condition)

+ while 循环使用 else 语句
``` python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

## for 语句
+ 一般格式  
for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串
``` python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

``` python
sites = ["Baidu", "Google","Bing","Taobao"]
for site in sites:
    print(site)

word = 'runoob'
for letter in word:
    print(letter)

#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)
```

+ for...else
``` python
for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码
```

+ break 语句  
`break` 语句用于跳出当前循环体，不会执行 `else` 子句  
``` python
sites = ["Baidu", "Google","Bing","Taobao"]
for site in sites:
    if site == "Bing":
        print("必应")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

+ continue 语句  
`continue` 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环 
``` python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
```

+ pass 语句  
pass 不做任何事情，一般用做占位语句，保持程序结构的完整性  
``` python
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
```

+ range() 函数  
遍历数字序列，range() 函数会生成数列
``` python
# 一般用法
for i in range(5):
    print(i)

# 指定区间
for i in range(5,9):
    print(i)

# 指定步长((甚至可以是负数)
for i in range(0, 10, 3):       # 步长为3
    print(i)
for i in range(-10, -100, -30): # 步长为-30
    print(i)

# 结合 range() 和 len() 函数，遍历序列的索引
a = ['Google', 'Baidu', 'Bing', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# 使用 range() 函数来创建一个列表
list(range(5))
```