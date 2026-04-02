## torch.randn
- `torch.randn` 函数用于创建一个随机张量，其元素服从`标准正态分布`。 
- 输入：
  -  size (int...) – 定义输出张量形状的整数序列。可以是可变数量的参数，也可以是列表或元组之类的集合。
- 输出：
  - 返回一个包含随机数的张量，形状由输入参数指定。
```python
import torch

torch.randn(*size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False)
```


## nn.Linear
- `nn.Linear` 函数用于创建一个全连接层，即一个线性层。  
- 这个层会对输入数据应用一个线性变换，即$y = xA^T + b$，其中x是输入数据，A是层的权重，b是偏置项。  
- 它接收一个输入张量，将其映射到一个输出张量。  
- 输入：
  - in_features (int) 输入特征的数量，即输入张量的最后一个维度的大小。
  - out_features (int) 输出特征的数量，即输出张量的最后一个维度的大小。
  - bias (bool) 是否添加偏置项，默认为True。

```python
import torch
import torch.nn as nn

class torch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)
```


## nn.Dropout
- 在训练期间，以概率 `p` 随机将输入张量中的一些元素归零。  
- 被置零的元素在每次前向传播调用时都是独立选择的，并从伯努利分布中采样得出。  
- 每个通道在每次前向传播调用时都将被独立地置零。  
- 此外，在训练期间，输出会按 $\frac{1}{1-p}$ 的比例进行缩放。这意味着在评估过程中，该模块仅执行恒等映射函数。
- 参数：
  - p (float) – 元素被归零的概率。默认值：0.5
  - inplace (bool) – 如果设置为 True，则该操作将就地执行。默认值：False
- 输出：
  - 输出与输入具有相同形状的张量
``` python
import torch
import torch.nn as nn

class torch.nn.Dropout(p=0.5, inplace=False)[source]
```


## .view
- `view` 函数用于重新调整张量的形状。
``` python
import torch

# 如果需要自动计算某一维度的大小，可以将该维度设置为 -1。 示例：
tensor.view(-1, 8)  # 表示自动计算第一维度的大小，使总元素数量保持一致。

# 将一个形状为 (4, 4) 的 Tensor 调整为一维：
tensor.view(-1)

# 将一个一维 Tensor 调整为 (2, 8)：
tensor.view(2, 8)

# 若无指定维度，.view()中所有维度的大小都必须与原始张量的元素数量相等，即.view()中所有维度数相乘等于原始张量的元素数量。
a1 = torch.arange(0,16)
a2 = a1.view(2, 2, 2, 2)        # 正确，2*2*2*2 = 16
a3 = a1.view(2, 4, 2)           # 正确，2*4*2 = 16
a4 = a1.view(2, 2, 2)           # 错误，2*2*2 = 8，与原始张量的元素数量不相等
```


## torch.cat
在给定维度上连接 tensors 中的给定张量序列。所有张量必须具有相同的形状（连接维度除外），或者是一个大小为 (0,) 的一维空张量。
- 参数：
  - tensors (Tensors 的序列) – 提供的非空张量必须具有相同的形状（连接维度除外）。
  - dim (int, 可选) – 连接张量的维度。
- 关键字参数：
  - out (Tensor, optional) – 输出张量。
- 输出：
  - 连接后的张量。
``` python
import torch

torch.cat(tensors, dim=0, *, out=None)
```


## .transpose 与 .permute
- `transpose` 函数用于交换张量的两个维度。它接受两个参数，分别是要交换的维度的索引。
- `permute` 函数用于重新排列张量的维度。它接受一个参数，即一个整数序列，表示新的维度顺序。
``` python
import torch
# 如果你有一个形状为(2, 3)的张量，使用x.transpose(0, 1)将会得到一个形状为(3, 2)的张量

# 有一个形状为(2, 3, 4)的三维张量，使用y.permute(1, 0, 2)将会得到一个形状为(3, 2, 4)的张量
```


## torch.all() 与 torch.all()
- torch.any()：只要有一个为 True，就返回 True
- torch.all()：必须全部为 True，才返回 True


## 

# 内存连续性问题？