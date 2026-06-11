# `Creating Releases` 创建发布包

发布包是让用户接触项目不错的方式： 

1. 页面顶端，点击你的用户名
2. 在你的 `profile` 页面，点击 `Repositories` 窗口，接着点击你的库的名称
3. 顶端，点击 `releases`
4. 点击 `Draft a new release`
5. 输入发布包的版本号。版本号基于 `Git` 标签,我们建议标签命名，符合语义版本。
6. 选择一个分支来包含你想发布的项目。通常，你会想发布在你的主分支，除非你发布测试软件。
7. 在你的发布包中输入标题和描述
8. 如果发布中包含二进制文件，托文件进二进制框中
9. 如果，发布包不稳定，选择 `This is a pre-release` 来提醒用户这个是不能用于生产环境的
10. 如果准备好了发布了，点击 `Publish release`。另外 点击 `Save draft` 用于保存在草稿箱中。只有你和你的合作者可以看到到草稿箱。

## `Automatically creating releases` 自动创建发布

自动创建发布（支持命令行或者脚本），详见 `Releases API documentation`.

## `Further reading` 扩展阅读

链接到发布包
参考：[Creating Releases](https://help.github.com/articles/creating-releases/)
