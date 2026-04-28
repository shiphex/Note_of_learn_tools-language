# 使用 pathlib 模块（现代化推荐）
自 Python 3.4 起引入，pathlib 提供了一种面向对象的操作方式，代码更加简洁易读。
``` python
from pathlib import Path

# 1. 定义路径对象
path = Path("my_new_folder/test.txt")

# 2. 创建父级文件夹 (parents=True 自动创建缺失的父目录)
path.parent.mkdir(parents=True, exist_ok=True)

# 3. 创建文件并写入
path.write_text("Hello Python!", encoding="utf-8")

print(f"文件已创建在: {path.absolute()}")
```

创建目录：
- os.mkdir(): 只能创建单层目录，父目录不存在会报错。
- os.makedirs(): 可创建多层嵌套目录（如 a/b/c）。  

创建文件：
- open(path, "w"): 如果文件不存在则新建，如果存在则会覆盖原内容。
- open(path, "a"): 如果文件不存在则新建，如果存在则在末尾追加内容。  

