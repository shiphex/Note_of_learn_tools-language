## 使用 uv 初始化 Python 项目完整流程

### 1. 初始化项目

```bash
# 新建项目目录并初始化
uv init project
cd project

# 或在已有目录中初始化
cd project
uv init
```

### 2. 创建虚拟环境

```bash
# 使用默认名称 .venv（推荐）
uv venv

# 或指定自定义名称
uv venv myenv
```

### 3. 激活虚拟环境

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows (CMD)**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

激活后命令行前缀会显示 `(.venv)`。

### 4. 安装依赖

```bash
uv add requests          # 添加运行时依赖
uv add pytest --dev      # 添加开发依赖
uv sync                  # 安装所有依赖
```

### 5. 运行项目

```bash
uv run main.py
```

### 6. 退出虚拟环境

```bash
deactivate
```

---

> **提示**：日常开发中可以跳过手动激活，直接用 `uv run` 执行脚本，uv 会自动使用项目虚拟环境。