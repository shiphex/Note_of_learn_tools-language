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



