#cython: language_level=3
#cython: c_string_type=bytes; c_string_encoding='utf-8'
#cython: warn.unreachable=False

#Copyright (c) 2025, <363766687@qq.com>
#Author: Huang Yiyi

import sys
import os, re
import subprocess
import pywintypes
import pyperclip
import winreg
from typing import Optional
import platform as platformd
from Other.importcode import output as __D__
from typing import Optional, Dict, TextIO
import threading
from Other import CommunicationResult
import warnings, types, inspect

def raise_in_user_frame(func):
    """装饰器：将函数内抛出的异常堆栈直接定位到用户调用代码"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 获取用户调用帧（跳过装饰器层）
            stack = inspect.stack()
            user_frame = None
            for frame_info in stack[2:]:  # 跳过装饰器和被装饰函数
                if __file__ not in frame_info.filename:  # 排除库内部帧
                    user_frame = frame_info.frame
                    break

            if user_frame:
                # 构造新的 traceback
                tb = types.TracebackType(
                    tb_next=None,
                    tb_frame=user_frame,
                    tb_lasti=user_frame.f_lasti,
                    tb_lineno=user_frame.f_lineno
                )
                e.__traceback__ = tb
            raise e
    return wrapper

class TubiuError(Exception):
    """Custom exception class for print operations"""
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.original_error = original_error

__TubiuError__ = TubiuError

class platform:
    def __cinit__(self):  # 使用__cinit__代替__new__
        sys_platform = sys.platform
        if sys_platform.startswith("win"):
            self.system = "windows"
        elif sys_platform == "darwin":
            self.system = "macos"
        elif sys_platform.startswith("linux"):
            self.system = "linux"
        else:
            self.system = sys_platform

    def __str__(self):
        return self.system

class PATH:
    """
    About system or environment variables.
    Examples:
        path_manager = PATH()

        # 获取 PATH 列表
        print("当前 PATH 列表:", path_manager.get_environment_vars())

        # 获取所有系统变量字典
        system_vars = path_manager.get_system_vars()
        print("系统变量示例:", list(system_vars.keys())[:3])

        # 添加新路径到 PATH
        path_manager.add_to_environment("/usr/local/custom_bin")
        print("更新后的 PATH:", path_manager.get_environment_vars()[-1])

        # 设置新环境变量
        path_manager.set_variable("MY_APP_CONFIG", "/etc/myapp/config.ini")
        print("MY_APP_CONFIG 值:", os.environ.get("MY_APP_CONFIG"))

    Note: Persistence operations involve system
    permissions and security, and should be used
    with caution!
    """
    @raise_in_user_frame
    def __init__(self):
        # 确定路径分隔符（Windows用';'，类Unix用':'）
        self.separator = ';' if sys.platform.startswith('win') else ':'

    def get_environment_vars(self) -> list:
        """获取当前环境变量 PATH 的列表形式"""
        path_str = os.environ.get('PATH', '')
        return path_str.split(self.separator) if path_str else []

    def get_system_vars(self) -> dict:
        """获取所有系统环境变量（字典形式）"""
        return dict(os.environ)

    def update_environment_vars(self, new_path_list: list) -> None:
        """更新环境变量 PATH"""
        os.environ['PATH'] = self.separator.join(new_path_list)

    def add_to_environment(self, path: str) -> None:
        """向环境变量 PATH 中添加新路径（自动去重）"""
        current_path = self.get_environment_vars()
        if path not in current_path:
            current_path.append(path)
            self.update_environment_vars(current_path)

    def set_variable(self, name: str, value: str) -> None:
        """设置或更新系统环境变量（键值对形式）"""
        os.environ[name] = value

    def remove_variable(self, name: str) -> None:
        """删除系统环境变量"""
        if name in os.environ:
            del os.environ[name]

    def save_to_system(self):
        """Persist to the system (requires administrator privileges)"""
        try:
            sys_platform = platform()
            if sys_platform == "windows":
                self._save_windows()
            elif sys_platform == "linux":
                self._save_linux()
            elif sys_platform == "macos":
                self._save_macos()
            else:
                raise TubiuError("Unsupported operating systems.")
        except PermissionError as e:
            raise TubiuError("Administrator privileges are required to do this.", original_error=e)
        

    def _save_windows(self):
        # 使用 winreg 操作注册表
        import winreg
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:
            with winreg.OpenKey(root, "Environment", 0, winreg.KEY_WRITE) as key:
                for name, value in self.get_system_vars().items():
                    winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)

    def _save_linux(self):
        # 写入 ~/.bashrc 或 /etc/environment
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            for k, v in self.get_system_vars().items():
                f.write(f'\nexport {k}="{v}"')

    def _save_macos(self):
        """macOS 环境变量持久化（写入 ~/.zshrc）"""
        try:
            config_file = os.path.expanduser("~/.zshrc")
            if not os.path.exists(config_file):
                open(config_file, 'w').close()

            with open(config_file, 'a') as f:
                for name, value in self.get_system_vars().items():
                    if name == 'PATH':
                        # 特殊处理 PATH 变量
                        f.write(f'\nexport PATH="{self.separator.join(self.get_environment_vars())}:$PATH"')
                    else:
                        f.write(f'\nexport {name}="{value}"')
            
            # 使当前shell环境立即生效（需要用户手动 source 或重启终端）
            subprocess.run(['source', config_file], shell=True, check=True)
        except (IOError, subprocess.CalledProcessError) as e:
            raise TubiuError(f"保存macOS环境变量失败: {str(e)}", original_error=e)

class Exit:
    """
    Exit
    ~~~~
    Close the Python interpreter, but the code that
    follows the class will no longer work.
    """
    @raise_in_user_frame
    def __init__(self,code = 0):
        sys.exit(code)

class Serve:
    """
    Serve
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    About Windows services.
    """
    @raise_in_user_frame
    def __init__(self):
        if not __check_pywin32_installed__():
            return
        
        global win32service, win32serviceutil
        import win32serviceutil
        import win32service
        if not sys.platform.startswith('win'):
            raise TubiuError("This feature is only available for Windows systems.")

    def _handle_win_error(self, action: str, error: Exception):
        """Unified handling of Windows API errors."""
        raise TubiuError(f"Service operation failed ({action}): {str(error)}", original_error=error)
    @raise_in_user_frame
    def get_service_status(self, service_name: str) -> str:
        """Get the status of the service."""
        try:
            status = win32serviceutil.QueryServiceStatus(service_name)[1]
            states = {
                win32service.SERVICE_STOPPED: 'Stopped',
                win32service.SERVICE_RUNNING: 'Running',
                win32service.SERVICE_PAUSED: 'Paused',
            }
            return states.get(status, 'Unknown status')
        except pywintypes.error as e:
            self._handle_win_error("Query the service status.", e)
    @raise_in_user_frame
    def start_service(self, service_name: str, timeout: int = 30) -> None:
        """Start the service."""
        try:
            win32serviceutil.StartService(service_name)
            win32serviceutil.WaitForServiceStatus(service_name, win32service.SERVICE_RUNNING, timeout)
        except pywintypes.error as e:
            self._handle_win_error("Start the service", e)
    @raise_in_user_frame
    def stop_service(self, service_name: str, timeout: int = 30) -> None:
        """Discontinuation of service."""
        try:
            win32serviceutil.StopService(service_name)
            win32serviceutil.WaitForServiceStatus(service_name, win32service.SERVICE_STOPPED, timeout)
        except pywintypes.error as e:
            self._handle_win_error("Discontinuation of service.", e)
    @raise_in_user_frame
    def create_service(self, 
                      service_name: str,
                      display_name: str,
                      binary_path: str,
                      start_type: str = 'manual') -> None:
        """Create a new service."""
        try:
            start_type_map = {
                'auto': win32service.SERVICE_AUTO_START,
                'manual': win32service.SERVICE_DEMAND_START,
                'disabled': win32service.SERVICE_DISABLED
            }
            win32serviceutil.CreateService(
                None,  # 使用本地计算机
                service_name,
                display_name,
                binaryPathName=binary_path,
                startType=start_type_map[start_type.lower()]
            )
        except pywintypes.error as e:
            self._handle_win_error("Create a new service.", e)
    @raise_in_user_frame
    def delete_service(self, service_name: str) -> None:
        """Delete the service."""
        try:
            win32serviceutil.RemoveService(service_name)
        except pywintypes.error as e:
            self._handle_win_error("Delete the service.", e)
    @raise_in_user_frame
    def set_startup_type(self, service_name: str, start_type: str) -> None:
        """Modify the service startup type."""
        try:
            type_map = {
                'auto': win32service.SERVICE_AUTO_START,
                'manual': win32service.SERVICE_DEMAND_START,
                'disabled': win32service.SERVICE_DISABLED
            }
            win32serviceutil.ChangeServiceConfig(
                service_name,
                startType=type_map[start_type.lower()]
            )
        except pywintypes.error as e:
            self._handle_win_error("Modify the service startup type.", e)

class Clipboard:
    """Some operations on the clipboard."""
    @raise_in_user_frame
    def __init__(
        self, 
        content: Optional[str] = None, 
        modify: bool = False, 
        get: bool = False
    ):
        """
        Parameter description:
        - content: The content to be saved to the clipboard (only if modify=True takes effect)
        - modify: Whether to modify the clipboard content
        - get: Whether to get clipboard content (higher priority than modify)
        """
        self._content = content
        
        if get:
            self._get_from_clipboard()
        elif modify:
            self._set_to_clipboard()

    def _set_to_clipboard(self) -> None:
        """Write the content to the clipboard."""
        try:
            if self._content is None:
                raise TubiuError("Unable to save empty content to the clipboard.")
            
            # 使用跨平台库 pyperclip 实现
            pyperclip.copy(self._content)
            
            # 验证写入是否成功（可选）
            if platform() != "windiws":
                # 非Windows系统可能需要额外验证
                read_back = pyperclip.paste()
                if read_back != self._content:
                    raise TubiuError("Clipboard content validation failed.")
        except Exception as e:
            raise TubiuError(f"Failed to write to clipboard: {str(e)}", original_error=e)

    def _get_from_clipboard(self) -> None:
        """Read content from the clipboard."""
        try:
            self._content = pyperclip.paste()
        except Exception as e:
            raise TubiuError(f"Failed to read clipboard: {str(e)}", original_error=e)

    @property
    def content(self) -> str:
        """Get current content (cached value or clipboard content)"""
        if self._content is None:
            self._get_from_clipboard()
        return self._content

    @classmethod
    @raise_in_user_frame
    def clear(cls) -> None:
        """清空剪切板"""
        try:
            # 根据不同平台使用原生命令
            system = platform()
            if system == "windows":
                subprocess.run(['cmd', '/c', 'echo off | clip'], check=True)
            elif system == "macos":
                subprocess.run(['pbcopy', ''], check=True)
            else:  # Linux
                subprocess.run(['xclip', '-selection', 'c', '-i', '/dev/null'], check=True)
        except subprocess.CalledProcessError as e:
            raise TubiuError(f"Failed to empty the clipboard: {str(e)}", original_error=e)
        
    @staticmethod
    @raise_in_user_frame
    def is_image_available() -> bool:
        """
        Detect whether there are pictures on the clipboard
        (supported by Windows/macOS only).
        """
        try:
            if platformd.system() == "Windows":
                import win32clipboard
                win32clipboard.OpenClipboard()
                fmt = win32clipboard.EnumClipboardFormats(0)
                while fmt:
                    if fmt == win32clipboard.CF_DIB:
                        return True
                    fmt = win32clipboard.EnumClipboardFormats(fmt)
                return False
            elif platformd.system() == "Darwin":
                return subprocess.run(['osascript', '-e', 'clipboard info'], capture_output=True).stdout.decode().find('TIFF') != -1
            else:
                raise TubiuError("Linux does not support image detection.")
        except Exception as e:
            raise TubiuError("Image detection failed.", original_error=e)

    @classmethod
    @raise_in_user_frame
    def get_image(cls) -> bytes:
        """Get Clipboard Pictures (Windows/macOS)."""
        try:
            if platformd.system() == "Windows":
                import win32clipboard
                win32clipboard.OpenClipboard()
                if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
                    data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
                    win32clipboard.CloseClipboard()
                    return data
                else:
                    raise TubiuError("There are no pictures in the clipboard.")
            elif platformd.system() == "Darwin":
                return subprocess.check_output(['osascript', '-e', 'get the clipboard as «class PNGf»'])
            else:
                raise TubiuError("Linux does not support image acquisition.")
        except Exception as e:
            raise TubiuError("Failed to get the image.", original_error=e)

import shutil, hashlib

class Copy:
    @raise_in_user_frame
    def __init__(
        self,
        src: str,
        dest_dir: str,
        safe_copy: bool = False,
        overwrite: bool = False
    ):
        """
        Parameter description:
        - src: source path (file or folder)
        - dest_dir: The target parent directory
        - safe_copy: Enable security check (file-level check)
        - overwrite: Overwrites an existing target
        """
        self.src = os.path.normpath(src)
        self.dest_dir = os.path.normpath(dest_dir)
        self.safe_copy = safe_copy
        self.overwrite = overwrite
        self.dest_path = None

        self._validate()
        self._copy()

    def _validate(self) -> None:
        """验证路径有效性"""
        if not os.path.exists(self.src):
            raise TubiuError(f"Source path does not exist: {self.src}")

        # 确保目标父目录存在且可写
        try:
            os.makedirs(self.dest_dir, exist_ok=True)
            if not os.access(self.dest_dir, os.W_OK):
                raise TubiuError(f"Destination directory is not writable: {self.dest_dir}")
        except PermissionError as e:
            raise TubiuError(f"No permission to create directory: {self.dest_dir}", e)

    def _get_dest_path(self) -> str:
        """生成完整目标路径"""
        base_name = os.path.basename(self.src)
        return os.path.join(self.dest_dir, base_name)

    def _prepare_destination(self, dest_path: str) -> None:
        """处理覆盖逻辑"""
        if os.path.exists(dest_path):
            if self.overwrite:
                if os.path.isfile(dest_path):
                    os.remove(dest_path)
                else:
                    shutil.rmtree(dest_path)
            else:
                raise TubiuError(f"The target already exists and is not allowed to be overridden: {dest_path}")

    def _copy_file(self, src: str, dest: str) -> None:
        """复制单个文件"""
        # 执行实际复制操作
        shutil.copy2(src, dest)
        
        # 安全校验
        if self.safe_copy and self._file_hash(src) != self._file_hash(dest):
            os.remove(dest)
            raise TubiuError("File security verification failed.")

    def _copy_dir(self, src: str, dest: str) -> None:
        """递归复制文件夹"""
        try:
            # 创建目标目录结构
            os.makedirs(dest, exist_ok=True)
            
            # 遍历复制所有内容
            for item in os.listdir(src):
                src_path = os.path.join(src, item)
                dest_path = os.path.join(dest, item)
                
                if os.path.isdir(src_path):
                    self._copy_dir(src_path, dest_path)
                else:
                    self._copy_file(src_path, dest_path)
        except Exception as e:
            shutil.rmtree(dest, ignore_errors=True)
            raise TubiuError(f"Folder Copy Break: {str(e)}", e)

    def _file_hash(self, path: str) -> str:
        """计算文件哈希值"""
        hasher = hashlib.sha256()
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def _copy(self) -> None:
        """主复制逻辑"""
        dest_path = self._get_dest_path()
        self.dest_path = dest_path
        
        # 处理覆盖逻辑
        self._prepare_destination(dest_path)

        try:
            if os.path.isfile(self.src):
                self._copy_file(self.src, dest_path)
            else:
                self._copy_dir(self.src, dest_path)
        except shutil.Error as e:
            raise TubiuError(f"Error during copy: {str(e)}", e)

    def __repr__(self) -> bytes:  # 返回bytes类型
        return f"<Copy: {self.src} → {self.dest_path}>".encode('utf-8')
    
class output:
    """print(CMD,POWERSHELL)"""
    @raise_in_user_frame
    def __init__(self, *values,sep=" ", 
                 end="\n",file=None, 
                 flush=False) -> None:
        try:
            __D__(*values, sep=sep, end=end, file=file, flush=flush)
        except Exception as error:
            self.__tubiu__(error)

    def __tubiu__(self, error) -> None:
        raise TubiuError("print Error:",error)

class print:
    """
    Enhanced print class with ANSI color support
    Features:
    - Full 256-color and RGB support
    - Custom syntax: color="color[style][be background]"
    - Cross-platform compatibility
    
    Args:
        color (str): Color/style specification. Format:
            - Named colors: red, bright_blue, etc.
            - 256 colors: color123
            - RGB colors: rgb(255,0,0)
            - Styles: [bold], [italic], [underline]
            - Background: [be <color>]
        file: Output stream (default: sys.stdout)
        sep: Separator between arguments
        end: Ending character
        flush: Force flush output
    """
    # ANSI code mappings
    _STYLES: Dict[str, int] = {
        "bold": 1, "italic": 3, "underline": 4, 
        "blink": 5, "reverse": 7, "strike": 9
    }
    
    _NAMED_COLORS: Dict[str, int] = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "bright_black": 90, "bright_red": 91, "bright_green": 92,
        "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
        "bright_cyan": 96, "bright_white": 97
    }
    @raise_in_user_frame
    def __init__(self, *args,
                 color: Optional[str] = None,
                 file: TextIO = sys.stdout,
                 sep: str = " ",
                 end: str = "\n",
                 flush: bool = False):
        try:
            self._enable_ansi(file)
            self.text = sep.join(map(str, args)) + end
            self.file = file
            self.flush = flush
            
            ansi_code = self._parse_color(color)
            reset_code = "\033[0m" if ansi_code else ""
            
            self.file.write(f"{ansi_code}{self.text}{reset_code}")
            if flush:
                self.file.flush()
                
        except Exception as e:
            raise TubiuError(str(e), e)

    def _enable_ansi(self, file: TextIO):
        """Enable ANSI support on Windows"""
        if sys.platform == "win32" and file in (sys.stdout, sys.stderr):
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                handle = kernel32.GetStdHandle(-11 if file == sys.stdout else -12)
                kernel32.SetConsoleMode(handle, 0x0001 | 0x0002 | 0x0004)
            except Exception as e:
                raise TubiuError(f"Failed to enable ANSI: {str(e)}")

    def _parse_color(self, color: Optional[str]) -> bytes:
        """Parse color specification to ANSI codes"""
        if not color:
            return b""

        try:
            parts = re.findall(r'([^[]+)(\[.*?\]|$)', color)
            if not parts:
                return b""
            
            base_color, modifiers_str = parts[0]
            base_color = base_color.strip()
            modifiers = re.findall(r'\[(.*?)\]', modifiers_str)

            codes = []
            
            # Parse base color
            if base_color.startswith("color"):
                codes.append(f"38;5;{base_color[5:]}")
            elif base_color.startswith("rgb("):
                r, g, b = base_color[4:-1].split(",")
                codes.append(f"38;2;{r};{g};{b}")
            elif base_color in self._NAMED_COLORS:
                codes.append(str(self._NAMED_COLORS[base_color]))
            else:
                raise ValueError(f"Invalid color: {base_color}")

            # Parse modifiers
            for mod in modifiers:
                if mod.startswith("be "):
                    bg_color = mod[3:].strip()
                    if bg_color.startswith("color"):
                        codes.append(f"48;5;{bg_color[5:]}")
                    elif bg_color.startswith("rgb("):
                        r, g, b = bg_color[4:-1].split(",")
                        codes.append(f"48;2;{r};{g};{b}")
                    elif bg_color in self._NAMED_COLORS:
                        codes.append(str(self._NAMED_COLORS[bg_color] + 10))
                    else:
                        raise ValueError(f"Invalid background: {bg_color}")
                elif mod in self._STYLES:
                    codes.append(str(self._STYLES[mod]))
                else:
                    raise ValueError(f"Invalid modifier: {mod}")

            return f"\033[{';'.join(codes)}m".encode('ascii')
        
        except ValueError as e:
            raise TubiuError(str(e))

class Popen:
    @raise_in_user_frame
    def __init__(self, args, shell=False, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
        if shell:
            if platformd.system() == 'Windows':
                shell_cmd = ['cmd', '/c'] + args
            else:
                shell_cmd = ['sh', '-c'] + args
            args = shell_cmd

        self.args = args
        self.stdout_data = []
        self.stderr_data = []
        self.process = None
        self._start_process()

    def _start_process(self):
        try:
            self.process = subprocess.Popen(
                self.args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False
            )

            self.stdout_thread = threading.Thread(target=self._read_output, args=(self.process.stdout, self.stdout_data))
            self.stderr_thread = threading.Thread(target=self._read_output, args=(self.process.stderr, self.stderr_data))
            self.stdout_thread.start()
            self.stderr_thread.start()
        except Exception as e:
            print(f"Error starting process: {e}", file=sys.stderr)

    def _read_output(self, stream, data_list):
        try:
            encoding = 'gbk' if platform.system() == 'Windows' else 'utf-8'
            for line in iter(stream.readline, b''):
                try:
                    decoded_line = line.decode(encoding)
                except UnicodeDecodeError:
                    try:
                        decoded_line = line.decode('utf-8', errors='replace')
                    except UnicodeDecodeError:
                        continue
                data_list.append(decoded_line)
        except Exception as e:
            print(f"Error reading output: {e}", file=sys.stderr)
        finally:
            stream.close()

    def communicate(self, input_data=None):
        if self.process is None:
            return CommunicationResult("", f"Process failed to start: {self.args}", 1)

        if input_data:
            if isinstance(input_data, str):
                input_data = input_data.encode()
            self.process.stdin.write(input_data)
            self.process.stdin.flush()
        if self.process.stdin:
            self.process.stdin.close()

        if self.stdout_thread:
            self.stdout_thread.join()
        if self.stderr_thread:
            self.stderr_thread.join()

        if self.process:
            self.process.wait()
            status = self.process.returncode
            stdout_str = ''.join(self.stdout_data)
            stderr_str = ''.join(self.stderr_data)
            return CommunicationResult(stdout_str, stderr_str, status)
        return CommunicationResult("", "Process is None", 1)

    def wait(self):
        if self.process:
            self.process.wait()
            return self.process.returncode
        return 1
    
class Bytes:
    """
    Handling of bytes encoding.
    """
    #@raise_in_user_frame
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding
        try:
            if self._is_binary_file():
                with open(self.file_path, 'rb') as file:
                    self.bytes_data = file.read()
            else:
                with open(self.file_path, 'r', encoding=self.encoding) as file:
                    text_data = file.read()
                    self.bytes_data = text_data.encode(self.encoding)
        except FileNotFoundError:
            self.bytes_data = None
            raise TubiuError(f"The specified file was not found: {self.file_path}")
        except UnicodeDecodeError:
            self.bytes_data = None
            raise TubiuError(f"An encoding error occurred while reading the file, and the encoding {self.encoding} may be specified incorrectly.")
        except Exception as e:
            self.bytes_data = None
            raise TubiuError(f"Error: {e}")

    def _is_binary_file(self):
        """简单判断文件是否为二进制文件"""
        with open(self.file_path, 'rb') as file:
            head = file.read(1024)
            return b'\0' in head

    def __str__(self):
        if self.bytes_data is not None:
            return str(self.bytes_data)
        return "Unable to get byte data for file."
    @raise_in_user_frame
    def getbytes(self):
        """Get the bytes encoding."""
        return self.bytes_data
    @raise_in_user_frame
    def bytestofile(self, output_file_path, bytes_content=None):
        """Convert bytes encoding to files."""
        if bytes_content is None:
            bytes_content = self.bytes_data
        if bytes_content is None:
            raise TubiuError("There is no valid byte data available to write to the file.")

        try:
            if self._is_binary_file():
                with open(output_file_path, 'wb') as file:
                    file.write(bytes_content)
            else:
                text_data = bytes_content.decode(self.encoding)
                with open(output_file_path, 'w', encoding=self.encoding) as file:
                    file.write(text_data)
            #print(f"成功将字节数据写入文件: {output_file_path}")
        except UnicodeDecodeError:
            raise TubiuError(f"An encoding error occurred while writing to a file, and the encoding {self.encoding} may have been specified incorrectly.")
        except Exception as e:
            raise TubiuError(f"Error: {e}")
    
class notify:
    @raise_in_user_frame
    def __init__(self, title, message, app_name=None, timeout=5, icon=None):
        if not __check_pywin32_installed__():
            return
        
        from plyer import notification
        self.notification = notification
        self.title = title
        self.message = message
        self.app_name = app_name
        self.timeout = timeout
        self.icon = icon
        self.__notify__()

    def __notify__(self):
        if self.title is None:
            self.title = ""
        if self.message is None:
            self.message = ""
        if self.app_name is None:
            self.app_name = ""
        try:
            self.notification.notify(
                title=self.title,
                message=self.message,
                app_name=self.app_name,
                timeout=self.timeout,
                app_icon=self.icon
            )
        except Exception as e:
            raise TubiuError(f"Notify: {e}")

class Restrain:
    """
    Initialize the Restrain class to specify the type of warning you want to suppress.

    :param warning_type: The type of warning that needs to be suppressed.
    """
    @raise_in_user_frame
    def __init__(self, warning_type=None):
        """
        Initialize the Restrain class to specify the type of warning you want to suppress.

        :param warning_type: The type of warning that needs to be suppressed.
        """
        if warning_type is None:
            raise TubiuError("Please fill in the type of warning you want to suppress!")
        else:
            self.warning_type = warning_type
        
        # 创建 warnings 上下文管理器以保存和恢复过滤器状态
        self._warnings_context = warnings.catch_warnings()

    def __enter__(self):
        """Alert suppression is activated when entering the context."""
        self._warnings_context.__enter__()
        warnings.filterwarnings("ignore", category=self.warning_type)
        return self  # 可返回实例本身以便链式调用

    def __exit__(self, exc_type, exc_value, traceback):
        """Revert to the original warning settings when exiting the context."""
        self._warnings_context.__exit__(exc_type, exc_value, traceback)
    
class TubiuWarning(Warning):
    pass

class PyWin32NotInstalledWarning(TubiuWarning):
    pass

class PlyerNotInstalledWarning(TubiuWarning):
    pass

def __check__():
    try:
        from tubiu import Other, message, _Tcode
        from tubiu.Other import importcode,__setting__
        from tubiu.Other._ATTR_ import tubiu
        import tubiu as tubiu
        return True
    except ImportError:
        warnings.warn(
            "Missing features are detected, please reinstall this module, please execute the following command: 'pip uninstall tubiu', 'pip install tubiu'.",
            TubiuWarning,
            stacklevel=2
        )
        Exit(1)

def __check_pywin32_installed__():
    try:
        import win32api
        return True
    except ImportError:
        warnings.warn(
            "The pywin32 library is not detected and some features may be limited. Please run 'pip install pywin32' to install.",
            PyWin32NotInstalledWarning,
            stacklevel=2
        )
        return False
    
def __check_plyer_installed__():
    try:
        import plyer
        return True
    except ImportError:
        warnings.warn(
            "The plyer library is not detected and some features may be limited. Please run 'pip install plyer' to install.",
            PlyerNotInstalledWarning,
            stacklevel=2
        )
        return False

import mpmath

def pi(numbers):
    mpmath.mp.dps = numbers
    return mpmath.pi

def factorial(n):
    """计算阶乘"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin(x, num_terms=10):
    """使用泰勒级数展开计算正弦函数"""
    result = 0
    for n in range(num_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        result += term
    return result

def cos(x, num_terms=10):
    """使用泰勒级数展开计算余弦函数"""
    result = 0
    for n in range(num_terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        result += term
    return result

def tan(x, num_terms=10):
    """计算正切函数"""
    cos_value = cos(x, num_terms)
    if cos_value == 0:
        return float('inf')  # 当 cos 为 0 时，tan 为无穷大
    return sin(x, num_terms) / cos_value

def cot(x, num_terms=10):
    """计算余切函数"""
    tan_value = tan(x, num_terms)
    if tan_value == 0:
        return float('inf')  # 当 tan 为 0 时，cot 为无穷大
    return 1 / tan_value

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
def sqrt(a, tolerance=1e-6, max_iterations=100):
    x = a  # 初始猜测值
    for _ in range(max_iterations):
        f = x ** 2 - a
        f_prime = 2 * x
        delta_x = f / f_prime
        x -= delta_x
        if abs(delta_x) < tolerance:
            break
    return x

def exp(x, num_terms=10):
    result = 0
    for n in range(num_terms):
        term = (x ** n) / factorial(n)
        result += term
    return result

def ln(x, tolerance=1e-6, max_iterations=100):
    y = 1  # 初始猜测值
    for _ in range(max_iterations):
        f = exp(y) - x
        f_prime = exp(y)
        delta_y = f / f_prime
        y -= delta_y
        if abs(delta_y) < tolerance:
            break
    return y

def power(x, n):
    result = 1
    if n >= 0:
        for _ in range(n):
            result *= x
    else:
        for _ in range(-n):
            result /= x
    return result

import math

def combination(n, k):
    if k > n or k < 0:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def log10(x, tolerance=1e-6, max_iterations=100):
    """
    计算以 10 为底的对数 log10(x)
    :param x: 输入值
    :param tolerance: 收敛的容差
    :param max_iterations: 最大迭代次数
    :return: log10(x) 的近似值
    """
    ln_10 = ln(10, tolerance, max_iterations)
    return ln(x, tolerance, max_iterations) / ln_10

def sinh(x, num_terms=10):
    """
    计算双曲正弦函数 sinh(x) 的近似值
    :param x: 输入值
    :param num_terms: 计算指数函数时泰勒级数展开的项数
    :return: sinh(x) 的近似值
    """
    return (exp(x, num_terms) - exp(-x, num_terms)) / 2


def cosh(x, num_terms=10):
    """
    计算双曲余弦函数 cosh(x) 的近似值
    :param x: 输入值
    :param num_terms: 计算指数函数时泰勒级数展开的项数
    :return: cosh(x) 的近似值
    """
    return (exp(x, num_terms) + exp(-x, num_terms)) / 2


def tanh(x, num_terms=10):
    """
    计算双曲正切函数 tanh(x) 的近似值
    :param x: 输入值
    :param num_terms: 计算指数函数时泰勒级数展开的项数
    :return: tanh(x) 的近似值
    """
    sinh_val = sinh(x, num_terms)
    cosh_val = cosh(x, num_terms)
    return sinh_val / cosh_val

def floor(x):
    return int(x) if x >= 0 else int(x) - 1

def absolute_value(x):
    return x if x >= 0 else -x

def combination(n, k):
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def cmd(command):
    os.system(command)

def increase(file_extension=None, file_type=None, icon_path=None, associated_program=None):
    """
    :param file_extension 自定义后缀名
    :param file_type 自定义文件类型名称
    :param icon_path 图标文件路径，确保图标文件存在
    :param associated_program 关联的程序路径
    """
    if all(arg is None for arg in [file_extension, file_type, icon_path, associated_program]):
        print("Error: 至少需要提供一个参数")
        return
    try:
        if platform() == 'windows':
            try:
                if file_type:
                    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_type)
                    winreg.SetValue(key, "", winreg.REG_SZ, "Custom File")
                if icon_path and file_type:
                    icon_key = winreg.CreateKey(key, "DefaultIcon")
                    winreg.SetValue(icon_key, "", winreg.REG_SZ, icon_path)
                if associated_program and file_type:
                    shell_key = winreg.CreateKey(key, r"shell\open\command")
                    winreg.SetValue(shell_key, "", winreg.REG_SZ, f'"{associated_program}" "%1"')
                if file_extension and file_type:
                    ext_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_extension)
                    winreg.SetValue(ext_key, "", winreg.REG_SZ, file_type)
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if 'key' in locals():
                    winreg.CloseKey(key)
                if 'icon_key' in locals():
                    winreg.CloseKey(icon_key)
                if 'shell_key' in locals():
                    winreg.CloseKey(shell_key)
                if 'ext_key' in locals():
                    winreg.CloseKey(ext_key)
        elif platform() == 'macos':
            if file_extension and associated_program:
                try:
                    subprocess.run(["duti", "-s", associated_program, file_extension], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
        elif platform() == 'linux':
            if file_extension and associated_program:
                mime_type = subprocess.run(['xdg-mime', 'query', 'filetype', f'test{file_extension}'], capture_output=True, text=True).stdout.strip()
                try:
                    with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'a') as f:
                        f.write(f'[Default Applications]\n{mime_type}={associated_program}\n')
                except Exception as e:
                    print(f"Error: {e}")
    except Exception as e:
        raise Exception('increase Error:',e)
    

def delete(file_extension, file_type):
    """
    删除文件扩展名关联的函数
    :param file_extension: 要删除关联的文件扩展名
    :param file_type: 要删除关联的文件类型
    """
    if platform() == 'windows':
        try:
            try:
                ext_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, file_extension, 0, winreg.KEY_ALL_ACCESS)
                winreg.DeleteKey(ext_key, "")
                winreg.CloseKey(ext_key)
            except FileNotFoundError:
                pass
            try:
                key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, file_type, 0, winreg.KEY_ALL_ACCESS)
                winreg.DeleteKey(key, "")
                winreg.CloseKey(key)
            except FileNotFoundError:
                raise Exception('delete Error: 文件不存在')
        except Exception as e:
            print(f"Error: {e}")
    elif platform() == 'macos':
        if file_extension:
            try:
                subprocess.run(["duti", "-d", file_extension], check=True)
            except subprocess.CalledProcessError as e:
                raise Exception('delete Error:',e)
    elif platform() == 'linux':
        if file_extension:
            mime_type = subprocess.run(['xdg-mime', 'query', 'filetype', f'test{file_extension}'], capture_output=True, text=True).stdout.strip()
            try:
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'r') as f:
                    lines = f.readlines()
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'w') as f:
                    for line in lines:
                        if not line.startswith(f'{mime_type}='):
                            f.write(line)
            except Exception as e:
                raise Exception('delete Error:',e)
            

def modify(old_file_extension=None, old_file_type=None, new_file_extension=None, new_file_type=None,
           new_icon_path=None, new_associated_program=None):
    """修改 文件后缀名的关联 """
    new_params = [new_file_extension, new_file_type, new_icon_path, new_associated_program]
    if all(arg is None for arg in new_params):
        print("Error: 至少需要提供一个新参数进行修改")
        return
    if platform() == 'windows':
        try:
            if old_file_extension and old_file_type:
                try:
                    ext_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, old_file_extension, 0, winreg.KEY_ALL_ACCESS)
                    winreg.DeleteKey(ext_key, "")
                    winreg.CloseKey(ext_key)
                except FileNotFoundError:
                    pass
                try:
                    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, old_file_type, 0, winreg.KEY_ALL_ACCESS)
                    winreg.DeleteKey(key, "")
                    winreg.CloseKey(key)
                except FileNotFoundError:
                    pass
            increase(new_file_extension, new_file_type, new_icon_path, new_associated_program)
        except Exception as e:
            raise Exception('modify Error:',e)
    elif platform() == 'macos':
        if old_file_extension:
            try:
                subprocess.run(["duti", "-d", old_file_extension], check=True)
            except subprocess.CalledProcessError as e:
                raise Exception('modify Error:',e)
        increase(new_file_extension, new_file_type, new_icon_path, new_associated_program)
    elif platform() == 'linux':
        if old_file_extension:
            mime_type = subprocess.run(['xdg-mime', 'query', 'filetype', f'test{old_file_extension}'], capture_output=True, text=True).stdout.strip()
            try:
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'r') as f:
                    lines = f.readlines()
                with open(os.path.expanduser('~/.local/share/applications/mimeapps.list'), 'w') as f:
                    for line in lines:
                        if not line.startswith(f'{mime_type}='):
                            f.write(line)
            except Exception as e:
                raise Exception('modify Error:',e)
        increase(new_file_extension, new_file_type, new_icon_path, new_associated_program)

# Usage examples
if __name__ == "__main__":
    from message import askquestion
    try:
        askquestion("Build","Test")
        # System
        __System__ = platform()
        print("Your system is:",__System__,  )

        # Named color with style
        print("Error message", color="red[bold]", file=sys.stderr)
        
        # 256-color
        print("Color palette", color="color214[be color20]")
        
        # RGB color
        print("Custom RGB", color="rgb(255,150,0)[italic]")
        
        # Invalid color (will raise TubiuError)
        #print("Test", color="invalid_color[bold]")
        
    except __TubiuError__ as __e__:
        print(f"Operation failed: {str(__e__)}")