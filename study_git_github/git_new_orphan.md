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