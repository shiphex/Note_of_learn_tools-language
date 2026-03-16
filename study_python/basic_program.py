# #####################################################################
# Learn Python programming language.
# Date: 2026-03-15
# auther: Hao Zhou
# #####################################################################


# This is a basic Python program that prints 
# 基础输出
'''
"Hello, World!" and "你好，世界！" to the console.
print("Hello, World!")
print("你好，世界！")  
'''


# This is a simple for indentation example.
# 缩进控制类
'''
if True:
    print("Ture")
else:
    print("False")
'''


# This is a example of line continuation using backslash for break line.
# 反斜杠用于换行
'''
item_A = 1
item_B = 2
item_C = 3

total = item_A + \
        item_B + \
    item_C
print("Total:", total)
'''


# This is a example of using parentheses for line continuation.
# 使用括号进行换行
"""
word = 'word'
sentence = "这是一个句子"
paragraph = '''这是一个段落，
可以包含多行文本。'''
print("Word:", word)
print("Sentence:", sentence)
print("Paragraph:", paragraph)
"""


# This is a example of using semicolon to separate multiple statements on the same line.
# 使用分号分隔同一行的多个语句
'''
import sys; x = 'Hello, world!'; sys.stdout.write(x + '\n')
'''

# this is a example of printing break line
# 换行输出
'''
A = "a"; B = "b"
# 换行输出
print (A)
print (B)

print ('---------')
# 不换行输出
print (A),
print (B)

print ('---------')
# 不换行输出
print (A, B)
'''


# this is a example of waiting for user input
# 等待用户输入
'''
input_buffer = input('请输入一些内容,回车以结束：' + '\n')
print('你输入的内容是：', input_buffer)
input('按回车键以退出' + '\n')
'''


# This is a example of multiple statements in a code block.
# 多语句代码段
'''
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
'''    

# this a example of variables assignment and multiple variables assignment
# 多变量赋值
'''
counter = 100   # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"   # 字符串
 
print (counter)
print (miles)
print (name)
print ('---------')

a = b = c = 1
print (a, b, c)
a, b, c = 1, 2000.0, "John"
print (a, b, c)
'''


# This is a example of data types and type checking.
# 数据类型及类型检查
'''
# 定义变量
x = 9               # 整形
y = 3.1415926       # 浮点型
name  = "Alice"     # 字符串
is_active = True    # 布尔型
# 查看数据类型
print(type(x))
print(type(y))
print(type(name))
print(type(is_active))

# 定义变量
a, b, c, d = 20, 5.5, True, 4+3j
# 查看数据类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(isinstance(a, int))
'''

# This is a example of string operations.
# 字符串操作
'''
str = "Python"
print(str)          # 打印整个字符串
print(str[0:-1])    # 打印字符串从第一个到倒数第二个字符（不包含倒数第一个字符，即索引为-1的字符）
print(str[0])       # 打印第一个字符
print(str[2:5])     # 打印第三个到第五个字符（不包含索引为5的字符）
print(str[2:])      # 打印从第三个字符开始到末尾
print(str * 2)      # 打印字符串两遍
print(str + "test") # 打印字符串和test拼接在一起
'''

# This is a example of special characters in strings.
# 特殊字符
'''
print('Py\nthon')
print(r'Py\nthon')
'''


# Tihs is a example of word and character access in strings.
# 字符串中的单词和字符访问
'''
word = 'Python'
print(word[0] + word[5])
print(word[-1], word[-6])

'''


# This is a example of boolean type and operations.
# 布尔类型的值和类型
'''
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
'''


# This is a example of list operations.
# 列表操作
'''
list = [ 'abcd', 786 , 2.23, 'Python', 70.2 ]  # 定义一个列表
tinylist = [123, 'Python']

print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist) # 打印两个列表拼接在一起的结果

a = [1, 2, 3, 4, 5, 6]

a[0] = 9
a[2:5] = [13, 14, 15]
print(a)

a[2:5] = []   # 将对应的元素值设置为 []
print(a)

letters = ['P', 'y', 't', 'h', 'o', 'n']
print(letters[1: 4: 2]) #从第二个参数到第五个参数，以二为步长截取输出
'''

# This is a example of tuple operations.
# 元组操作
'''
tuple = ( 'abcd', 786 , 2.23, 'Python', 70.2  )
tinytuple = (123, 'Python')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
'''

# This is a example of set operations.
# 集合操作
'''
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
'''

# This is a example of dictionary operations.
# 字典操作
'''
dict = {}
dict['one'] = "1"
dict[2]     = "two"

tinydict = {'name': 'baidu','code':1, 'site': 'www.bing.com'}

tinydict['name'] = 'bing'

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
'''


# This is a example of bytes type and operations.
# bytes类型和操作
'''
x = bytes("hello", encoding="utf-8")
x = b"hello"
y = x[1:3]          # 切片操作，得到 b"el"
z = x + b"world"    # 拼接操作，得到 b"helloworld"
print(z)

x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")
'''


# This is a example of type conversion.
# 类型转换
'''
num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))
'''


# This is a example of assignment expression using the walrus operator.
# 海象运算符赋值表达式
'''
# 在这个示例中，赋值表达式可以避免调用 len() 两次:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
# 传统写法
n = 10
if n > 5:
    print(n)
# 使用海象运算符
if (n := 10) > 5:
    print(n)
'''


# This is a example of structural pattern matching using match-case.
# 结构化模式匹配 match-case
'''
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
'''

# This is a example of for loops.
# for 循环示例
'''
sites = ["Baidu", "Google","Bing","Taobao"]
for site in sites:
    print(site)

word = 'Bing'
for letter in word:
    print(letter)

#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)
'''


# This is a example of for loop with break and else.
# 带有 break 和 else 的 for 循环示例
'''
sites = ["Baidu", "Google","Bing","Taobao"]
for site in sites:
    if site == "Bing":
        print("必应")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
'''


# This is a example of while loop with continue.
# 带有 continue 的 while 循环示例
'''
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
'''


# This is a example of pass statement in loops.
# 循环中的 pass 语句示例
'''
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
'''


# This is a example of range() function usage.
# range() 函数用法示例
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