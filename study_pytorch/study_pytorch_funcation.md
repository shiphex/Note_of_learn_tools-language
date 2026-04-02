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


