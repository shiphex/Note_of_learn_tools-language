# github action

## git flow 工作流(分支管理)
1. `main` 分支：主分支，存放正式发布的代码
2. `develop` 分支：开发分支，存放开发版本的代码(开发时最少要有一个develop分支，而不是把未经验证的新功能直接发布到main分支上)
3. `feature` 分支：功能分支，存放新功能的代码
4. `release` 分支：发布分支，存放发布版本的代码
5. `hotfix` 分支：热修复分支，存放紧急修复的代码

## github action流程
1. **撰写测试案例**
2. 将测试案例提交到远程仓库的`develop`分支
3. 打开远程仓库的`develop`分支页面，点击上方托盘中的 `Actions` 选项卡
4. 找到对应的`workflow`，点击进入
5. 参看`测试执行结果`(绿色√表示通过，红色×表示失败)
6. 点击`测试执行结果`，查看测试执行详情
7. 回到对应的`workflow`页面，在`artifact`选项卡中，可下载测试执行详情
8. 下载的测试执行详情`压缩包`文件，包含测试执行的详细信息，如测试用例、测试结果、测试时间等
9. 可通过`压缩包`中`index.html`看到测试覆盖率报告
10. 可根据测试情境，补充测试用例，提高测试覆盖率(没有必要追求100%，但要保证重要的逻辑、功能得到测试)

## rules(通过`测试`的分支才能合并到主分支)
1. 打开远程仓库的`main`分支页面
2. 点击上方托盘中的 `settings` 选项卡
3. 在左侧菜单栏中，点击 `Rules` 选项卡，点击其中的`Rulesets`选项
4. 点击`New ruleset`选项卡，选择`New branch ruleset`
5. `Ruleset Name`选项框输入名称，如`Protect main branch`(表示保护main分支的测试rules)
6. `Enforcement status`选项卡切换成`Active`(**只有这样这条规则才会生效**)
7. 向下滑动，找到`Target branches`栏目，`Add target`选项卡选择`Include default branch`，该默认分支为`main`分支
8. 向下滑动，勾选`Require a pull request before merging`，表示要`PR`才能合并分支，不能直接push
9. 向下滑动，勾选`Require status checks to pass`并，
10. 然后选拓展出来的`Require branches to be up to date before merging`，表示只有测试通过后才能进行合并
11. 点击`Add checks`选项卡，检索`test`，勾选通过`github action`设计出来的`test`
12. 最后点击`Create`完成`Rules`的创建
13. 通过两步验证完成`Rules`的生效   
> **注意：**rules在私人仓库中无法生效，要不然公开，要不然移动到团队账号下  

## 当推送的分支没有通过测试时
1. 点击上方托盘中的 `Actions` 选项卡
2. 找到对应的`workflow`(可直接查看测试结果，绿色√表示通过，红色×表示失败)，点击进入
3. 参看`测试执行结果`(绿色√表示通过，红色×表示失败)
4. 切换到上方托盘中的 `Pull requests` 选项卡
5. 点击`New pull request`按钮，创建新的`Pull Request`
6. `compare` 选择测试失败的分支，`base` 选择`main`分支
7. 点击 `Create pull request` 按钮创建合并需求
8. 编写`Pull Request`的标题 `title` 和文本`description`，点击 `Create pull request` 按钮完成建立
9. 若**推送的分支没有通过测试**，会出现 `All checks have failed`，此时无法点击 `Merge pull request` 按钮

## 当推送的分支通过测试时
1. 点击上方托盘中的 `Pull requests` 选项卡
2. 在测试时出现 `Some checks haven't completed yet`，若测试通过将显示 `All checks have passed`，未通过将显示 `Some checks have failed`
3. 通过测试后，点击 `Merge pull request` 按钮合并，点击 `Confirm merge` 确认合并
4. 回到 `Code` 选项卡，可确认合并成功


> Test-Driven Development(测试驱动开发)