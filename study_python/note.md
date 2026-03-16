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