"""
LogWrapper\n
日志包装器\n
使程序的错误报告存储到 log 目录中\n
By ATN\n
函数列表：\n
logwrap\n
使用方法：
@LogWrapper
def main():
    ...
"""

import time, traceback, os, sys

def _write_log(fname, text):
    '''保存日志\n
    fname ->str 文件名。无需.txt后缀\n
    text ->str 日志内容\n'''
    try:
        fi = open('log\\' + fname + '.txt', 'a', encoding="utf8")
    except FileNotFoundError:
        os.makedirs('log')
        fi = open('log\\' + fname + '.txt', 'a', encoding="utf8")
    fi.write(text + '\n')
    fi.close()

def logwrap(func):
    '''对修饰函数进行日志包装并立刻执行\n
    func ->function 需要修饰的函数\n'''
    try:
        func()
    except SystemExit:
        os.system('cls')
        os.system("color F0")
        sys.exit()
    except Exception:
        os.system("color F0")
        print('-' * 50)
        print("(#)游戏出错。")
        now_time = time.localtime()
        log_time = "error" + str(now_time[0]) + 'Y' + str(now_time[1]) + 'M' + str(now_time[2]) + 'D' + str(now_time[3]) + 'h' + str(now_time[4]) + 'm' + str(now_time[5]) + 's'
        log_text = traceback.format_exc()
        _write_log(log_time, log_text)
        print("(#)错误日志已保存在游戏目录log文件夹下。")
        print(log_text)
        input()