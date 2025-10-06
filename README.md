# 导入说明
将`ATNModules`目录放入项目中，用`from ATNModules import *`引入所有模块或根据需求引入
# 模块目录
- `TerminalRenderer` 控制台渲染器
- `LogWrapper` 日志包装器
# 方法手册
## `TerminalRenderer`
### place 字体颜色与样式对照表
- fore_color : {'sys_default' : 系统默认, 'blue' : 蓝色, 'red' : 红色, 'yellow' : 黄色, 'green' : 绿色, 'cyan' : 青色, 'magenta' : 洋红色, 'black' : 黑色, 'white' : 白色}
- back_color : {'sys_default' : 系统默认, 'blue' : 蓝色, 'red' : 红色, 'yellow' : 黄色, 'green' : 绿色, 'cyan' : 青色, 'magenta' : 洋红色, 'black' : 黑色, 'white' : 白色}
- style : {'default' : 默认, 'highlight' : 加粗, 'underline' : 下划线, 'flick' : 闪烁, 'reverse' : 反色, 'non-visible' : 隐藏}
注意：`styles`在不同的渲染策略中不保证按照期望生效，例如`flick`在高速渲染时会在每一帧重置而失效。不同终端也会影响效果。
### `void change_title(str: title)`
修改控制台窗口的标题
- `title` -> 标题文本
### `void place(str: string, (int, int): pos, str: fore_color='default', str: back_color='default', str: style='default')`
在指定坐标放置文本
- `string` -> 文本内容
- `pos` -> 文本起始的坐标
- `fore_color` -> 前景色。若为 'default' 则使用 render 传入的默认配色
- `back_color` -> 背景色。若为 'default' 则使用 render 传入的默认配色
- `style` -> 样式
### `void render((str, str): origin_colors=('sys_default', 'sys_default'), bool: clear_window=True)`
渲染已放置的文本
- `origin_colors` -> 字符的默认前景色与背景色。默认为系统的默认配色。
- `clear_window` -> 在渲染之后是否清除所有已放置的文本
### `str getch()`
在不阻断程序的情况下获取键盘输入

示例程序结构：
```
while 1:
    TerminalRenderer.place('...') # 放置字符
    TerminalRenderer.render() # 渲染字符
    keyboard_input = getch() # 获取键盘输入
    time.sleep(1 / 60) # 控制帧率
```
返回按键对应的字节串
## `LogWrapper`
### `void logwrap(bool pause=True)`
将主函数包装日志保存功能并立刻执行
- `pause` -> 选择是否在输出日志后使用`input()`方法暂停程序

示例程序结构：
```
@LogWrapper.logwrap()
def main(): # main 函数会立刻执行，并在出错时保存日志在 log 目录下
    ...
```
