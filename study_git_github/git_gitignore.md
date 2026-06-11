# 忽略文件 gitignore

## 忽视文件的三种编写方式
1. 文件名匹配 → 所有同名文件都命中
``` shell
.env    # 忽略所有 .env 文件
```
2. 目录匹配 → 所有在该目录下的文件都命中
``` shell
# 忽略所有在该目录下的文件
node_modules/
build/
target/
```
3. 正则表达式匹配 → 符合正则表达式的文件都命中
    - `*` 通配符，匹配任意字符
    ``` shell
    *.log
    temp*
    ```
    - `?` 匹配单个字符
    ``` shell
    file?.txt
    ```
    - `**` 匹配任意层级目录
    ``` shell
    **/node_modules/
    ```

---

## 若文件已经被追踪如何处理
1. 先将需要移除的文件添加到 `.gitignore` 中
2. 执行 `git rm --cached <file>` 命令，将文件从 git 中移除，让 git 不再 stage 该文件
3. 提交一次 `git commit -m 'remove(.git): stop tracking xxx'`  
**注意：**如果仓库已经被推送到远程，这种操作不能改变文件内容已经泄露的事实