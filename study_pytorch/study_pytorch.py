import torch
import torch.version
print(torch.__version__)
print(torch.version.cuda)  #输出CUDA版本
print(torch.cuda.is_available())  #输出为True，则安装无误

