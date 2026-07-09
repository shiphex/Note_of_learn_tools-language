
## ast 库
`import ast`:
ast 是 Python 内置模块，ast.literal_eval() 用来安全地把字符串还原成 Python 对象。
``` python
import ast

todos_str = '[{"task":"看书"},{"task":"跑步"}]' # 现在 todos 只是字符串，不是列表
todos = ast.literal_eval(todos_str) # 把字符串转换为列表
print(todos)

# 输出：
# [{'task': '看书'}, {'task': '跑步'}]
```


