# <center>Study how to use Git & Github</center>
# github社区
+ `awesome` + 关键词：社区精选优质资源（Explore下的Topics中有AwesomeLists）
+ `stars:`筛选收藏数

HelloGithub：优质资源周期汇总

# 使用git管理仓库
## 初次运行 Git 前的配置
1. 查看版本号`git --version`  

2. 设置昵称  
`git config --global user.name "xxxxx"`（全局）  
`git config user.name "xxxxx"`（某仓库下）
   +  `config`: 配置
   + `--global`: 全局
   + `user`: 用户
   + `name`: 昵称

3. 设置邮箱  
`git config --global user.email "xxxxx"`（全局）  
`git config user.email "xxxxx"`（某仓库下）
   + `email`: 邮箱

4. 查看昵称和邮箱设置
   + 全局：
     +  `git config --global user.name`
     +  `git config --global user.email`
   + 某仓库下:  
     +  `git config user.name`
     +  `git config user.email` 

5. 检查配置信息  
`git config --list`  
输入 ``git config <key>``： 来检查 Git 的某一项配置  


> note:
> `name`和`email`自行设置，无需与Github中一致，Git和GitHub是两个不同的实体，因此它们之间的用户名并不需要强制相同。只要你在提交代码时使用了**正确的GitHub账户**，你的贡献信息就会被正确地显示在GitHub上。  

## 基础操作
### 获取git仓库
+ 本地项目自建仓库：  
   1. 打开项目目录
   2. 初始化仓库`git init`  
   

+ 从服务器clone一个git仓库：  
   `git clone <url>`    
   `git clone <url> <mylibname>`(并自定义本地仓库)
   

### 跟踪管理仓库代码
  1. 指定所需的文件来进行追踪(暂时保存)` git add <file>`(添加全部文件` git add .`)
  2. 提交变更(固定成一个版本)`git commit`进入vim书写变更解释(直接书写变更解释`git commit -m 'xxxx'`、`git commit -m "xxxx"`)
  3. 查看日志`git log`

### 分支重命名
`git branch -m <new name of branch>`


### 回退到某个版本
回退到某个版本，同时删除这个版本之后的所有版本  
`git reset --hard <commit id>`(硬重置：`hard`，？`soft`，？`mixed`)


### 分支
+ 在`git commit`后使用`git branch <name of branch>`创建分支
+ `git branch -a`查看全部分支
+ `git checkout <name of branch>`切换分支
+ `git merge <name of branch>`合并分支并重新指向
+ 保存文件后，使用 `git add` 命令将文件标记为已解决冲突的状态
+ 完成合并后，继续进行其他合并操作`git merge --continue`
+ 完成所有合并操作后，提交合并结果`git commit -m "解决了文件 file 的合并冲突"`
+ 确认合并`git status`

# github远程仓库
## 创建新的远程仓库
1. 新建仓库`new repository`
2. 选择归属并给仓库命名
3. 选择公开或私有仓库
4. 创建仓库`creat repository`
5. 重命名主分支为main`git branch -M main`
6. 添加远程仓库地址连接`git remote add origin <url of repository>`
7. 推送上传到远程仓库`git push -u origin main`(第一次推送时加 `-u`，建立本地分支与远程分支的跟踪关系，之后可以简化成 `git push`或`git pull`。)
8. 输入用户名和密码（github邮箱、密码）
9. 刷新远程仓库网页检测是否上传成功
10. 若远程仓库合并了其他人的分支更新了导致版本不一致，则需要更新本地版本`git fetch origin`，再`git merge origin/main`把远程仓库的代码合并到本地分支中

## 远程仓库的管理
### 将远程仓库克隆到本地
+ `git clone <url of remote repository> .`得到基于自己原远程仓库的链接
+ `git remote -v`可验证链接
+ `git remote add upstream <url of remote repository>`添加上游代码库
+ `git remote -v`可验证链接
+ 若想给别人代码库加功能，可先创建一个分支`git checkout -b <name of your branch>`(`-b` 是 `branch` 的缩写，创建一个新的分支并立即切换到该分支。)
+ 修改更新工程代码，再` git add <file>`、`git commit -m 'xxxx'`、`git push`(`git push -u origin main`)
+ 可在远程仓库中看到除原有分支外，还有**新**`push`的分支
+ 若远程仓库更新了`commit`导致版本不一致，则需要更新本地版本`git fetch upstream`，再`git merge upstream/main`把远程仓库的代码合并到本地分支中，最后`git push`尽快提交新pr


### 远程仓库中管理不同分支
+ 到新(或想要的主要)分支，点击`Pull requests`进入，点击`New pull request`新建pr
+ 选定好`base`分支及`compare`分支
+ 若出现`Able to merge.`，则表示无问题可以合并
+ 点击`Create pull request`后填写pr信息，再次点击`Create pull request`即提交成功
+ 显示`No conflicts with base branch`表示分支合并成功

### 分支保护
+ **强制签出（Require pull request reviews before merging）**： 分支保护可以要求在合并更改到主分支之前，至少需要一个审阅者审核并批准相关的 Pull Request。这可以确保代码在合并之前经过审查。  

+ **必须通过 CI/CD（Require status checks to pass before merging）**： 您可以配置分支保护，要求 CI/CD 流程必须成功才能合并代码。这可以确保代码通过自动化测试和构建程。    

+ **分支保护规则（Require branches to be up to date before merging）**： 分支保护还可以要求主分支必须是最新的，以确保合并的更改不会与过时的代码冲突。  

+ **封锁分支（Include administrators）**： 分支保护还可以包括仓库管理员，以确保即使是仓库管理员也需要按照规则提交更改，以确保一致性和质量。  






















# git commit风格规范？
https://www.conventionalcommits.org/zh-hans/v1.0.0/
