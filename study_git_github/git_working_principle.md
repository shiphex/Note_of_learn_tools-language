
# 1. Git 工作原理

## 1.1 git 工作对象的引用关系
git 的三个对象的引用关系：
``` shell
commit -> tree -> blob -> object
```

1. commit 对象：记录了文件的变更历史，包括文件的变更内容、变更时间、变更人等。
2. tree 对象：记录了文件的目录结构，包括文件的路径、文件的类型等。
3. blob 对象：记录了文件的内容，包括文件的二进制数据等。

使用命令 `git cat-file -p 哈希值` 来查看 `commit` 对象的内容。例如：
``` shell
$ git cat-file -p ec83597
tree 1a004a28c3367c3b9f1fa825c2f2a0abe091fffe
parent 4a6072483e4c4bbe46d84be3a9125d131e6704a3
author Zhou Hao <zhmsolone@outlook.com> 1784171218 +0800
committer Zhou Hao <zhmsolone@outlook.com> 1784171218 +0800

feat: 添加模块和包的导入原理文档，包含示例和详细说明
```
- 可以看到指向的 `tree` 对象的哈希值。
- `parent` 字段指向上一个 `commit` 对象的哈希值(从哪个 commit 衍生而来)。

继续查看 `tree` 对象的内容。
``` shell
$ git cat-file -p 1a004a
040000 tree e962f44cdb64dcc1459d1f3cd8cdd48a4a065c74    .obsidian
040000 tree d1e9120574438513b8629b4680c230c8ef63a41a    .vscode
040000 tree 8e416bf22bbb146088406c7f858c6d94a132bb33    study_git_github
040000 tree 0335b6ad2d8d00c6943046d8424e98d959f5fe9e    study_python
040000 tree 6b9afa01320eec6c97651a8b74e0803a25747418    study_pytorch
040000 tree e12648d397dcee5fdfad276cf4cb1f80e0ae7ab1    study_tools
040000 tree 143c93692aa4c73637b5c54f8c5f2ce47f6a8542    study_venv
```
以上依然是 `tree` 对象的内容。
继续查看 `tree` 对象的内容。
``` shell
$ git cat-file -p 0335b6ad
100644 blob 1847a62123b8b292f2b948bad1b8c99479c00504    basic_program.md
100644 blob 862fa02a95d277d3650ee9b0d6c4e922f05d9a44    basic_program.py
100644 blob e0f5087d1c92d5229b9e28af365760f89efb7f08    built-in-functions.md
100644 blob d93f3f1cc4113e63e98f6bf9213a9df3d8ebfc44    file_operate.md
100644 blob 9b213acb309ecdaa492f4a9fddae1bb82c6e01b5    init.md
040000 tree 1903eac1d5c9838808d5bda3ac3dcca9d4005d34    init_code
100644 blob 47857f915228a3e43c1995d0176d04f718201f5d    python_libraries.md
100644 blob 079827bef3a7ecec141832dd51fffb0e46a29684    ui_and_show.md
```
这里可以看到有 `tree` 对象和 `blob` 对象。

继续查看 `blob` 对象的内容。
``` shell
$ git cat-file -p 1847a62
# <center>python语法学习笔记</center>
# 基础语法

## 注释
+ 单行注释，使用`#`
+ 多行注释，使用`'''`、`"""`
``` python
# 注释使用“# ”

…………………………
```
可以发现 `blob` 对象的内容是一个文件，且该文件是一个完整的文件，而不是只有此次修改的内容。


## 1.2 对新旧文件的引用
- 当文件修改后，`tree` 对象会指向新的 `blob` 对象（`commit -> tree -> 新blob`）。
- 当文件未修改时，`tree` 对象会指向旧的 `blob` 对象（`commit -> tree -> 旧blob`）。


## 1.3 如何彻底从 git 中删除文件
通过删除文件再 git commit 的方式，只能在工作区删除文件，而不会在 git 中删除文件。  

要想真正删除文件，需要：
``` python
git reset XXXX      # 让 blob 对象成为没有被引用的悬空对象
git gc --prune=now  # 清理悬空对象的垃圾
```


## 1.3 关于 branch
branch 不是一个对象，只是一个指针，指向某个 commit 对象。跳转到一个 branch，就是将指针指向该 branch 对象的 commit 对象。