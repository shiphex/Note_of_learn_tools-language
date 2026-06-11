# Tag

## 一种常见的`tag`版本规划

**A.B.C**  

- A: 主版本号，大的 `feature` 更新
- B: 次版本号，小的 `feature` 更新
- C: 修订版本号，只修复 `bug` ，无 `feature` 更新

> 例如：发布了 `v2.9` 版本，那么我们可以去下载2.9版本的最新版本，如 `v2.9.3`   

### 当过去的版本号需要修复 `bug` 时，版本号如何规划？
> 比如，当前 `master` 已经指向了更新的 `commit` ，或者已经发布了新的版本如 `v2.11.0` 时，发现 `v2.9.0` 版本存在 `bug` 。  

那么应该修复 `v2.9.0` 版本的 `bug` ，并发布 `v2.9.1` 版本。具体做法：
1. `git log`检查提交信息
2.  `git checkout commitID` `v2.9.0` 版本的 `commitID` ，即切换到 `v2.9.0` 对应的 `commit`
3. 基于 `v2.9.0` 版本创建分支 `git branch v2.9.0-bug-fix` ，并切换到该分支 `git checkout 2.9.0-bug-fix` （可 `git log` 检查当前所处分支）
4. 修复 `bug` ，并提交 `git commit -m "fix bug"`
5. 基于该bug修复版本，发布新的 `commit` 
6. 然后基于这个新的 `commit` ，打上新的 `tag` 发布 `v2.9.1` 版本（通过命令 `git tag v2.9.1` 实现）


**但会存在问题：**  
这样修复的bug，会在 `v2.9.1` 版本中修复，但是 `master`、`v2.11.0` 版本的 `bug` 会继续存在。解决方法：  
- 方法一：切换到 `master` 、`v2.11.0` 版本，然后使用命令 `git merge v2.9.0-bug-fix` 合并 `v2.9.0-bug-fix` 分支到 `master` 、`v2.11.0` 分支。  
- 方法二：`git cherry-pick` 功能
  - 切换到 `master` 、`v2.11.0` 版本，然后使用命令 `git cherry-pick v2.9.0-bug-fix` 合并 `v2.9.0-bug-fix` 分支的 `commit` 到当前分支。  

---  
# Release

1. 后续如果有新的 `bug` ，需要修复，可基于 `2.9.0-bug-fix` 分支，修复 `bug` ，并发布新的 `commit` ，并打上新的 `tag` 发布新的版本。例如：`v2.9.2`、`v2.9.3` 或 `stable/2.9` 或 `release/2.9` 等。  
2. 但会将在 `2.9.0-bug-fix` 分支上新建 `git branch stable/2.9` 或 `release/2.9` ，
3. 并 `git checkout stable/2.9` 或 `release/2.9` 转移到该分支，
4. 再`git branch -D 2.9.0-bug-fix`将 `v2.9.0-bug-fix` 分支删除。  
5. 这样 `stable/2.9` 或 `release/2.9` 将指向2.9版本最新的bug修复版本，这种分支被称之为 **`stable`** 或 **`release` 分支**。




> 待学习：

【这可能是最方便的嵌入式Linux学习开发姿势，基于Git+Release自动化构建嵌入式Linux系统镜像及开发套件的分发系统，满足你不同产品的开发需求！】 https://www.bilibili.com/video/BV1H44y157vm/?share_source=copy_web&vd_source=1e7e09f5b87e218f8cde7fe5df1821c7

