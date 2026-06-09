# Pull Request
## 编写Pull Request标题和文本

## github合并Pull Request的操作
1. 点击上方托盘中的 `Pull Request` 选项卡进入 `Pull Request` 页面
2. 点击 `New pull Request` 按钮创建新的 `Pull Request`
   - 若仓库是fork别人的，需要将 `base repository` 选择为自己的仓库或者目标仓库
3. 选中 `base` 为 `main`、`master` 主分支(或者合并至的目标分支)；选中 `compare` 分支为 `feature` 分支(或者合并的分支、旁路分支)
   - 即：将 `compare` 分支的代码导入到 `base` 分支
4. 点击 `Create pull request` 按钮创建合并需求
5. 填写 `Add a title` 和 `Add a description` 字段(**重点，让人能够具体做了什么，决定code review、项目品质的重要环节**)
   - 可在 `Add a description` 中添加图片；可点击 `Review` 按钮查看 `description` 显示效果。
6. 点击 `Create pull request` 按钮完成建立
7. 若确认合并，点击 `Merge pull request` 按钮合并，最后点击 `Confirm merge` 验证
8. 回到 `Code` 选项卡，确认合并成功

## Pull Request时对冲突的处理
1. 在击 `Merge pull request` 按钮时无法合并，则是两个分支的代码出现冲突导致的
2. 点击 `Resolve conflicts` 按钮可以跳转看到冲突的代码段(不建议在网页上合并冲突)
3. 回到IDE工具中，合并冲突
4. **在IDE工具切换到 `compare` 分支或者 `feature` 分支**
5. 终端输入 `git fetch origin` 拉取远端最新代码
6. 执行 `git merge origin/main`、`git merge origin/master` 或 `base` 分支等，同步远端最新代码  
   （或 `git rebase origin/main`、`git rebase main`，如果有冲突，解决冲突后`git rebase --continue`，再快速合并到主分支：`git checkout main` -> `git merge feature`，最后推送到远程仓库：`git push origin main`）

 **对冲突进行合并**
1. 点击 `Merge pull request` 按钮合并，最后点击 `Confirm merge` 验证
2.  `git checkout main`、`git pull origin main`、`git merge feature/name` 合并 `feature` 分支到 `main` 分支
3.  合并完所有分支、所有冲突后，主分支执行 `git pull` 拉取全部更新
4.  执行、测试合并后的代码，确保没有问题