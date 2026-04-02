import torch
import torch.version
import torch.nn as nn

# print(torch.__version__)
# print(torch.version.cuda)  #输出CUDA版本
# print(torch.cuda.is_available())  #输出为True，则安装无误


## torch.randn
# 创建一个随机张量，形状为(3, 4)，元素服从标准正态分布
'''
random_tensor = torch.randn(3, 4)
print(random_tensor)
'''


## nn.Linear
'''
# 创建一个全连接层(线性层)
linear_layer = nn.Linear(3, 4)
# 创建一个随机输入张量，
input_tensor = torch.randn(5, 3)
# 通过全连接层传递输入张量
output_tensor = linear_layer(input_tensor)
# 打印张量
print("输入张量的形状:", input_tensor.shape)
print(input_tensor)

print("输出张量的形状:", output_tensor.shape)
print(output_tensor)
'''


## nn.Dropout
'''
# 创建一个Dropout实例，设置丢弃概率为0.2
dropout = nn.Dropout(p=0.2)

# 创建一个随机张量作为输入
x = torch.randn(10, 2)

# 应用Dropout
y = dropout(x)

# 输出结果
print("输入:\n", x)
print("Dropout后的输出:\n", y)
'''


## .view
'''
a1 = torch.arange(0,16)
print(a1)
# 将a1调整形状
a2 = a1.view(16, -1)
print(a2)
a3 = a2.view(-1, 4)
print(a3)
a4 = a3.view(2, 2, 2, 2)
print(a4)
a5 = a4.view(2, 4, 2)
print(a5)
'''


## torch.cat
'''
A = torch.ones(2, 3)        # 创建一个全1的张量，形状为(2, 3)
B = 2 * torch.zeros(4, 3)   # 创建一个全0的张量，形状为(4, 3)，元素乘以2

# 沿着第0维（行）拼接A和B
C = torch.cat((A, B), dim=0)
print(C)

# 沿着第1维（列）拼接A和B
D = torch.cat((A, B), dim=1)        # 错误，A和B的最后一个维度不匹配
print(D)

# dim=-1 表示在最后一个维度上进行拼接
# E = torch.cat((A, B), dim=-1)         # 错误，A和B的最后一个维度不匹配
# print(E)
'''


