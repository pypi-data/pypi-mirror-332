#Copyright (c) 2025, <363766687@qq.com>
#Author: Huang Yiyi
import ctypes
import os
#from tubiu.__TUBIU__ import TubiuError

user32 = ctypes.windll.user32
shell32 = ctypes.windll.shell32
kernel32 = ctypes.windll.kernel32
ole32 = ctypes.windll.ole32
ws2_32 = ctypes.windll.ws2_32
winmm = ctypes.windll.winmm
gdi32 = ctypes.windll.gdi32
advapi32 = ctypes.windll.advapi32
odbc32 = ctypes.windll.odbc32
msimg32 = ctypes.windll.msimg32
_system32_path = os.path.join(os.environ['SystemRoot'], 'System32')
_winspool_path = os.path.join(_system32_path, 'winspool.drv')
system32 = os.path.join(os.environ['SystemRoot'], 'System32')

try:
    winspool = ctypes.windll.LoadLibrary(_winspool_path)
except Exception:
    #TubiuError(f"Error loading winspool.drv: {e}")
    pass

setupapi = ctypes.windll.setupapi
crypt32 = ctypes.windll.crypt32
netapi32 = ctypes.windll.netapi32
__author__ = "Huang Yiyi"
__version__ = "0.0.1"

__all__ = ["user32","shell32","kernel32","ole32","ws2_32",
           "winmm","gdi32","advapi32","odbc32","msimg32",
           "winspool","setupapi","crypt32","netapi32","system32",]