# <center>学习pytorch<center>

## pytorch深度学习模型建立的范式
+ 准备数据
+ 定义模型
+ 训练模型
+ 评估模型
+ 做出预测

## 安装验证torch
+ 下载
    ``` shell
    $ pip install torch
    ```
+ 验证是否安装成功
    ``` python
    import torch
    import torch.version
    print(torch.__version__)
    print(torch.version.cuda)  #输出CUDA版本
    print(torch.cuda.is_available())  #输出为True，则安装无误
    ```

## 准备数据
+ 数据下载
+ 数据格式化
+ 数据集划分

