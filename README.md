一个简易的控制台界面渲染库。
提供字符定位打印、颜色渲染、键盘输入等功能，便于在控制台制作小型游戏和交互程序。

⚠️ 注意：Thu Terminal Engine 适合低速渲染和文字交互，不适合实时高帧率渲染。

--------------------------------
对外主要方法
--------------------------------

1. change_title(title: str) -> None
   修改控制台窗口标题。

2. get_terminal_size() -> (int, int)
   获取控制台大小（列数, 行数）。

3. getch(sleep=0.02) -> Optional[bytes]
   非阻塞读取键盘输入。
   - 返回 None 表示没有输入。
   - 常见方向键：↑ b'H'，↓ b'P'，← b'K'，→ b'M'。

4. print_in_pos(string: str, x: int, y: int, fore_color='default', back_color='default') -> None
   在指定坐标写入字符串（写入缓冲区，需调用 update() 才能显示）。

5. update(origin_colors=['white','black'], clear_window=True) -> None
   刷新屏幕，把缓冲区内容渲染到控制台。
   - origin_colors 指定默认前景/背景色。
   - clear_window=True 表示刷新后自动清空缓冲区。
