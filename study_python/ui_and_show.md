
# 控制终端颜色的 ANSI Escape Code

例如：
``` shell
\033[36m    # 输出青色
```
语法解析：
- `\033` 表示八进制值 033，即 ASCII 控制字符 `ESC`。
- 组合为 `ESC[36m` 表示输出青色。
- `\033[0m` 表示重置颜色，恢复默认颜色。

颜色列表：

| ANSI 代码 | 颜色       |
| ------- | -------- |
| `30`    | 黑色       |
| `31`    | 红色       |
| `32`    | 绿色       |
| `33`    | 黄色       |
| `34`    | 蓝色       |
| `35`    | 洋红       |
| `36`    | 青色（Cyan） |
| `37`    | 白色       |
| `90~97` | 高亮颜色     |
| `0`     | 恢复默认     |


---
# argparse 模块
add_argument() 是 Python 内置模块 argparse 中的核心方法，它的战场不在类继承内部，而在 命令行（Terminal/CMD）。
如果说 kwargs.get() 是在代码内部安全获取参数，那么 add_argument() 就是在程序入口处定义、解析并拦截用户从命令行输入的参数。

## 1. 它解决了什么问题？
当你写了一个 Python 脚本 script.py，你希望用户能在终端通过输入不同的参数来控制运行逻辑，比如：

python script.py --port 8080 --debug

add_argument() 就是用来告诉 Python：“我的脚本接受一个叫 --port 的数字参数和一个叫 --debug 的开关参数”。

## 2. 核心语法与四大常用金刚
通过 parser.add_argument('参数名', ...) 定义参数时，有四个最常用的配置项：
``` python
import argparse
# 1. 创建解析器parser = argparse.ArgumentParser(description="这是一个示例脚本")
# 2. 添加各种类型的参数# ① 位置参数（必填，不用加 --）
parser.add_argument('filename', type=str, help='要处理的文件名')
# ② 可选参数（带默认值）
parser.add_argument('--port', type=int, default=8000, help='服务端口号')
# ③ 布尔开关（无需传值，触发即为 True）
parser.add_argument('--debug', action='store_true', help='是否开启调试模式')
# ④ 限制可选范围
parser.add_argument('--mode', choices=['train', 'eval'], default='train')
# 3. 解析参数args = parser.parse_args()
```

## 3. 三者大串联：从“终端”到“类内部”
在实际的工业级项目（如深度学习训练脚本、Web 服务启动脚本）中，add_argument()、kwargs.get() 和 super().__init__() 经常是三位一体、流水线式配合的。
## 核心流水线：

   1. 终端输入 → 2. add_argument() 抓取并解析 → 3. 转化为字典 → 4. 传入类中，用 kwargs.get() 提取 → 5. 用 super().__init__() 传给父类。

## 完整闭环代码示例：
``` python
import argparse
# ----------------- 阶段一：定义命令行参数 -----------------parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default='Robot')
parser.add_argument('--learning_rate', type=float, default=0.01)
parser.add_argument('--gpu', action='store_true') # 子类专属参数
cmd_args = parser.parse_args()
# 将命令行解析出的命名空间，快速转化为标准的 Python 字典# 此时 args_dict = {'name': 'Robot', 'learning_rate': 0.01, 'gpu': False}args_dict = vars(cmd_args) 

# ----------------- 阶段二：类继承与参数分发 -----------------class BaseModel:
    def __init__(self, name, learning_rate, **kwargs):
        self.name = name
        self.lr = learning_rate
        print(f"[父类] 初始化模型: {self.name}, 学习率: {self.lr}")
class AdvancedModel(BaseModel):
    def __init__(self, **kwargs):
        # 使用 kwargs.get() 安全获取子类关心的参数
        self.use_gpu = kwargs.get('gpu', False)
        print(f"[子类] GPU 状态: {self.use_gpu}")
        
        # 使用 super().__init__ 将其余参数（name, learning_rate）抛给父类
        super().__init__(**kwargs)

# ----------------- 阶段三：运行 -----------------# 直接把命令行得到的字典，通过 ** 解包传进去model = AdvancedModel(**args_dict)
```

## 总结与终极对比
它们三者代表了 Python 传参在不同生命周期的形态：

| 方法 | 发生阶段 | 核心作用 | 找不到参数时怎么办？ |
|---|---|---|---|
| add_argument() | 程序刚启动时 (用户与代码的边界) | 规定脚本在终端接收什么参数，并自动生成 --help 帮助文档。 | 如果是必填项没传，直接在终端报错并提示用法。 |
| kwargs.get() | 代码运行中 (函数/类内部) | 在代码内部安全、容错地从字典中提取某个配置项。 | 返回你指定的 default 默认值，不报错。 |
| super().__init__() | 类初始化时 (父子类之间) | 将子类处理完剩下的参数，当成接力棒向上传递给父类。 | 取决于父类签名，若父类没定义且没写 **kwargs 则会抛出 TypeError。 |



