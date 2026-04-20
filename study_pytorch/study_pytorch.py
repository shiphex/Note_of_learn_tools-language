# import torch
# import torch.version
# import torch.nn as nn

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


## .transpose 与 .permute
'''
# 使用transpose交换维度
# 创建一个二维张量
x = torch.randn(2, 3)
print("原始张量:\n", x)
# 使用transpose交换维度
x_transposed = x.transpose(0, 1)
print("使用transpose交换维度:\n", x_transposed)

# 使用permute重新排列维度
# 创建一个三维张量
y = torch.randn(2, 3, 4)
print("原始三维张量:\n", y)
# 使用permute重新排列维度
y_permuted = y.permute(2, 0, 1)
print("使用permute重新排列维度:\n", y_permuted) 
'''


## torch.all() 与 torch.all()
'''
a = torch.tensor([1, 1, 1])
torch.all(a == 1)   # True
print(torch.all(a == 1))

b = torch.tensor([1, 0, 1])
torch.all(b == 1)   # False
print(torch.all(b == 1))
'''


## PyTorch中矩阵乘法
'''
# 创建两个张量
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[2, 2], [2, 2]])
# 使用*进行元素逐个相乘
result1 = a * b
print(result1)
# 使用torch.mul进行元素逐个相乘
result2 = torch.mul(a, b)
print(result2)

# 创建两个矩阵
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[7, 8], [9, 10], [11, 12]])
# 使用@进行矩阵乘法
result1 = a @ b
print(result1)
# 使用torch.mm进行矩阵乘法
result2 = torch.mm(a, b)
print(result2)
'''


## torch.triu()
'''
a = torch.randn(3, 3)
a_1 = torch.triu(a)
a_2 = torch.triu(a, diagonal=1)
a_3 = torch.triu(a, diagonal=-1)
print(a_1)
print(a_2)
print(a_3)
# 
b = torch.randn(4, 6)
b_1 = torch.triu(b)
b_2 = torch.triu(b, diagonal=1)
b_3 = torch.triu(b, diagonal=-1)
print(b_1)
print(b_2)
print(b_3)
# 保留上三角区域和主对角线
c = torch.randn(3, 3)
c_0 = c.triu(0)
c_1 = c.triu(1)
c_2 = c.triu(2)
c_3 = c.triu(-1)
print(c_0)
print(c_1)
print(c_2)
print(c_3)
'''


## torch.nn.ModuleList

import torch
import torch.nn as nn
'''
class MyModule(nn.Module):
  def __init__(self):
    super().__init__()
    # 创建 10 个线性层
    self.linears = nn.ModuleList([nn.Linear(10, 10) for _ in range(10)])

  def forward(self, x):
    for i, layer in enumerate(self.linears):
        x = self.linears[i // 2](x) + layer(x)
    return x


model = MyModule()
print(model)
'''
# 动态创建模型
"""
动态神经网络模型

该类用于创建一个具有指定层数的全连接神经网络，每层都有ReLU激活函数
"""
class DynamicModel(nn.Module):
  """
  初始化动态神经网络模型
  
  Args:
      num_layers (int): 隐藏层的数量
      in_size (int): 输入特征的维度
      hidden_size (int): 隐藏层的神经元数量
      out_size (int): 输出层的神经元数量
  """
  def __init__(self, num_layers, in_size, hidden_size, out_size):
    super().__init__()
    # 存储网络层
    layers = []
    # 构建隐藏层，每层包含线性层和ReLU激活函数
    for _ in range(num_layers):
      layers.append(nn.Linear(in_size, hidden_size))  # 线性变换层
      layers.append(nn.ReLU())  # ReLU激活函数
      in_size = hidden_size  # 更新输入大小为当前隐藏层大小
    # 添加输出层
    layers.append(nn.Linear(hidden_size, out_size))
    # 将层列表转换为ModuleList，以便PyTorch能够正确跟踪参数
    self.layers = nn.ModuleList(layers)

  """
  前向传播方法
  
  Args:
      x (torch.Tensor): 输入张量
      
  Returns:
      torch.Tensor: 模型输出
  """
  def forward(self, x):
    # 依次通过每一层
    for layer in self.layers:
      x = layer(x)
    return x

# 创建一个具有3个隐藏层、输入维度为10、隐藏层大小为20、输出维度为1的模型
net = DynamicModel(3, 10, 20, 1)
# 打印模型结构
print(net)