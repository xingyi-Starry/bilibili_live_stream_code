"""
说明：跨平台系统API封装

作者：xingyistarry

版本：1.0.0

更新时间：2025-07-03
"""

import os
import sys
import subprocess
import platform
import ctypes
from ctypes import wintypes
import tkinter as tk
from tkinter import messagebox


def get_desktop_path() -> str:
    """
    获取桌面路径，跨平台实现
    :return: 桌面路径字符串
    """
    # Windows系统
    if platform.system() == "Windows":
        try:
            # 使用Windows API获取桌面路径
            buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
            ctypes.windll.shell32.SHGetFolderPathW(0, 0x0000, 0, 0, buf)
            return buf.value
        except Exception:
            # 备用方案：使用环境变量
            return os.path.join(os.path.expanduser("~"), "Desktop")
    
    # macOS系统
    elif platform.system() == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Linux系统
    elif platform.system() == "Linux":
        # 尝试读取用户目录配置
        try:
            with open(os.path.expanduser("~/.config/user-dirs.dirs"), "r") as f:
                for line in f:
                    if line.startswith("XDG_DESKTOP_DIR"):
                        return os.path.expanduser(line.split("=")[1].strip().strip('"'))
        except Exception:
            pass
        
        # 备用方案：使用标准桌面路径
        return os.path.join(os.path.expanduser("~"), "Desktop")
    
    # 其他系统，返回用户主目录
    return os.path.expanduser("~")


def show_message_box(message: str, title: str, is_error: bool = False) -> None:
    """
    显示消息框，跨平台实现
    :param message: 消息内容
    :param title: 标题
    :param is_error: 是否为错误消息
    :return: None
    """
    # Windows系统，使用原生API
    if platform.system() == "Windows":
        try:
            # 定义常量
            MB_OK = 0x00000000
            MB_ICONERROR = 0x00000010
            MB_ICONWARNING = 0x00000030
            
            MB_ICON = MB_ICONERROR if is_error else MB_ICONWARNING
            ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICON)
            return
        except Exception:
            # 如果失败，使用Tkinter作为备选
            pass
    
    # 使用Tkinter (跨平台)
    try:
        # 创建一个临时的根窗口
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        
        # 显示消息框
        if is_error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)
        
        # 销毁临时窗口
        root.destroy()
    except Exception as e:
        # 如果GUI显示失败，回退到控制台输出
        print(f"\n{title}: {message}\n")
        print(f"错误: {str(e)}")


def custom_pause(context: str, exit_code: int, title: str) -> None:
    """
    显示消息并等待用户确认，跨平台实现
    :param context: 提示信息
    :param exit_code: 退出码
    :param title: 提示框标题
    :return: None
    """
    message = context + '\n\n退出码：' + str(exit_code) + '\n\n点击确定退出程序......'
    show_message_box(message, title, exit_code != 0)


def startfile(file_path: str) -> bool:
    """
    打开文件，跨平台实现
    :param file_path: 文件路径
    :return: 是否成功打开
    """
    if not os.path.exists(file_path):
        return False
    
    try:
        # Windows系统
        if platform.system() == "Windows":
            os.startfile(file_path)
        
        # macOS系统
        elif platform.system() == "Darwin":
            subprocess.call(["open", file_path])
        
        # Linux系统
        elif platform.system() == "Linux":
            subprocess.call(["xdg-open", file_path])
        
        # 其他系统
        else:
            return False
        
        return True
    except Exception:
        return False


def open_url(url: str) -> bool:
    """
    打开URL，跨平台实现
    :param url: URL地址
    :return: 是否成功打开
    """
    import webbrowser
    try:
        webbrowser.open(url)
        return True
    except Exception:
        return False
