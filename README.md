# Modules By ATN
## 导入说明
将`ATNModules`目录放入项目中，用`from ATNModules import *`引入所有模块或根据需求引入
## 模块目录
- `TerminalRenderer` 控制台渲染器
- `LogWrapper` 日志包装器
## 方法手册
### `TerminalRenderer`
- `void change_title(str: title)`

修改控制台窗口的标题
`title` -> 标题文本
- `void place(str: string, [int, int]: pos, string: fore_color='default', string: back_color='default')`
