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

v0.2
