# 彻底重构 `project` 完整操作流程

## 第一步：设置变量（只需改这里）

```bash
PROJECT_PATH="$HOME/project"          # 项目绝对路径
PROJECT_NAME="project"                # 项目名
GITHUB_USER="your_username"           # GitHub 用户名
OLD_TAG="archive/v1-legacy"           # 存档 Tag 名
```

---

## 第二步：Git —— 存档旧代码

```bash
cd $PROJECT_PATH

# 确认当前状态干净
git status

# 给旧代码打存档 Tag（永久保留可查）
git tag $OLD_TAG
git push origin $OLD_TAG

# 验证 Tag 已推送
git ls-remote --tags origin
```

---

## 第三步：Git —— 创建孤儿分支作为新起点

```bash
# 创建无历史的孤儿分支
git checkout --orphan main-v2

# 清空工作区所有文件
git rm -rf .

# 验证工作区已空
ls -la    # 应该只剩 .git 目录
```

---

## 第四步：Claude Code —— 清理旧项目记忆

```bash
# 计算 ~/.claude/projects/ 里对应的 key
# 规则：绝对路径的 / 全部替换为 -，并去掉开头的 -
PROJECT_KEY=$(echo "$PROJECT_PATH" | sed 's|/|-|g' | sed 's|^-||')
echo "项目 key: $PROJECT_KEY"    # 应输出: home-yourname-project

# 先备份
cp -r ~/.claude/projects/$PROJECT_KEY \
      ~/.claude/projects/${PROJECT_KEY}.bak.$(date +%Y%m%d)

# 删除旧项目历史（让 Claude Code 对旧代码"失忆"）
rm -rf ~/.claude/projects/$PROJECT_KEY

# 清理 todos.json 中旧项目的条目（手动检查）
grep -n "$PROJECT_NAME" ~/.claude/todos.json
# 如果有旧条目，编辑删除：
# nano ~/.claude/todos.json
```

---

## 第五步：初始化新项目骨架

```bash
cd $PROJECT_PATH

# 建立基础目录结构（按你的实际技术栈调整）
mkdir -p src docs scripts .github/workflows

# 创建 .gitignore
cat > .gitignore << 'EOF'
node_modules/
dist/
.env
.env.local
*.log
.DS_Store
EOF

# 创建 README
cat > README.md << EOF
# $PROJECT_NAME (V2)

> ⚠️ 本分支为 V2 完全重构版本，与旧版无继承关系。
> 旧代码存档于 Tag: \`$OLD_TAG\`
EOF
```

---

## 第六步：编写 CLAUDE.md（最关键）

```bash
cat > CLAUDE.md << 'EOF'
# CLAUDE.md — project V2

## ⚠️ 重构声明
- 本项目处于 V2 完全重构阶段
- 禁止参考、复用任何 V1 旧代码的设计模式
- 旧代码存档于 Git Tag: archive/v1-legacy，仅供历史查阅

## 技术栈
- （在此填写 V2 的实际技术栈）
- Runtime: 
- 数据库: 
- 框架: 

## 架构约束
- （在此填写新的架构规则）

## 目录结构
src/
  （按实际结构填写）

## 当前优先任务
1. 
2. 
3. 

## 禁止事项
- 禁止复用 V1 的 API 设计
- 禁止复用 V1 的数据库 schema
EOF

echo "✅ CLAUDE.md 已创建，请打开编辑填写实际内容"
```

---

## 第七步：首次提交 & 推送

```bash
cd $PROJECT_PATH

# 按顺序提交
git add .gitignore
git commit -m "chore: init v2 rewrite — add .gitignore"

git add CLAUDE.md
git commit -m "docs: init CLAUDE.md for v2 rewrite"

git add README.md
git commit -m "docs: init README for v2"

# 推送新分支到远端
git push origin main-v2

# 查看提交历史（应该只有3条干净的提交）
git log --oneline
```

---

## 第八步：GitHub 上切换默认分支

```
GitHub 仓库页面 →
  Settings →
    Branches →
      Default branch → 改为 main-v2 → Update

# 然后可选：删除旧的 main 分支
git push origin --delete main

# 本地重命名分支
git branch -m main-v2 main
git push origin main
git push origin --set-upstream origin main
```

---

## 第九步：启动 Claude Code 验证新环境

```bash
cd $PROJECT_PATH

# 启动 Claude Code（会读取新的 CLAUDE.md，没有旧历史）
claude

# 在 Claude Code 里验证它的认知
# 可以问它："请描述一下这个项目当前的技术栈和架构约束"
# 它应该只知道 CLAUDE.md 里写的 V2 内容
```

---

## 完整 Checklist

```
Git
  ✅ 旧代码打 Tag: archive/v1-legacy 并推送
  ✅ 创建 orphan 分支 main-v2
  ✅ 工作区清空
  ✅ GitHub 默认分支已切换
  ✅ 旧 main 分支已删除（可选）

Claude Code
  ✅ ~/.claude/projects/home-yourname-project/ 已备份
  ✅ ~/.claude/projects/home-yourname-project/ 已删除
  ✅ todos.json 旧条目已清理
  ✅ CLAUDE.md 已重写为 V2 内容

新项目
  ✅ 目录结构已建立
  ✅ .gitignore 已配置
  ✅ 首次提交历史干净（3条）
  ✅ Claude Code 启动后认知正确
```

---

**最容易忘的两步**：打完 `archive/v1-legacy` Tag 之后立刻 push，以及 CLAUDE.md 要在 `git rm -rf .` 之后**第一个**重新创建——这是 Claude Code 新记忆的起点。  


## 补充：删除 Tag

``` bash
# 创建标签 v1.0 指向当前提交
git tag v1.0
# 再次创建同名标签会报错
git tag v1.0
# fatal: tag 'v1.0' already exists

# 删除本地旧标签
git tag -d v1.0
# 删除远程旧标签（两种写法，兼容不同版本Git）
git push origin :refs/tags/v1.0
git push --delete origin v1.0
# 在指定提交上创建新标签
git tag v1.0 <commit-hash>
# 推送新标签到远程
git push origin v1.0
```


## 第八步的补充说明

按照第八步的命令顺序，在执行 `git branch -m main-v2 main` **之前**，原有的 `main` 已经被处理掉了：

```
git push origin --delete main   # ← 此时远端 main 已删除
git branch -m main-v2 main      # ← 此时本地 main 已不存在（你在 main-v2 上）
```

所以重命名时**不存在冲突**，具体状态是：

| | 原 `main` 分支 | 新 `main`（原 `main-v2`）|
|---|---|---|
| **本地** | 创建 orphan 分支时就已离开，`git rm -rf .` 后本地的 `main` 实际已被孤立丢弃 | `git branch -m` 后正常存在 |
| **远端** | `git push origin --delete main` 执行后**已删除** | `git push origin main` 后正常存在 |

---

**如果你跳过了 `git push origin --delete main` 这一步**，直接重命名再 push，则会遇到：

```bash
git branch -m main-v2 main
git push origin main
# ❌ 报错：remote 上已存在 main，且两者无共同历史（孤儿分支）
# 需要加 --force 才能覆盖：
git push origin main --force
```

所以流程里**先删远端 main、再重命名、再推送**的顺序是刻意安排的，避免 force push 的风险提示。


## 保留远程旧 `main` 分支的做法

把第八步改成这样：

```bash
# 1. 先在远端把旧 main 备份成一个新分支名
git push origin main:archive/main-v1

# 2. 本地重命名 main-v2 → main
git branch -m main-v2 main

# 3. 强推覆盖远端 main（旧内容已备份，放心 force）
git push origin main --force

# 4. 设置上游追踪
git push origin --set-upstream origin main
```

执行后远端状态：

```
origin/main          ← 新的 V2 孤儿分支（干净）
origin/archive/main-v1  ← 旧 main 完整保留，只读存档
```

---

### `archive/v1-legacy` Tag 完全不受影响

Tag 是**直接指向某个 commit 对象**的，和分支名无关：

```
archive/v1-legacy tag
        │
        ▼
    commit abc123  ←── 这个 commit 对象永远在 Git 对象库里
        │
    （旧 main 的最后一次提交）
```

- 删除或重命名分支**不会删除 commit 对象**
- Tag 只认 commit hash，不认分支名
- 只要不执行 `git push origin --delete archive/v1-legacy`，Tag 就永远在远端

验证一下：

```bash
# 确认 tag 还在远端
git ls-remote --tags origin | grep archive

# 通过 tag 检出旧代码（任何时候都可以）
git checkout archive/v1-legacy
```

---

### 最终远端结构

```
远端 (origin)
├── main                  ← V2 新起点（孤儿分支，无旧历史）
├── archive/main-v1       ← 旧 main 完整分支，可随时 checkout
└── tags/
    └── archive/v1-legacy ← 指向旧 main 最后一个 commit
```

`archive/main-v1` 分支和 `archive/v1-legacy` Tag 双重保险，旧代码任何时候都找得回来。 