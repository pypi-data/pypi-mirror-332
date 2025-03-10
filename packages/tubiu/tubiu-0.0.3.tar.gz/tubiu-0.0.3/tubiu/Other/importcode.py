#Copyright (c) 2025, <363766687@qq.com>
#Author: Huang Yiyi

import os
import shutil
import stat
import fnmatch
import tempfile
import hashlib
from datetime import datetime
from functools import wraps
from ftplib import FTP
import paramiko
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
from watchdog.events import PatternMatchingEventHandler
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import winshell
from win32com.client import Dispatch
import difflib
import subprocess
import mimetypes
import win32file
import hmac
import win32api
import win32con
import ctypes

try:
    from cryptography import x509 as x509
    from cryptography.x509.oid import NameOID as NameOID
    from cryptography.hazmat.primitives import hashes as hashes
    from cryptography.hazmat.primitives.asymmetric import rsa as rsa
    from cryptography.hazmat.primitives import serialization as serialization
except ImportError:
    x509 = None

import datetime as datetime
FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_READONLY = 0x1
FILE_ATTRIBUTE_ARCHIVE = 0x20
FILE_ATTRIBUTE_SYSTEM = 0x4
FILE_ATTRIBUTE_COMPRESSED = 0x800
from builtins import print as output
if __name__  == "__main__":
    print("Code 运行成功(🐏)")