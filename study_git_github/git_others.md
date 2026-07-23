# 其他git操作

包括 `amend` 、 `stash` 、 `detached` 、 `revert` 、 `reset`

---

## `amend`
即 `git commit --amend`：修改上一个提交的消息，覆盖上次提交（包括commit message），这样做可避免零碎小问题导致提交历史的信息噪音过大    
何时使用：
- 上一次提交中有一些小的代码错误需要修改（如readme中拼写错误、语法错误等）
- 上一次提交的commit message不够清晰，需要修改

### VScode图形化界面中的操作方法
1. 修改完小错误后，点击**源代码管理**的 `Commit`按钮边上下拉列表，再点击 `Commit (Amend)` 
2. 在跳出的弹窗中，修改commit message，完成后点击**界面右下角** `Commit`

---

## `stash`
- 问题：  
在某工作目录中做了一些修改，但尚未 `commit` 提交，但此时需要切换到其他分支进行开发工作。  
此时若不 `commit` 提交当前工作目录，直接切换分支，会导致当前工作目录的修改丢失丢失。  

### VScode图形化界面中的操作方法
1. 点击图形化界面**源代码管理**的 `CHANGES`/`更改`栏最右侧有三个点 `⋯` ，找到`Stash`/`储存` 选项栏
2. 点击选项栏弹出选择中的 `Stash`/`储存`
   - `Stash (inclaude Untracked)`/`储存（包含未跟踪文件）` 会将没有被跟踪的文件也储存起来
   - `Stash Staged`/`储存已暂存文件` 只有被 `staged` 的文件才会储存起来
3. 在跳出来的窗口中输入`stash message`，完成后回车
4. `Git Graph` 中可以看到 `stash` 操作
5. 在处理完另一个分支后，回到 `stash` 所在分支，再在 `Git Graph` 中右击 `stash` ，点击 `Pop Stash…` 恢复储存的修改  
   - 或者：在`CHANGES`/`更改`栏最右侧有三个点 `⋯` ，找到`Stash`/`储存` 选项栏，点击 `Pop Latest Stash` 恢复储存的修改
  
### 命令行操作方法
- 保存当前修改
  - `git stash`：保存工作区和暂存区的所有修改。
  - `git stash push -m "add notes"`：保存时添加备注说明，方便识别。
- 查看与管理列表
  - `git stash list`：查看所有保存的 `stash` 记录列表。
  - `git stash show`：查看最近一次 `stash` 的修改详情。
- 恢复修改
  - `git stash pop`：恢复最近一次保存的修改，并从记录列表中删除它。
  - `git stash apply`：恢复修改，但不从记录列表中删除它。
- 删除记录
  - `git stash drop stash@{n}`：删除指定的某条 `stash` 记录。
  - `git stash clear`：清空所有保存的 `stash` 记录。

---

## `detached`
切换到无分支指向的 `commit`，称为 `detached head`，创建分支后继续开发。  
用于从某一个没有分支指向的 `commit` 开始进行开发，不改变已有的分支。 
**注意：**实施时需要在这个 `commit` 上创建一个新的分支，用于后续的开发工作，若直接开发并提交，此提交无效且不会被记录。（切换分支后，此提交会被删除）   

### VScode图形化界面中的操作方法
1. 在 `Git Graph` 中右击 `stash` ，点击 `Create Branch…` 创建一个新的分支
   - 或者：点击图形化界面**源代码管理**的 `CHANGES`/`更改`栏最右侧有三个点 `⋯` ，找到`Create Branch`/`创建分支` 选项栏
2. 在弹出来的窗口中输入分支名称，完成后回车
3. `Git Graph` 中可以看到 `detached head` 操作
4. 切换到新创建的分支，继续开发

---

## `revert`
即 `git revert`：撤销上一个 `commit` 提交，将上一个提交的修改撤销，重新应用到当前工作目录中。  
**注意：**不会删除上一个提交，只是将上一个提交的修改撤销，重新应用到当前工作目录中。  
``` bash
git revert HEAD
```

若需要撤销两个提交，例如撤销上一个提交和上上一个提交，上一个提交的hash值为 `c2e2`，上上一个提交的hash值为 `70a0`，可使用 `git revert 70a0`(`git revert HEAD~1`) 等命令，撤销两步。  

**注意：**若提交已经 `push` 到远程仓库的公有分支，不能使用 `reset` 操作，否则会导致远程仓库的提交历史被修改，只能使用 `revert` 操作。  
对于私有分支：`git revert HEAD~1` ，然后 `git reset -f` （分支少了 `commit` 的内容，必须强制推送）

---

## `reset`
直接**删除**上一次 `commit` 提交，将上一次提交的修改从当前工作目录中移除。  

### VScode图形化界面中的操作方法
1. 点击图形化界面**源代码管理**的 `CHANGES`/`更改`栏最右侧有三个点 `⋯` ，找到 `Commit`/`提交` 选项栏
2. 点击选项栏弹出选择中的 `Undo Last Commit`/`撤销上次提交`
``` bash
# 撤销上次提交
# `~1`表示从HEAD上一个提交开始撤销，`~2`表示从上上一个提交开始撤销，以此类推
git reset --soft HEAD~1   # 把更改退回staged（Undo Last Commit）
git reset --mixed HEAD~1  # 把更改退回modified（并且changes没有被staged）
git reset --hard HEAD~1   # 把更改彻底删除
```

---

## 更改分支名
### 命令行
1. 先切换到要更改分支名的分支 `git checkout 分支名`
2. 执行 `git branch -m 新分支名` 即可更改分支名

### VScode图形化界面
1. 点击图形化界面**源代码管理**的 `CHANGES`/`更改`栏最右侧有三个点 `⋯` ，找到`Branch`/`分支` 选项栏
2. 点击选项栏弹出选择中的 `Rename Branch…`/`重命名分支`
3. 在弹出来的窗口中输入新分支名，完成后回车