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
# transpose(-2, -1)：把张量倒数第二个维度 和 最后一个维度 交换位置。

# 有一个形状为(2, 3, 4)的三维张量，使用y.permute(1, 0, 2)将会得到一个形状为(3, 2, 4)的张量
```


## torch.all() 与 torch.all()
- torch.any()：只要有一个为 True，就返回 True
- torch.all()：必须全部为 True，才返回 True


## PyTorch中矩阵乘法
- 元素逐个相乘：
  - `*`
  - torch.mul()
- 矩阵乘法:
  - @
  - torch.mm()


## torch.triu()
- 返回矩阵（二维张量）或矩阵批次 input 的上三角部分，结果张量 out 的其余元素设为 0。  
- 矩阵的上三角部分定义为对角线及其上方的所有元素。
- 参数：
  - input (Tensor) – 输入张量。
  - diagonal (int, optional) – 要考虑的对角线。
``` python
torch.triu(input, diagonal=0, *, out=None)

x.triu(1)   # 保留上三角区域
x.triu(0)   # 保留上三角区域和主对角线
x.triu(-1)  # 保留上三角区域、主对角线和下三角区域的第一条对角线
```


## PyTorch nn.ModuleList 用法
`torch.nn.ModuleList` 是 `PyTorch` 中的一个容器类，用于按列表形式存储多个子模块（`nn.Module` 对象），并确保它们被正确注册到模型中，从而参与 参数管理 和 自动求导。与普通 `Python list` 不同，`ModuleList` 中的模块会自动加入计算图并参与优化。

核心特性
- 自动参数注册：内部模块的权重和偏置会被模型识别。
- 灵活访问：支持索引、切片、迭代等操作。
- 动态构建：可在初始化或运行时添加模块。

基本示例
``` python
import torch
import torch.nn as nn

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
```

这里 `ModuleList` 像列表一样可迭代，但每个子模块都被注册，可参与训练。

动态构建网络
``` python
class DynamicModel(nn.Module):
  def __init__(self, num_layers, in_size, hidden_size, out_size):
    super().__init__()
    layers = []
    for _ in range(num_layers):
      layers.append(nn.Linear(in_size, hidden_size))
      layers.append(nn.ReLU())
      in_size = hidden_size
    layers.append(nn.Linear(hidden_size, out_size))
    self.layers = nn.ModuleList(layers)

  def forward(self, x):
    for layer in self.layers:
      x = layer(x)
    return x

net = DynamicModel(3, 10, 20, 1)
print(net)
```
这种方式适合层数可变的模型构建。

常用方法
- append(module)：在末尾添加模块
- extend(modules)：批量添加模块
- insert(index, module)：在指定位置插入模块

与 `nn.Sequential` 区别

`ModuleList` 不实现 `forward()`，需手动定义执行顺序，灵活性高。

`Sequential` 内部已定义顺序执行，适合固定结构。

总结 `nn.ModuleList` 是构建 动态网络结构 的利器，尤其适合循环生成层、条件添加层等场景。相比普通 `list`，它能确保参数被追踪并参与优化，是 `PyTorch` 模型开发中非常重要的组件。


## nn.Parameter
它是一个包装器，将普通张量转换为可学习的参数，会自动添加到模块参数列表中。  
函数定义：
``` python
# data：初始值，默认 None
# requires_grad：是否需要计算梯度，默认 True
# 返回值：nn.Parameter 对象
torch.nn.Parameter(data=None, requires_grad=True)
```

例程：
``` python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        # 创建可学习参数
        self.weight = nn.Parameter(torch.randn(10, 5))
        self.bias = nn.Parameter(torch.zeros(5))

    def forward(self, x):
        return x @ self.weight.t() + self.bias

model = MyModule()
print("参数:", list(model.named_parameters()))
print("权重形状:", model.weight.shape)
```


## torch.scatter_add
torch.scatter_add 是 PyTorch 中用于将源张量的值加到指定位置的函数。它将 src 的值按照 index 指定的位置加到 input 中。  
函数定义:
``` python
torch.scatter_add(input, dim, index, src)
```
参数:
- input (Tensor): 输入张量。
- dim (int): 散布的维度。
- index (Tensor): 索引张量，指定要将 src 的值加到 input 的哪个位置。
- src (Tensor): 源张量，要添加的值。  
返回值:
- torch.Tensor: 返回修改后的张量。  

``` python
import torch

# 创建输入张量
input = torch.zeros(3, 5)

# 创建索引和源
index = torch.tensor([[0, 1, 2, 0, 0],
                      [1, 2, 0, 1, 2],
                      [2, 0, 1, 2, 0]])
src = torch.tensor([[1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2],
                    [3, 3, 3, 3, 3]])

# 沿 dim=0 散布并累加
output = torch.scatter_add(input, dim=0, index=index, src=src)

print("输入:")
print(input)
print("n索引:")
print(index)
print("n源:")
print(src)
print("n结果:")
print(output)
```

### 核心函数
`torch.scatter_add`：**按指定维度，根据index索引位置，把src的值累加写入目标张量**，覆盖+累加，不是直接覆盖。

---
### 代码逐点解析
1. 初始化
```python
input = torch.zeros(3, 5)
```
生成**3行5列**全0张量，作为被写入的容器。

2. 关键参数
- `dim=0`：按**行维度**散布（纵向索引）
- `index`：和`src`同形状，**每个值代表要写入的行号**
- `src`：待累加的数据源

3. 运算逻辑（dim=0）
对**每一列、每一行**：
`index[i,j] = k` → 把 `src[i,j]` 加到 `output[k, j]`

---
### 举一列看懂（以第0列举例）
- index第0列：`[0,1,2]`
- src第0列：`[1,2,3]`
  - 行0数据1 → 累加至第0行第0列
  - 行1数据2 → 累加至第1行第0列
  - 行2数据3 → 累加至第2行第0列

再看**有重复索引**的列（比如第4列）：
index第4列：`[0,2,0]`
src第4列：`[1,2,3]`
- 两个索引=0：\(1+3\) 累加进第0行第4列
- 索引=2：2 进第2行第4列

---
### 最终结果规律
- 无重复索引位置：直接等于src对应值
- 同一目标位置被多个index指向：**数值累加**
- 本质：分组求和，index是分组下标，src是待求和数据。


## F.one_hot
F.one_hot 是 PyTorch 中的一个函数，用于将整数类别标签转换为 独热编码（One-Hot Encoding） 格式。  
函数定义:
``` python
torch.nn.functional.one_hot(tensor, num_classes: Optional[int] = None) -> Tensor
```
参数:
- tensor (Tensor): 输入张量，包含类别索引。
- num_classes (int, 可选): 类别总数。如果未指定，将根据输入张量的最大值推断。

返回值:
- torch.Tensor: 独热编码后的张量。


基本用法:
``` python
import torch
import torch.nn.functional as F

# 示例标签（类别索引）
labels = torch.tensor([0, 2, 1])

# 独热编码（自动推断类别数）
one_hot_auto = F.one_hot(labels)
print(one_hot_auto)
# tensor([[1, 0, 0],
#         [0, 0, 1],
#         [0, 1, 0]])

# 指定类别总数（num_classes）
one_hot_fixed = F.one_hot(labels, num_classes=4)
print(one_hot_fixed)
# tensor([[1, 0, 0, 0],
#         [0, 0, 1, 0],
#         [0, 1, 0, 0]])
```


## torch.no_grad 装饰器与用法
在 PyTorch 中，torch.no_grad() 及 @torch.no_grad() 都用于禁用梯度计算，常用于推理（Inference）或模型评估阶段，以节省显存和计算资源。  
核心作用： 在禁用梯度模式下，即使输入张量 requires_grad=True，计算结果也会自动变为 requires_grad=False，从而避免反向传播所需的中间状态存储。  
1. 上下文管理器形式 适合在代码的局部范围内临时关闭梯度计算：
``` python
import torch
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
with torch.no_grad():
   y = x * 2 # 不会记录梯度
print(y.requires_grad) # False
```
这种方式灵活，可在不同代码块中多次启用/关闭梯度计算。

2. 装饰器形式 适合将整个函数标记为无需梯度：
``` python
import torch
@torch.no_grad()
def inference(model, data):
   return model(data) # 函数内所有操作均不计算梯度
# 示例调用
model = torch.nn.Linear(3, 1)
input_data = torch.randn(2, 3)
output = inference(model, input_data)
```
这种方式简洁，适合推理 API 或评估函数。

3. 注意事项  
工厂函数例外：在 torch.no_grad() 中使用 torch.nn.Parameter() 等创建张量时，requires_grad 仍可能为 True。  
线程本地性：该模式只影响当前线程，不会影响其他线程的计算。  
性能收益：禁用梯度可显著减少内存占用，并加快推理速度，尤其在大模型部署时效果明显。

总结：  
with torch.no_grad() → 控制粒度细，可局部关闭梯度计算。  
@torch.no_grad() → 一次性作用于整个函数，适合推理接口。 在推理或验证阶段，合理使用它们可提升性能并降低显存压力。


## repeat_interleave
`repeat_interleave` 是 PyTorch 里常用的张量复制函数，核心作用是：**沿着某个维度，把每个元素重复 N 次再拼接起来**。

- 和 `repeat` 不同：
  - `repeat`：整体复制多遍（块重复）
  - `repeat_interleave`：逐个元素重复（交错重复）

- 常用形式：
  ```python
  x.repeat_interleave(repeats, dim)
  ```
  - `repeats`：每个元素重复几次
  - `dim`：在哪个维度上操作

- 简单例子：
  ```python
  import torch

  x = torch.tensor([1,2,3])
  x.repeat_interleave(2)  # [1,1,2,2,3,3]
  ```

总结：**按元素逐个重复展开，而不是整块复制。**


# 内存连续性问题？