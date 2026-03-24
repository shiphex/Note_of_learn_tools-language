# venv是什么
虚拟环境，用于管理不同项目所需要的不同依赖

# 基础操作
``` shell
uv venv                     # 创建环境
uv venv my-env -p 3.11      # 指定环境名字和python版本
uv venv -p python@3.11      # 使用 python3.11 创建 .venv
source .venv/bin/activate   # 激活环境 (此步仍然需要)
uv init                     # 初始化uv项目
uv pip install              # 装包
uv add                      # 为项目加包
uv sync # 如果有拉取一个uv的项目，直接sync即可配置好环境
uv pip freeze > requirements.txt # 生成一个包含所有已安装包及其精确版本的列表，格式与 pip freeze 的输出相同，常用于生成 requirements.txt 文件
```

# 初始化流程
+ 创建虚拟环境：打开项目路径，终端输入
  ``` shell
  $ python3 -m venv .[venv_project_name]
  ```
+ 激活环境
  ``` shell
  $ .[venv_project_name]\Scripts\activate
  ```

+ 添加安装依赖
  打开`pyproject.toml`,将  
  ``` python
  dependencies = []
  ```
  中添加  
  ``` python
  dependencies = [
    "numpy>=2.3.4",             # 添加项目所需依赖
    "pandas>=2.3.3",            
    "torch>=2.9.0",             
    "transformers>=4.57.1",     
    ]
  ```
  终端输入  
  ``` shell
  $ uv sync     # 安装依赖，配置虚拟环境
  ```