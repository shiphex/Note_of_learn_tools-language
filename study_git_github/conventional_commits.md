# Conventional Commits 约定式提交规范

## git commit 规范式提交模板
提交说明结构：
``` shell
<type>[optional scope]: <description>

[optional body]

[optional footer]
```  

中文版本：
``` shell
<类型>[可选 范围]: <描述>

[可选 正文]

[可选 脚注]
```


## 提交说明的结构化元素解读

### `type` 类型

1. `fix`: 该 `类型` 提交表示在代码库中修复了一个 `bug`。
2. `feat`: 该 `类型` 提交表示在代码库中添加了一个新功能。
3. 其他常见 `类型`：
   - `build`: 用于修改项目构建系统，如：修改依赖库、外部接口、升级 Node\Python 版本等。
   - `chore`: 用于对非业余类型代码进行修改，如：修改构建流程、工具配置等。
   - `ci`: 用于修改次序集成流程，如：修改 GitHub Actions、GitLab CI、Jenkins、Travis 等流水线配置文件、自动化任务、部署脚本等。
   - `docs`: 用于修改文档，如：修改 readme.md、 API 文档、用户手册等。
   - `style`: 用于修改代码样式，如：调整缩进、空行、空格等。
   - `refactor`: 用于重构代码，如：修改代码结构、变量名、函数名等，但不修改其功能逻辑。
   - `perf`: 用于优化代码性能，如：减少运行时间、减少内存占用等。
   - `test`: 用于修改测试用例，如：添加、删除、修改代码的测试用例。

### `BREAKING CHANGE` 和 `!`
在 `脚注` 中包含 `BREAKING CHANGE:` 或 `<类型>(范围)` 后面有一个 `!` 的提交：  
- 表示引入了破坏性 API 变更，破坏性变更可以是任意 `类型` 提交的一部分
- 只要提交里标了破坏性变更，就代表接口不兼容、旧代码可能直接报错，版本必须升 `MAJOR`（大版本号）
- 和版本对应：只要标了，就对应 SemVer 的 MAJOR 主版本升级（比如 1.x.x → 2.0.0）
- 任何类型都能用：`feat`、`fix`、`docs`、`ci`、`refactor` 都可以标破坏性变更
- 目的：明确告诉别人：这次更新不兼容旧版，升级要小心


### 脚注
脚注中除了 `BREAKING CHANGE: <description>` ，其它条目应该采用类似 [git trailer format](https://git-scm.com/docs/git-interpret-trailers) 这样的惯例。


## 示例

1. 只有必要元素的提交说明
``` shell
docs: correct spelling of CHANGELOG
```

2. 包含`范围`的提交说明
``` shell
feat(lang): add polish language
```

3. 包含了 `!` 字符以提醒注意破坏性变更的提交说明
``` shell
feat!: send an email to the customer when a product is shipped
```

4. 包含了`范围`和破坏性变更 `!` 的提交说明
``` shell
feat(api)!: send an email to the customer when a product is shipped
```

5. 包含了`描述`并且`脚注`中有破坏性变更 `BREAKING CHANGE:` 的提交说明
``` shell
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

6. 包含了 `!` 和 `BREAKING CHANGE:` 脚注的提交说明
``` shell
feat!: drop support for Node 6

BREAKING CHANGE: use JavaScript features not available in Node 6.
```

7. 包含多行`正文`和多行`脚注`的提交说明
``` shell
fix: prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z
Refs: #123
```

