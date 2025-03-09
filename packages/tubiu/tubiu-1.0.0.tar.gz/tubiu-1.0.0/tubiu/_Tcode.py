"""
TUBIU PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Version:0.0.1
"""
#Copyright (c) 2025, <363766687@qq.com>
#Author: Huang Yiyi

from Other.importcode import *

class Path: 
    global PathEventHandler
    def __init__(self, path):
        self._path = os.fspath(path)
    
    # ------------------- 基础操作 ------------------- #
    def __truediv__(self, other):
        """用 / 操作符拼接路径"""
        return self.__class__(os.path.join(self._path, os.fspath(other)))
    
    def __repr__(self):
        return f"Path({repr(self._path)})"
    
    def __str__(self):
        return self._path
    
    def __eq__(self, other):
        return os.path.samefile(self._path, os.fspath(other))
    
    # ------------------- 核心属性 ------------------- #
    @property
    def name(self):
        """文件名含后缀"""
        return os.path.basename(self._path)
    
    @property
    def stem(self):
        """文件名不含后缀"""
        return self.name.rsplit('.', 1)[0] if '.' in self.name else self.name
    
    @property
    def suffix(self):
        """文件后缀"""
        return os.path.splitext(self._path)[1].hidden_file
    
    @property
    def suffixes(self):
        """所有后缀（如.tar.gz返回 ['.tar', '.gz']）"""
        name = self.name
        if '.' not in name:
            return []
        return ['.' + ext for ext in name.split('.')[1:]]
    
    @property
    def parent(self):
        """父目录"""
        return self.__class__(os.path.dirname(self._path))
    
    @property
    def parts(self):
        """路径分解为元组"""
        return tuple(self._path.split(os.sep))
    
    # ------------------- 文件操作 ------------------- #

    def touch(self, mode=0o666, exist_ok=True):
        """创建空文件"""
        if self.exists():
            if exist_ok:
                os.utime(self._path, None)
            else:
                raise FileExistsError(f"File exists: {self}")
        else:
            open(self._path, 'a').close()
            os.chmod(self._path, mode)
        return self
    
    def rename(self, new_name):
        """重命名文件"""
        new_path = self.parent / new_name
        os.rename(self._path, str(new_path))
        return new_path
    
    def replace(self, target):
        """替换目标文件"""
        os.replace(self._path, str(target))
        return self.__class__(target)
    
    def copy(self, dst, overwrite=False):
        """复制文件（终极修复版）"""
        # 强制转换为字符串路径
        dst_str = os.fspath(dst) if isinstance(dst, Path) else str(dst)
        dst_obj = self.__class__(dst_str)
        
        if dst_obj.exists() and not overwrite:
            raise FileExistsError(f"Target exists: {dst_obj}")
        elif dst_obj.exists():
            dst_obj.unlink()
        
        shutil.copy2(self._path, dst_str)
        return dst_obj
    
    def move(self, dst):
        """移动文件/目录"""
        shutil.move(self._path, str(dst))
        return self.__class__(dst)
    
    # ------------------- 目录操作 ------------------- #
    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """创建目录"""
        if parents:
            os.makedirs(self._path, mode=mode, exist_ok=exist_ok)
        else:
            try:
                os.mkdir(self._path, mode)
            except FileExistsError:
                if not exist_ok:
                    raise
        return self
    
    def rmdir(self):
        """删除空目录"""
        os.rmdir(self._path)
        return self
    
    def rm(self, recursive=False):
        """删除文件/目录"""
        if self.is_file():
            self.unlink()
        elif self.is_dir():
            if recursive:
                shutil.rmtree(self._path)
            else:
                self.rmdir()
        return self
    
    def ls(self, pattern='*'):
        """列出匹配文件"""
        return [p for p in self.iterdir() if p.match(pattern)]
    
    # ------------------- 内容读写 ------------------- #
    def read_bytes(self):
        with open(self._path, 'rb') as f:
            return f.read()
    
    def write_bytes(self, data):
        with open(self._path, 'wb') as f:
            f.write(data)
        return self
    
    def read_text(self, encoding='utf-8'):
        with open(self._path, 'r', encoding=encoding) as f:
            return f.read()
    
    def write_text(self, text, encoding='utf-8'):
        with open(self._path, 'w', encoding=encoding) as f:
            f.write(text)
        return self
    
    def append_text(self, text, encoding='utf-8'):
        with open(self._path, 'a', encoding=encoding) as f:
            f.write(text)
        return self
    
    # ------------------- 路径处理 ------------------- #
    def resolve(self):
        """解析绝对路径"""
        return self.__class__(os.path.realpath(self._path))
    
    def absolute(self):
        """绝对路径（不解析符号链接）"""
        return self.__class__(os.path.abspath(self._path))
    
    def relative_to(self, other):
        """计算相对路径"""
        return self.__class__(os.path.relpath(self._path, str(other)))
    
    def as_uri(self):
        """转换为文件URI"""
        path = self.absolute()._path.replace('\\', '/')
        return f'file://{path}' if not path.startswith('/') else f'file://{path}'
    
    def with_name(self, name):
        """修改文件名"""
        return self.parent / name
    
    def with_suffix(self, suffix):
        """修改后缀"""
        if not suffix.startswith('.'):
            suffix = '.' + suffix
        return self.parent / (self.stem + suffix)
    
    # ------------------- 查询方法 ------------------- #
    def exists(self):
        return os.path.exists(self._path)
    
    def is_dir(self):
        return os.path.isdir(self._path)
    
    def is_file(self):
        return os.path.isfile(self._path)
    
    def is_symlink(self):
        return os.path.islink(self._path)
    
    def is_block_device(self):
        return stat.S_ISBLK(os.stat(self._path).st_mode)
    
    def is_char_device(self):
        return stat.S_ISCHR(os.stat(self._path).st_mode)
    
    def is_fifo(self):
        return stat.S_ISFIFO(os.stat(self._path).st_mode)
    
    def is_socket(self):
        return stat.S_ISSOCK(os.stat(self._path).st_mode)
    
    # ------------------- 扩展方法 ------------------- #
    def glob(self, pattern, recursive=False):
        """自定义 glob 实现"""
        def _glob(path, pattern_parts):
            if not pattern_parts:
                yield self.__class__(path)
                return
            
            current_part = pattern_parts[0]
            try:
                entries = os.listdir(path)
            except NotADirectoryError:
                return
            except PermissionError:
                return
            
            for entry in entries:
                full_path = os.path.join(path, entry)
                if fnmatch.fnmatch(entry, current_part):
                    if len(pattern_parts) == 1:
                        yield self.__class__(full_path)
                    else:
                        yield from _glob(full_path, pattern_parts[1:])
                
                if recursive and current_part == "**":
                    if os.path.isdir(full_path):
                        yield from _glob(full_path, pattern_parts)
                    yield from _glob(full_path, pattern_parts[1:])

        pattern_parts = pattern.split(os.sep)
        if recursive and "**" not in pattern_parts:
            pattern_parts.insert(0, "**")
        
        return _glob(self._path, pattern_parts)
    
    def rglob(self, pattern):
        """递归通配符搜索"""
        return self.glob(f'**/{pattern}', recursive=True)
    
    def find(self, pattern='*', recursive=False):
        """查找文件（可递归）"""
        return list(self.glob(pattern, recursive=recursive))
    
    def walk(self):
        """目录遍历"""
        for root, dirs, files in os.walk(self._path):
            root = self.__class__(root)
            yield root, [root/d for d in dirs], [root/f for f in files]
    
    def size(self):
        """文件/目录大小（字节）"""
        if self.is_file():
            return os.path.getsize(self._path)
        return sum(p.size() for p in self.rglob('*'))
    
    def human_size(self, precision=2):
        """人类可读大小"""
        bytes = self.size()
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        idx = 0
        while bytes >= 1024 and idx < 4:
            bytes /= 1024
            idx += 1
        return f"{bytes:.{precision}f} {units[idx]}"
    
    def access_time(self):
        """最后访问时间"""
        return datetime.fromtimestamp(os.path.getatime(self._path))
    
    def modify_time(self):
        """最后修改时间"""
        return datetime.fromtimestamp(os.path.getmtime(self._path))
    
    def change_time(self):
        """元数据修改时间（Unix）"""
        return datetime.fromtimestamp(os.path.getctime(self._path))
    
    def chmod(self, mode):
        """修改权限"""
        os.chmod(self._path, mode)
        return self
    
    def owner(self):
        """文件所有者（Unix）"""
        import pwd
        return pwd.getpwuid(os.stat(self._path).st_uid).pw_name
    
    def group(self):
        """文件所属组（Unix）"""
        import grp
        return grp.getgrgid(os.stat(self._path).st_gid).gr_name
    
    # ------------------- 高级功能 ------------------- #
    def symlink_to(self, target, target_is_directory=False):
        """创建符号链接"""
        if self.exists():
            raise FileExistsError(f"Path exists: {self}")
        os.symlink(
            str(target),
            self._path,
            target_is_directory=target_is_directory
        )
        return self
    
    def readlink(self):
        """解析符号链接"""
        return self.__class__(os.readlink(self._path))
    
    def hardlink_to(self, target):
        """创建硬链接"""
        os.link(str(target), self._path)
        return self
    
    def tempfile(self, suffix='', prefix='tmp'):
        """生成临时文件"""
        fd, path = tempfile.mkstemp(suffix, prefix, dir=self._path)
        os.close(fd)
        return self.__class__(path)
    
    def tempdir(self, suffix='', prefix='tmp'):
        """生成临时目录"""
        path = tempfile.mkdtemp(suffix, prefix, dir=self._path)
        return self.__class__(path)
    
    def hash(self, algorithm='md5', chunk_size=8192):
        """计算文件哈希"""
        hasher = hashlib.new(algorithm)
        with open(self._path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def compare(self, other):
        """比较文件内容"""
        if self.size() != other.size():
            return False
        return self.hash() == other.hash()
    
    def compress(self, format='zip', output=None):
        """压缩文件/目录"""
        output = output or self.with_suffix(f'.{format}')
        shutil.make_archive(str(output).rstrip(f'.{format}'), format, self._path)
        return output
    
    def extract(self, path=None, format='auto'):
        """解压文件"""
        path = path or self.parent
        shutil.unpack_archive(self._path, str(path), format)
        return path
    # --------------------- FTP传输 -------------------- #
    def ftp_connect(self, host, user, password, port=21):
        """连接 FTP 服务器"""
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(user, password)
        return self

    def ftp_upload(self, remote_path):
        """上传到 FTP"""
        with open(self._path, 'rb') as f:
            self.ftp.storbinary(f'STOR {remote_path}', f)
        return self.__class__(remote_path)

    def ftp_download(self, remote_path, local_path=None):
        """从 FTP 下载"""
        local_path = local_path or self._path
        with open(local_path, 'wb') as f:
            self.ftp.retrbinary(f'RETR {remote_path}', f.write)
        return self.__class__(local_path)
    
    def ftp_mirror(self, remote_dir, delete_extra=False):
        """镜像同步目录到FTP"""
        existing_files = set()
        self.ftp.cwd(remote_dir)
        
        # 上传新文件
        for local_file in self.glob('**/*'):
            if local_file.is_file():
                rel_path = os.path.relpath(local_file._path, self._path)
                remote_path = os.path.join(remote_dir, rel_path)
                local_file.ftp_upload(remote_path)
                existing_files.add(remote_path)
        
        # 删除多余文件
        if delete_extra:
            ftp_files = []
            self.ftp.retrlines('LIST', ftp_files.append)
            for line in ftp_files:
                filename = line.split()[-1]
                if filename not in existing_files:
                    self.ftp.delete(filename)
        return self
    # ------------------- SFTP 传输 ------------------- #
    def sftp_connect(self, host, user, password=None, key_path=None, port=22):
        """连接 SFTP 服务器"""
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        if key_path:
            key = paramiko.RSAKey.from_private_key_file(key_path)
            self.ssh.connect(host, port, user, pkey=key)
        else:
            self.ssh.connect(host, port, user, password)
        
        self.sftp = self.ssh.open_sftp()
        return self

    def sftp_upload(self, remote_path):
        """上传到 SFTP"""
        self.sftp.put(self._path, remote_path)
        return self.__class__(remote_path)

    def sftp_download(self, remote_path, local_path=None):
        """从 SFTP 下载"""
        local_path = local_path or self._path
        self.sftp.get(remote_path, local_path)
        return self.__class__(local_path)

    def sftp_sync_dir(self, remote_dir):
        """同步目录到远程"""
        for root, dirs, files in os.walk(self._path):
            rel_path = os.path.relpath(root, self._path)
            remote_root = os.path.join(remote_dir, rel_path)
            
            try:
                self.sftp.mkdir(remote_root)
            except IOError:
                pass
            
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(remote_root, file)
                self.__class__(local_file).sftp_upload(remote_file)
        return self
    
    def sftp_exec_command(self, command):
        """在远程执行命令"""
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return {
            'exit_code': stdout.channel.recv_exit_status(),
            'stdout': stdout.read().decode(),
            'stderr': stderr.read().decode()
        }

    def sftp_mirror(self, remote_dir, preserve_permissions=True):
        """镜像目录到SFTP（保留权限）"""
        for root, dirs, files in self.walk():
            rel_path = os.path.relpath(root._path, self._path)
            remote_root = os.path.join(remote_dir, rel_path)
            
            try:
                self.sftp.mkdir(remote_root)
            except IOError:
                pass
            
            # 同步文件权限
            if preserve_permissions:
                stat = os.stat(root._path)
                self.sftp.chmod(remote_root, stat.st_mode)
            
            for file in files:
                local_path = root / file
                remote_path = os.path.join(remote_root, file)
                local_path.sftp_upload(remote_path)
                
                if preserve_permissions:
                    file_stat = os.stat(local_path._path)
                    self.sftp.chmod(remote_path, file_stat.st_mode)
        return self
    # ------------------ 文件监控模块 ------------------ #
    class PathEventHandler(FileSystemEventHandler):
        def __init__(self, callback):
            self.callback = callback
        
        def on_any_event(self, event):
            self.callback(event)

    def watch(self, callback, recursive=True):
        """监控文件变化"""
        self.observer = Observer()
        event_handler = PathEventHandler(callback)
        self.observer.schedule(
            event_handler,
            str(self),
            recursive=recursive
        )
        self.observer.start()
        return self.observer

    def watch_changes(self, event_types=['modified'], callback=None):
        """过滤特定事件类型的监控"""
        def filtered_callback(event):
            if event.event_type in event_types:
                callback(self.__class__(event.src_path))
        return self.watch(filtered_callback)
    # ------------------ 高级权限管理 ------------------- #
    def set_acl(self, user, permissions, recursive=False):
        """设置 ACL 权限（Unix）"""
        cmd = ['setfacl', '-m', f'u:{user}:{permissions}', self._path]
        subprocess.run(cmd, check=True)
        
        if recursive and self.is_dir():
            for p in self.glob('**/*'):
                p.set_acl(user, permissions)
        return self

    def get_acl(self):
        """获取 ACL 权限（Unix）"""
        result = subprocess.run(
            ['getfacl', self._path],
            capture_output=True,
            text=True
        )
        return result.stdout

    def take_ownership(self, recursive=False):
        """获取文件所有权（Windows）"""
        if sys.platform == 'win32':
            import win32security
            import ntsecuritycon
            
            sd = win32security.GetFileSecurity(
                self._path,
                win32security.OWNER_SECURITY_INFORMATION
            )
            owner = win32security.LookupAccountName(
                None, 
                win32security.GetUserNameEx(win32security.NameSamCompatible)
            )[0]
            sd.SetSecurityDescriptorOwner(owner, False)
            
            win32security.SetFileSecurity(
                self._path,
                win32security.OWNER_SECURITY_INFORMATION,
                sd
            )
            
            if recursive:
                for p in self.glob('**/*'):
                    p.take_ownership()
        return self

    def add_inheritance(self, enable=True):
        """启用/禁用权限继承（Windows）"""
        if sys.platform == 'win32':
            import win32security
            sd = win32security.GetFileSecurity(
                self._path,
                win32security.DACL_SECURITY_INFORMATION
            )
            dacl = sd.GetSecurityDescriptorDacl()
            dacl.SetInheritance(enable)
            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(
                self._path,
                win32security.DACL_SECURITY_INFORMATION,
                sd
            )
        return self
    
    def set_immutable(self, enable=True):
        """设置不可变标志（Linux chattr）"""
        if sys.platform != 'linux':
            raise NotImplementedError("Only supported on Linux")
        
        flag = 'i' if enable else '-i'
        subprocess.run(['sudo', 'chattr', flag, self._path], check=True)
        return self

    def clone_permissions(self, reference_path):
        """克隆其他文件的权限"""
        ref_stat = os.stat(reference_path)
        os.chmod(self._path, ref_stat.st_mode)
        
        # Windows ACL克隆
        if sys.platform == 'win32':
            import win32security
            sd = win32security.GetFileSecurity(
                reference_path,
                win32security.DACL_SECURITY_INFORMATION
            )
            win32security.SetFileSecurity(
                self._path,
                win32security.DACL_SECURITY_INFORMATION,
                sd
            )
        return self

    def take_ownership_recursive(self):
        """递归获取所有权（Windows）"""
        if sys.platform == 'win32':
            import subprocess
            subprocess.run(
                ['takeown', '/R', '/F', self._path],
                check=True
            )
            subprocess.run(
                ['icacls', self._path, '/T', '/grant', '*S-1-3-4:F'],
                check=True
            )
        return self
    # ------------------ 高级文件监控 ------------------ #
    def watch_pattern(self, patterns, callback, recursive=True):
        """模式化监控（*.log等）"""
        class PatternHandler(PatternMatchingEventHandler):
            def __init__(self, callback):
                super().__init__(patterns=patterns)
                self.callback = callback
            
            def on_any_event(self, event):
                self.callback(event)
        
        observer = Observer()
        observer.schedule(
            PatternHandler(callback),
            str(self),
            recursive=recursive
        )
        observer.start()
        return observer

    def debounce_watch(self, callback, delay=1.0):
        """防抖监控（避免重复触发）"""
        from threading import Timer
        last_event = None
        timer = None
        
        def debounced_callback(event):
            nonlocal last_event, timer
            last_event = event
            if timer:
                timer.cancel()
            timer = Timer(delay, lambda: callback(last_event))
            timer.start()
        
        return self.watch(debounced_callback)
    # ------------------ 虚拟文件系统 ------------------ #
    def mount_zip(self, mount_point):
        """将ZIP文件挂载为虚拟目录（Linux）"""
        if sys.platform == 'linux':
            subprocess.run(
                ['fuse-zip', self._path, mount_point],
                check=True
            )
        return self.__class__(mount_point)

    def create_loopback(self, size_mb=100):
        """创建环回设备（Linux）"""
        if sys.platform != 'linux':
            raise NotImplementedError
        
        self.truncate(size_mb * 1024 * 1024)
        losetup_cmd = ['losetup', '--find', '--show', self._path]
        loop_dev = subprocess.check_output(losetup_cmd).decode().strip()
        return self.__class__(loop_dev)
    # ------------------ 其他高级方法 ------------------ #
    def checksum(self, algorithm='sha256'):
        """计算文件校验和"""
        hash_obj = hashlib.new(algorithm)
        with open(self._path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    
    def create_hardlink_here(self, target):
        """在当前目录创建硬链接"""
        link_name = self / target.name
        os.link(target._path, link_name._path)
        return link_name

    def sparse_copy(self, dst):
        """稀疏文件感知复制"""
        if sys.platform == 'win32':
            win32file.CopyFileEx(
                self._path,
                os.fspath(dst),
                win32file.COPY_FILE_SPARSE_FILE
            )
        else:
            with open(self._path, 'rb') as src, open(dst, 'wb') as dst_f:
                while True:
                    data = src.read(4096)
                    if not data:
                        break
                    dst_f.write(data)
                    # 检测稀疏块
                    if all(b == 0 for b in data):
                        dst_f.truncate()
        return self.__class__(dst)

    def create_symlink_tree(self, target_dir):
        """创建符号链接目录树"""
        for root, dirs, files in self.walk():
            rel_path = os.path.relpath(root._path, self._path)
            new_dir = os.path.join(target_dir, rel_path)
            self.__class__(new_dir).mkdir(parents=True, exist_ok=True)
            
            for file in files:
                src = root / file
                dst = self.__class__(new_dir) / file
                dst.symlink_to(src)
        return self.__class__(target_dir)

    def lock_file(self):
        """文件锁（跨平台）"""
        if sys.platform == 'win32':
            import msvcrt
            self._lock_handle = open(self._path, 'a')
            msvcrt.locking(self._lock_handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            self._lock_handle = open(self._path, 'a')
            fcntl.flock(self._lock_handle, fcntl.LOCK_EX)
        return self

    def unlock_file(self):
        """释放文件锁"""
        if hasattr(self, '_lock_handle'):
            if sys.platform == 'win32':
                import msvcrt
                msvcrt.locking(self._lock_handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(self._lock_handle, fcntl.LOCK_UN)
            self._lock_handle.close()
        return self

    def mount(self, target, fs_type=None, options=''):
        """挂载文件系统（Linux）"""
        if sys.platform.startswith('linux'):
            cmd = ['mount']
            if fs_type:
                cmd += ['-t', fs_type]
            if options:
                cmd += ['-o', options]
            cmd += [self._path, target]
            subprocess.run(cmd, check=True)
        return self

    def create_sparse_file(self, size):
        """创建稀疏文件"""
        with open(self._path, 'wb') as f:
            f.truncate(size)
        return self

    def create_symlink_here(self, target):
        """在当前目录创建符号链接"""
        link_name = self.joinpath(target.name)
        link_name.symlink_to(target)
        return link_name

    def get_mime_type(self):
        """获取 MIME 类型"""
        return mimetypes.guess_type(self._path)[0]

    def virus_scan(self, scanner_path='/usr/bin/clamscan'):
        """病毒扫描"""
        result = subprocess.run(
            [scanner_path, '--infected', '-', self._path],
            capture_output=True,
            text=True
        )
        return 'Infected files: 0' not in result.stdout

    def create_diff(self, other, output):
        """生成文件差异"""
        with open(self._path) as f1, open(other) as f2:
            diff = difflib.unified_diff(
                f1.readlines(),
                f2.readlines(),
                fromfile=self.name,
                tofile=other.name
            )
            output.write_text(''.join(diff))
        return output
    
    def add_to_startup(self, shortcut_name="MyApp"):
        """添加到系统启动项（Windows）"""
        if sys.platform == 'win32':
            startup = winshell.startup()
            shortcut = os.path.join(startup, f"{shortcut_name}.lnk")
            
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut)
            shortcut.Targetpath = self._path
            shortcut.save()
        else:
            autostart_dir = Path('~/.config/autostart').expanduser()
            desktop_file = autostart_dir / f"{shortcut_name}.desktop"
            desktop_file.write_text(
                f"[Desktop Entry]\nType=Application\nExec={self._path}"
            )
        return self

    def desktop():
        """获取桌面位置(Desktop)"""
        return os.path.join(os.path.expanduser("~"), "Desktop")

    def create_desktop_shortcut(self, shortcut_name):
        """创建桌面快捷方式"""
        def desktop():
            """获取桌面位置(Desktop)"""
            return os.path.join(os.path.expanduser("~"), "Desktop")
        if sys.platform == 'win32':
            shortcut = os.path.join(desktop(), f"{shortcut_name}.lnk")
            
            import pythoncom
            from win32com.client import Dispatch
            shell = Dispatch('WScript.Shell', pythoncom.CoInitialize())
            shortcut = shell.CreateShortCut(shortcut)
            shortcut.TargetPath = self._path
            shortcut.save()
        else:
            desktop_dir = Path('~/Desktop').expanduser()
            desktop_file = desktop_dir / f"{shortcut_name}.desktop"
            desktop_file.write_text(
                f"[Desktop Entry]\nType=Application\nExec={self._path}"
            )
        return self
    # ------------------- 加密与安全 ------------------- #
    def encrypt_file(self, key, algorithm='aes256'):
        """加密文件（使用pycryptodome）"""
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_path = self.with_suffix('.enc')
        
        with open(self._path, 'rb') as f_in, open(encrypted_path._path, 'wb') as f_out:
            f_out.write(cipher.iv)
            while chunk := f_in.read(4096):
                f_out.write(cipher.encrypt(pad(chunk, AES.block_size)))
        
        return encrypted_path

    def decrypt_file(self, key, output_path=None):
        """解密文件"""
        output_path = output_path or self.with_suffix('.decrypted')
        
        with open(self._path, 'rb') as f_in, open(output_path._path, 'wb') as f_out:
            iv = f_in.read(16)
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            while chunk := f_in.read(4096):
                decrypted = cipher.decrypt(chunk)
                if f_in.tell() == os.path.getsize(self._path):
                    decrypted = unpad(decrypted, AES.block_size)
                f_out.write(decrypted)
        
        return output_path

    def sign_file(self, private_key):
        """数字签名文件"""
        key = RSA.import_key(private_key)
        h = SHA256.new(self.read_bytes())
        signature = pkcs1_15.new(key).sign(h)
        
        sig_file = self.with_suffix('.sig')
        sig_file.write_bytes(signature)
        return sig_file
    # ------------------- 装饰器方法 ------------------- #
    @classmethod
    def _check_exists(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.exists():
                raise FileNotFoundError(f"Path not found: {self}")
            return func(self, *args, **kwargs)
        return wrapper
    
    @classmethod
    def _check_file(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.is_file():
                raise IsADirectoryError(f"Not a file: {self}")
            return func(self, *args, **kwargs)
        return wrapper
    
    @classmethod
    def _check_dir(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.is_dir():
                raise NotADirectoryError(f"Not a directory: {self}")
            return func(self, *args, **kwargs)
        return wrapper
    
    def expandvars(self):
        """展开环境变量"""
        return self.__class__(os.path.expandvars(self._path))
    
    def expanduser(self):
        """展开用户目录"""
        return self.__class__(os.path.expanduser(self._path))
    
    def ensure_parent(self):
        """确保父目录存在"""
        self.parent.mkdir(parents=True, exist_ok=True)
        return self
    
    def backup(self, suffix='.bak'):
        """创建备份文件"""
        backup_path = self.with_suffix(suffix)
        if isinstance(backup_path, Path):  # 关键类型检查
            backup_path = str(backup_path)
        if os.path.exists(backup_path):
            self.__class__(backup_path).backup(suffix)
        return self.copy(backup_path)
    
    def sync_to(self, dst):
        """同步到目标路径（目录）"""
        dst = self.__class__(dst)
        if self.is_file():
            return self.copy(dst/self.name, overwrite=True)
        elif self.is_dir():
            for item in self.iterdir():
                item.sync_to(dst/self.name)
        return dst
    
    def is_world_writable(self):
        """检查全局可写权限（Unix）"""
        if sys.platform == 'win32':
            return False
        mode = os.stat(self._path).st_mode
        return bool(mode & stat.S_IWOTH)

    def is_safe_path(self):
        """检查路径是否安全（不在系统敏感目录）"""
        safe_dirs = [
            os.path.expanduser('~'),
            '/tmp',
            os.getcwd()
        ]
        abs_path = os.path.abspath(self._path)
        return any(abs_path.startswith(d) for d in safe_dirs)

    def is_executable(self):
        """检查是否是可执行文件"""
        if sys.platform == 'win32':
            return self.suffix.lower() in ('.exe', '.bat', '.cmd')
        return os.access(self._path, os.X_OK)

    def unlink(self, missing_ok=False):
        """删除文件"""
        try:
            os.unlink(self._path)
        except FileNotFoundError:
            if not missing_ok:
                raise
        return self

    def is_hidden(self):
        """检查是否是隐藏文件"""
        name = self.name
        if sys.platform == 'win32':
            return self._has_hidden_attribute()
        return name.startswith('.')
    
    def _has_hidden_attribute(self):
        """Windows系统检查隐藏属性"""
        if sys.platform != 'win32':
            return False
        
        try:
            import ctypes
            attrs = ctypes.windll.kernel32.GetFileAttributesW(self._path)
            return attrs & 2  # FILE_ATTRIBUTE_HIDDEN
        except (ImportError, AttributeError):
            # 回退方案
            try:
                return bool(os.stat(self._path).st_file_attributes & 2)
            except AttributeError:
                return self.name.startswith('.')

    def secure_delete(self, passes=3):
        """安全擦除文件内容"""
        with open(self._path, 'ba+') as f:
            length = f.tell()
            for _ in range(passes):
                f.seek(0)
                f.write(os.urandom(length))
            f.truncate(0)
        self.unlink()
        return self

    def sign_with_hmac(self, secret_key, algorithm='sha256'):
        """使用HMAC签名"""
        hmac_obj = hmac.new(secret_key, digestmod=algorithm)
        with open(self._path, 'rb') as f:
            while chunk := f.read(8192):
                hmac_obj.update(chunk)
        return hmac_obj.hexdigest()

    def verify_hmac(self, signature, secret_key, algorithm='sha256'):
        """验证HMAC签名"""
        return hmac.compare_digest(
            self.sign_with_hmac(secret_key, algorithm),
            signature
        )
    
    def md5_checksum(self):
        """计算MD5校验和"""
        return self._calculate_hash('md5')

    def sha256_checksum(self):
        """计算SHA256校验和"""
        return self._calculate_hash('sha256')
    
    def sha512_checksum(self):
        """计算SHA512校验和"""
        return self._calculate_hash("sha512")
    
    def sha1_checksum(self):
        """计算SHA1校验和"""
        return self._calculate_hash("sha1")
    
    def sha224_checksum(self):
        """计算SHA224校验和"""
        return self._calculate_hash("sha224")
    
    def sha384_checksum(self):
        """计算SHA384校验和"""
        return self._calculate_hash("sha384")

    def _calculate_hash(self, algorithm):
        hasher = hashlib.new(algorithm)
        with open(self._path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def truncate(self, size=0):
        """截断文件"""
        with open(self._path, 'w') as f:
            f.truncate(size)
        return self
    
    def is_empty(self):
        """检查是否为空（文件或目录）"""
        if self.is_file():
            return self.size() == 0
        return len(os.listdir(self._path)) == 0
    
    def same_as(self, other):
        """判断是否为同一文件（inode相同）"""
        return os.path.samefile(self._path, str(other))
    
    def find_duplicates(self, algorithm='md5'):
        """查找重复文件"""
        hashes = {}
        for file in self.rglob('*'):
            if file.is_file():
                file_hash = file.hash(algorithm)
                hashes.setdefault(file_hash, []).append(file)
        return [files for files in hashes.values() if len(files) > 1]
    
    def versioned(self, format='_{counter}'):
        """生成带版本号的文件名"""
        counter = 1
        while True:
            new_path = self.parent / f"{self.stem}{format.format(counter=counter)}{self.suffix}"
            if not new_path.exists():
                return new_path
            counter += 1
    
    def with_stem(self, stem):
        """修改文件名（不含后缀）"""
        return self.with_name(stem + self.suffix)
    
    def joinpath(self, *parts):
        """拼接多个路径组件"""
        return self.__class__(os.path.join(self._path, *parts))
    
    def split(self):
        """分解为 (父目录, 文件名)"""
        return self.parent, self.name
    
    def match(self, pattern):
        """通配符匹配"""
        return fnmatch.fnmatch(self.name, pattern)
    
    def contains(self, item):
        """判断是否包含子路径"""
        try:
            self.relative_to(item)
            return True
        except ValueError:
            return False
        
    def shred(self, passes=7):
        """军用级文件粉碎（Gutmann算法）"""
        patterns = [
            b'\x55\x55\x55\x55',  # 0x55
            b'\xAA\xAA\xAA\xAA',  # 0xAA
            b'\x92\x49\x24\x92',  # 随机
            b'\x49\x24\x92\x49',
            b'\x24\x92\x49\x24',
            b'\x00\x00\x00\x00',
            b'\x11\x11\x11\x11',
            b'\x22\x22\x22\x22',
            b'\x33\x33\x33\x33',
            b'\x44\x44\x44\x44',
            b'\x55\x55\x55\x55',
            b'\x66\x66\x66\x66',
            b'\x77\x77\x77\x77',
            b'\x88\x88\x88\x88',
            b'\x99\x99\x99\x99',
            b'\xAA\xAA\xAA\xAA',
            b'\xBB\xBB\xBB\xBB',
            b'\xCC\xCC\xCC\xCC',
            b'\xDD\xDD\xDD\xDD',
            b'\xEE\xEE\xEE\xEE',
            b'\xFF\xFF\xFF\xFF',
            os.urandom(4)
        ]
        
        with open(self._path, 'r+b') as f:
            length = f.tell()
            for i in range(passes):
                f.seek(0)
                if i < len(patterns):
                    pattern = patterns[i]
                else:
                    pattern = os.urandom(4)
                f.write(pattern * (length // len(pattern) + 1))
            f.truncate(0)
        self.unlink()
        return self

    def zero_fill(self):
        """用零填充文件空间"""
        with open(self._path, 'r+b') as f:
            length = f.tell()
            f.seek(0)
            f.write(b'\x00' * length)
        return self
    
    def set_sticky_bit(self):
        """设置粘滞位（Unix）"""
        if sys.platform != 'win32':
            mode = os.stat(self._path).st_mode
            os.chmod(self._path, mode | stat.S_ISVTX)
        return self

    def disable_execute(self):
        """禁用执行权限（所有用户）"""
        if sys.platform == 'win32':
            return self  # Windows无执行位概念
        os.chmod(self._path, os.stat(self._path).st_mode & ~0o111)
        return self
    
    def verify_integrity(self, original_hash, algorithm='sha256'):
        """验证文件完整性"""
        return self._calculate_hash(algorithm) == original_hash

    def compare_content(self, other_path):
        """二进制对比文件内容"""
        with open(self._path, 'rb') as f1, open(other_path, 'rb') as f2:
            while True:
                b1 = f1.read(4096)
                b2 = f2.read(4096)
                if b1 != b2:
                    return False
                if not b1:
                    return True

    def set_creation_date(self, timestamp):
        """设置创建时间戳（Windows）"""
        if sys.platform == 'win32':
            import pywintypes
            import win32file
            handle = win32file.CreateFile(
                self._path,
                win32file.GENERIC_WRITE,
                0, None, win32file.OPEN_EXISTING,
                0, None
            )
            win32file.SetFileTime(
                handle,
                pywintypes.Time(timestamp),
                None, None
            )
            handle.Close()
        return self

    def exit(code):
        """
        Exit  (SystemExit)
        ~~~~~~~~~~~~~~~~~~~~~~
        :param code: 退出返回值
        """
        raise SystemExit(code)

    def attributes(file_path, hidden=False, readonly=False, archive=False, compressed=False):
        """
        设置指定文件的属性为隐藏、只读、存档、系统或压缩
        :param file_path: 文件路径
        :param hidden: 是否设置为隐藏，默认为False
        :param readonly: 是否设置为只读，默认为False
        :param archive: 是否设置为存档，默认为False
        :param compressed: 是否设置为压缩，默认为False
        """
        def exit(code):
            """
            Exit  (SystemExit)
            ~~~~~~~~~~~~~~~~~~~~~~
            :param code: 退出返回值
            """
            raise SystemExit(code)
        
        if os.name == 'nt':
            if os.path.exists(file_path):
                attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
                if hidden:
                    attributes |= FILE_ATTRIBUTE_HIDDEN
                else:
                    attributes &= ~FILE_ATTRIBUTE_HIDDEN
                if readonly:
                    attributes |= FILE_ATTRIBUTE_READONLY
                else:
                    attributes &= ~FILE_ATTRIBUTE_READONLY
                if archive:
                    attributes |= FILE_ATTRIBUTE_ARCHIVE
                else:
                    attributes &= ~FILE_ATTRIBUTE_ARCHIVE
                if compressed:
                    attributes |= FILE_ATTRIBUTE_COMPRESSED
                else:
                    attributes &= ~FILE_ATTRIBUTE_COMPRESSED
                ctypes.windll.kernel32.SetFileAttributesW(file_path, attributes)
            else:
                print(f'文件路径没有检测到文件: {file_path}')
                exit(1)
        else:
            print('attributes: 此功能只支持Windows系统! ')
            exit(1)

    def to_posix(self):
        """转换为POSIX风格路径"""
        return self.__class__(self._path.replace(os.sep, '/'))
    
    def to_nt(self):
        """转换为Windows风格路径"""
        return self.__class__(self._path.replace('/', '\\'))
    
    def touch_dir(self):
        """更新目录时间戳"""
        os.utime(self._path, None)
        return self
    
    def listdir(self, pattern='*'):
        """列出目录内容"""
        return [self.joinpath(name) for name in os.listdir(self._path) if fnmatch.fnmatch(name, pattern)]
    
    def iterdir(self):
        """生成目录迭代器"""
        for name in os.listdir(self._path):
            yield self.joinpath(name)
    
    @classmethod
    def cwd(cls):
        """当前工作目录"""
        return cls(os.getcwd())
    
    @classmethod
    def home(cls):
        """用户主目录"""
        return cls(os.path.expanduser('~'))
    
    # ------------------- 魔法方法增强 ------------------- #
    def __contains__(self, item):
        return self.contains(item)
    
    def __lt__(self, other):
        return self._path < str(other)
    
    def __gt__(self, other):
        return self._path > str(other)
    
    def __len__(self):
        return len(self._path)
    
    def __bool__(self):
        return bool(self._path)

__all__ = ["Path","PathEventHandler"]