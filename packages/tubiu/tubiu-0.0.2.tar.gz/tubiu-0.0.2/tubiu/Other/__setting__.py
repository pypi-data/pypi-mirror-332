#BUILD __SETTING__.py
import os
import ctypes
import sys
import warnings
from typing import Dict, Optional, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from ctypes import WinDLL

# 禁用 ctypes 警告
warnings.filterwarnings("ignore", category=UserWarning)

class _DLLProxy:
    """实现动态 DLL 访问 + 类型提示"""
    def __getattr__(self, name: str) -> "WinDLL":
        dll = _DLLLoader.load(name)
        if dll is None:
            raise AttributeError(f"Windows DLL '{name}' not found or failed to load")
        return dll

class _DLLLoader:
    """DLL 加载核心（单例模式）"""
    _instance: Optional["_DLLLoader"] = None
    _dll_cache: Dict[str, "WinDLL"] = {}

    # 预定义 100+ DLL 名称清单（部分示例）
    _KNOWN_DLLS = {
        # 基础系统
        "user32", "kernel32", "gdi32", "shell32", "advapi32", "ole32",
        "ws2_32", "winmm", "comctl32", "shlwapi", "version", "oleaut32",
        # 图形/多媒体
        "d2d1", "dwrite", "d3d11", "dxgi", "dwmapi", "mfplat", "msimg32",
        # 网络/安全
        "wlanapi", "winhttp", "ncrypt", "secur32", "crypt32", "iphlpapi",
        # 硬件/驱动
        "setupapi", "hid", "winusb", "cfgmgr32", "xinput1_4", "dinput8",
        # 系统工具
        "psapi", "dbghelp", "powrprof", "wtsapi32", "taskeng", "winsta",
        # 扩展部分（新增60+）
        "amsi", "bcrypt", "cryptnet", "rasapi32", "credui", "textinputframework",
        "twinapi", "directml", "vulkan-1", "dxcompiler", "mfreadwrite", "avrt",
        "msacm32", "dxva2", "wmcodecdspuuid", "sensorsapi", "websocket", "ntdll",
        "shcore", "propsys", "msctf", "inputhost", "windowsudk", "wldap32",
        "dnsapi", "odbc32", "gdiplus", "msvcrt", "comdlg32", "winspool",
        "wintrust", "sensapi", "imm32", "netapi32", "odbc32", "msi", "d3d12",
        "d3dcompiler_47", "wininet", "urlmon", "oleacc", "uiautomationcore"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_dlls()
        return cls._instance

    def _init_dlls(self):
        """预加载常用DLL提升性能"""
        preload_list = {"user32", "kernel32", "shell32"}
        for name in preload_list:
            self.load(name)

    @classmethod
    def load(cls, name: str) -> Optional["WinDLL"]:
        """动态加载DLL（带缓存）"""
        if name in cls._dll_cache:
            return cls._dll_cache[name]

        path = cls._resolve_path(name)
        if not path:
            return None

        try:
            dll = ctypes.WinDLL(path)
            cls._dll_cache[name] = dll
            return dll
        except OSError:
            return None

    @staticmethod
    def _resolve_path(name: str) -> Optional[str]:
        """智能解析DLL路径"""
        # 特殊路径处理
        special_paths = {
            "winspool": os.path.join(os.environ["SystemRoot"], "System32", "winspool.drv"),
            "gdiplus": os.path.join(os.environ["SystemRoot"], "System32", "gdiplus.dll"),
            "vulkan-1": "vulkan-1.dll" if sys.maxsize > 2**32 else "vulkan-1.dll"
        }
        if name in special_paths:
            return special_paths[name]

        # 标准DLL直接查找
        return ctypes.util.find_library(name) or ctypes.util.find_library(name + ".dll")

# 创建代理实例（类型注解实现智能提示）
windll: Type[_DLLProxy] = _DLLProxy()

__author__ = "Huang Yiyi"
__version__ = "0.0.2"