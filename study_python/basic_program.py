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


