"""
Tubiu
~~~~~~~


BaseException
|
├── BaseExceptionGroup
│   └── ExceptionGroup
├── Exception
│   ├── ArithmeticError
│   │   ├── FloatingPointError
│   │   ├── OverflowError
│   │   └── ZeroDivisionError
│   ├── AssertionError
│   ├── AttributeError
│   ├── BufferError
│   ├── EOFError
│   ├── ImportError
│   │   ├── ModuleNotFoundError
│   │   └── ZipImportError
│   ├── LookupError
│   │   ├── IndexError
│   │   ├── KeyError
│   │   └── CodecRegistryError
│   ├── MemoryError
│   ├── NameError
│   │   └── UnboundLocalError
│   ├── OSError
│   │   ├── BlockingIOError
│   │   ├── ChildProcessError
│   │   ├── ConnectionError
│   │   │   ├── BrokenPipeError
│   │   │   ├── ConnectionAbortedError
│   │   │   ├── ConnectionRefusedError
│   │   │   └── ConnectionResetError
│   │   ├── FileExistsError
│   │   ├── FileNotFoundError
│   │   ├── InterruptedError
│   │   ├── IsADirectoryError
│   │   ├── NotADirectoryError
│   │   ├── PermissionError
│   │   ├── ProcessLookupError
│   │   ├── TimeoutError
│   │   ├── UnsupportedOperation
│   │   ├── Error
│   │   │   └── SameFileError
│   │   ├── SpecialFileError
│   │   ├── ExecError
│   │   └── ReadError
│   ├── ReferenceError
│   ├── RuntimeError
│   │   ├── NotImplementedError
│   │   ├── RecursionError
│   │   └── _DeadlockError
│   ├── StopAsyncIteration
│   ├── StopIteration
│   ├── SyntaxError
│   │   └── IndentationError
│   │       └── TabError
│   ├── SystemError
│   │   └── CodecRegistryError
│   ├── TypeError
│   ├── ValueError
│   │   ├── UnicodeError
│   │   │   ├── UnicodeDecodeError
│   │   │   ├── UnicodeEncodeError
│   │   │   └── UnicodeTranslateError
│   │   └── UnsupportedOperation
│   ├── Warning
│   │   ├── BytesWarning
│   │   ├── DeprecationWarning
│   │   ├── EncodingWarning
│   │   ├── FutureWarning
│   │   ├── ImportWarning
│   │   ├── PendingDeprecationWarning
│   │   ├── ResourceWarning
│   │   ├── RuntimeWarning
│   │   ├── SyntaxWarning
│   │   ├── UnicodeWarning
│   │   └── UserWarning
│   ├── ExceptionGroup
│   ├── _OptionError
│   ├── error
│   ├── ArgumentError
│   ├── ArgumentTypeError
│   ├── Error
│   ├── error
│   ├── LZMAError
│   ├── RegistryError
│   └── _GiveupOnFastCopy
├── GeneratorExit
├── KeyboardInterrupt
└── SystemExit
"""
#Copyright (c) 2025, <363766687@qq.com>
#Author: Huang Yiyi

from _Tcode import Path
from __TUBIU__ import *
import __TUBIU__

#with Restrain(TubiuWarning):

true = True
false = False

__tubiu__ = __TUBIU__
__version__ = "0.0.1"
__name__ = "tubiu"
__TUBIU__.__check__()