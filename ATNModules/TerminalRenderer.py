"""
TerminalRenderer\n
控制台渲染器\n
便于用控制台设计图形和键盘操作程序，以增强程序的可读性
与其他控制台程序一样，TerminalRenderer不适合实时高速渲染\n
By ATN\n
函数列表：\n
change_title\n
print_in_pos\n
update\n
"""

import os, msvcrt, time

string_list = []
fore_colors = {'default' : '0', 'blue' : '34', 'red' : '31', 'yellow' : '33', 'green' : '32', 'cyan' : '36', 'magenta' : '35', 'black' : '30', 'white' : '37'}
back_colors = {'default' : '0', 'blue' : '44', 'red' : '41', 'yellow' : '43', 'green' : '42', 'cyan' : '46', 'magenta' : '45', 'black' : '40', 'white' : '47'}
styles = {'default' : '0', 'highlight' : '1', 'non-highlight' : '22', 'underline' : '4', 'non-underline' : '24', 'flick' : '5', 'non-flick' : '25', 'reverse' : '7', 'non-reverse' : '27', 'non-visible' : '8', 'visible' : '28'}

def _decorate_string(string, fore_color='default', back_color='default'):
    """对字符进行彩色修饰。在使用前景色时，背景色必须设定。\n
    string ->str 要修饰的字符。\n
    fore_color='default' ->str 前景色。\n
    back_color='default' ->str 背景色。\n
    return str 修饰后的字符"""
    display_style = '\033[0;'
    if fore_color != '':
        display_style += fore_colors[fore_color]
    display_style += ';'
    if back_color != '':
        display_style += back_colors[back_color]
    string = display_style + 'm' + string + '\033[0m'
    return string

def _len_in_size(string):
    """以字符串所占的位置为标准计算长度。\n
    string ->str 要判断的字符串。\n
    return int 长度。"""
    length = 0
    for a in string:
        if len(a.encode()) == 1:
            length += 1
        elif len(a.encode()) > 1:
            length += 2
    return length

def change_title(title):
    """更改标题。\n
    title ->str 标题。"""
    os.system('title ' + title)

def _get_terminal_size():
    """获取控制台行数和列数。\n
    return int 列数, int 行数"""
    terminal_size = os.get_terminal_size()
    return terminal_size.columns, terminal_size.lines

def getch(sleep=0.02):
    """在不中断的情况下获取键盘输入。\n
    sleep=0.02 ->int 每一次获取间隔的时间。单位秒。\n
    return b'字符'"""
    get = None
    if msvcrt.kbhit(): #如果键盘有输入
        get = msvcrt.getch() #读取键盘输入
    time.sleep(sleep)
    return get

def print_in_pos(string, x, y, fore_color='default', back_color='default'):
    """在指定位置渲染字符。\n
    string ->str 字符。\n
    x ->int x坐标。\n
    y ->int y坐标。\n
    fore_color='default' ->str 前景色。\n
    back_color='default' ->str 背景色。"""
    now_x, now_y = x, y
    a = -1
    add = ''
    while a < len(string) - 1:
        a += 1
        add = string[a]
        string_list.append([add, now_x, now_y, fore_color, back_color])
        now_x += _len_in_size(add)
        add = ''
    if add != '':
        string_list.append([add, now_x, now_y, fore_color, back_color])

def update(origin_colors=['white', 'black'], clear_window=True):
    """刷新界面。\n
    origin_colors=['white', 'black'] ->list
    clear_window=True ->bool 是否清空界面。"""
    final_string = '\n'
    max_x, max_y = _get_terminal_size()
    x, y = -1, -1
    while y < max_y - 1:
        final_string += '\n'
        y += 1

        #若行内无渲染内容则跳过
        sth_in_line = False
        for a in string_list:
            if a[2] == y:
                sth_in_line = True
                break
        if not sth_in_line:
            continue

        x = -1
        while x < max_x - 1:
            x += 1
            printed = False
            for n in range(0, len(string_list)):
                s = string_list[len(string_list) - n - 1] #从string_list的后往前渲染
                colors = [s[3], s[4]]
                if s[3] == 'default':
                    colors[0] = origin_colors[0]
                if s[4] == 'default':
                    colors[1] = origin_colors[1]
                if s[1] == x and s[2] == y:
                    now_print = s[0]
                    if x + _len_in_size(now_print) > max_x:
                        if len(now_print) == 1: #中文字符
                            now_print = _decorate_string(' ', colors[0], colors[1])
                        elif len(now_print) == 2: #英文字符
                            now_print = _decorate_string(now_print[0], colors[0], colors[1])
                    final_string += _decorate_string(now_print, colors[0], colors[1])
                    printed = True
                    x += _len_in_size(now_print) - 1
                    break
            if not printed:
                final_string += ' '
    if final_string[-1] == '\n':
        final_string += ' ' * max_x
    print(final_string[1:], end='', flush=True) #刷新print
    if clear_window:
        _clear()

def _clear():
    """清空界面。默认在TerminalRenderer.update()中调用。"""
    global string_list
    string_list = []

if __name__ == '__main__':
    os.system('cls')
    background = 'Welcome  TerminalRenderer  Welcome'
    while 1:
        print_in_pos(background, int(_get_terminal_size()[0] / 2) - int(_len_in_size(background) / 2), int(_get_terminal_size()[1] / 2))
        update()
        time.sleep(0.01)

if __name__ != '__main__':
    os.system('cls') #不明原因，在程序开始时必须清空一次才会正确显示
