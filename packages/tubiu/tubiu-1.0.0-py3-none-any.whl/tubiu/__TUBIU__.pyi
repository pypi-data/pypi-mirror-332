# Copyright (c) 2025, <363766687@qq.com>
# Author: Huang Yiyi

import sys
from typing import Optional, Dict, TextIO
from Other import CommunicationResult
from typing import Union
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    try:
        from tubiu import TubiuError
    except ImportError:
        class TubiuError(Exception): ...


# Custom exception class for handling errors related to print operations
class TubiuError(Exception):
    """
    Custom exception class for print operations.
    """
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        """
        Initialize the TubiuError exception.
        :param message: The error message.
        :param original_error: The original exception object (optional).
        """
        ...

__TubiuError__ = TubiuError

# Custom class to automatically detect the system type and return the corresponding operating system name
class platform(str):
    """
    Automatically detects your system and
    returns: the operating system of the PC
    you are using.
    """
      
    def __new__(cls) -> 'platform':
        """
        Create an instance of the platform class and automatically detect the current system type.
        :return: An instance of the platform class representing the current system type.
        """
        ...

# Custom class for managing system or environment variables
class PATH:
    """
    About system or environment variables.
    Examples:
        path_manager = PATH()

        # Get the PATH list
        print("Current PATH list:", path_manager.get_environment_vars())

        # Get all system variables as a dictionary
        system_vars = path_manager.get_system_vars()
        print("Examples of system variables:", list(system_vars.keys())[:3])

        # Add a new path to PATH
        path_manager.add_to_environment("/usr/local/custom_bin")
        print("Updated PATH:", path_manager.get_environment_vars()[-1])

        # Set a new environment variable
        path_manager.set_variable("MY_APP_CONFIG", "/etc/myapp/config.ini")
        print("Value of MY_APP_CONFIG:", os.environ.get("MY_APP_CONFIG"))

    Note: Persistence operations involve system
    permissions and security, and should be used
    with caution!
    """
      
    def __init__(self):
        """
        Initialize an instance of the PATH class and determine the path separator.
        """
        ...

    def get_environment_vars(self) -> list[str]:
        """
        Get the current environment variable PATH as a list.
        :return: A list obtained by splitting the PATH environment variable.
        """
        ...

    def get_system_vars(self) -> dict[str, str]:
        """
        Get all system environment variables in dictionary form.
        :return: A dictionary containing all system environment variables.
        """
        ...

    def update_environment_vars(self, new_path_list: list[str]) -> None:
        """
        Update the environment variable PATH.
        :param new_path_list: The new list of paths.
        """
        ...

    def add_to_environment(self, path: str) -> None:
        """
        Add a new path to the environment variable PATH (automatically remove duplicates).
        :param path: The new path to be added.
        """
        ...

    def set_variable(self, name: str, value: str) -> None:
        """
        Set or update a system environment variable (in key-value pair form).
        :param name: The name of the environment variable.
        :param value: The value of the environment variable.
        """
        ...

    def remove_variable(self, name: str) -> None:
        """
        Delete a system environment variable.
        :param name: The name of the environment variable to be deleted.
        """
        ...

    def save_to_system(self) -> None:
        """
        Persist the environment variables to the system (requires administrator privileges).
        """
        ...

    def _save_windows(self) -> None:
        """
        Save environment variables to the registry on Windows systems.
        """
        ...

    def _save_linux(self) -> None:
        """
        Save environment variables to the ~/.bashrc file on Linux systems.
        """
        ...

    def _save_macos(self) -> None:
        """
        Save environment variables to the ~/.zshrc file on macOS systems.
        """
        ...

# Custom class for exiting the Python interpreter
class Exit:
    """
    Exit
    ~~~~
    Close the Python interpreter, but the code that
    follows the class will no longer work.
    """
      
    def __init__(self, code: int = 0):
        """
        Initialize an instance of the Exit class and exit the Python interpreter.
        :param code: The exit code, default is 0.
        """
        ...

# Custom class for managing Windows services
class Serve:
    """
    Serve
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    About Windows services.
    """
      
    def __init__(self):
        """
        Initialize an instance of the Serve class, check if the pywin32 library is installed, and ensure the current system is Windows.
        """
        ...

    def _handle_win_error(self, action: str, error: Exception) -> None:
        """
        Handle Windows API errors uniformly.
        :param action: A description of the operation.
        :param error: The exception that occurred.
        """
        ...

      
    def get_service_status(self, service_name: str) -> str:
        """
        Get the status of a specified service.
        :param service_name: The name of the service.
        :return: A description of the service's status.
        """
        ...

      
    def start_service(self, service_name: str, timeout: int = 30) -> None:
        """
        Start a specified service.
        :param service_name: The name of the service.
        :param timeout: The timeout for waiting for the service to start, default is 30 seconds.
        """
        ...

      
    def stop_service(self, service_name: str, timeout: int = 30) -> None:
        """
        Stop a specified service.
        :param service_name: The name of the service.
        :param timeout: The timeout for waiting for the service to stop, default is 30 seconds.
        """
        ...

      
    def create_service(self, 
                      service_name: str,
                      display_name: str,
                      binary_path: str,
                      start_type: str = 'manual') -> None:
        """
        Create a new Windows service.
        :param service_name: The name of the service.
        :param display_name: The display name of the service.
        :param binary_path: The path to the service's executable file.
        :param start_type: The startup type of the service, default is 'manual'.
        """
        ...

      
    def delete_service(self, service_name: str) -> None:
        """
        Delete a specified Windows service.
        :param service_name: The name of the service.
        """
        ...

      
    def set_startup_type(self, service_name: str, start_type: str) -> None:
        """
        Modify the startup type of a specified service.
        :param service_name: The name of the service.
        :param start_type: The startup type.
        """
        ...

# Custom class for operating the clipboard
class Clipboard:
    """
    Some operations on the clipboard.
    """
      
    def __init__(
        self, 
        content: Optional[str] = None, 
        modify: bool = False, 
        get: bool = False
    ):
        """
        Initialize an instance of the Clipboard class.
        :param content: The content to be saved to the clipboard (only takes effect when modify=True).
        :param modify: Whether to modify the clipboard content.
        :param get: Whether to get the clipboard content (higher priority than modify).
        """
        ...

    def _set_to_clipboard(self) -> None:
        """
        Write content to the clipboard.
        """
        ...

    def _get_from_clipboard(self) -> None:
        """
        Read content from the clipboard.
        """
        ...

    @property
    def content(self) -> str:
        """
        Get the current clipboard content (cached value or read in real-time).
        :return: The clipboard content.
        """
        ...

    @classmethod
      
    def clear(cls) -> None:
        """
        Clear the clipboard.
        """
        ...

    @staticmethod
      
    def is_image_available() -> bool:
        """
        Detect whether there is an image on the clipboard (only supported on Windows/macOS).
        :return: True if there is an image, otherwise False.
        """
        ...

    @classmethod
      
    def get_image(cls) -> bytes:
        """
        Get the image on the clipboard (Windows/macOS).
        :return: The byte data of the image.
        """
        ...

# Custom class for copying files or folders
class Copy:
      
    def __init__(
        self,
        src: str,
        dest_dir: str,
        safe_copy: bool = False,
        overwrite: bool = False
    ):
        """
        Initialize an instance of the Copy class for copying files or folders.
        :param src: The path of the source file or folder.
        :param dest_dir: The parent directory of the destination.
        :param safe_copy: Whether to enable security checks (file-level checks).
        :param overwrite: Whether to overwrite an existing destination.
        """
        ...

    def _validate(self) -> None:
        """
        Validate the validity of the source and destination paths.
        """
        ...

    def _get_dest_path(self) -> str:
        """
        Generate the complete destination path.
        :return: The complete destination path.
        """
        ...

    def _prepare_destination(self, dest_path: str) -> None:
        """
        Handle the overwrite logic. If the destination exists and overwrite is allowed, delete it; otherwise, raise an exception.
        :param dest_path: The destination path.
        """
        ...

    def _copy_file(self, src: str, dest: str) -> None:
        """
        Copy a single file.
        :param src: The path of the source file.
        :param dest: The path of the destination file.
        """
        ...

    def _copy_dir(self, src: str, dest: str) -> None:
        """
        Recursively copy a folder.
        :param src: The path of the source folder.
        :param dest: The path of the destination folder.
        """
        ...

    def _file_hash(self, path: str) -> str:
        """
        Calculate the hash value of a file.
        :param path: The path of the file.
        :return: The hash value of the file.
        """
        ...

    def _copy(self) -> None:
        """
        The main copy logic. Call the corresponding copy method depending on whether the source is a file or a folder.
        """
        ...

    def __repr__(self) -> str:
        """
        Return the string representation of the object.
        :return: The string representation of the object.
        """
        ...

# Custom class for outputting content
class output:
    """
    print(CMD,POWERSHELL)
    """
      
    def __init__(self, *values, sep: str = " ", 
                 end: str = "\n", file: Optional[TextIO] = None, 
                 flush: bool = False) -> None:
        """
        Initialize an instance of the output class and call the __D__ function to output content.
        :param values: The values to be output.
        :param sep: The separator between values, default is a space.
        :param end: The ending character of the output, default is a newline character.
        :param file: The output stream, default is sys.stdout.
        :param flush: Whether to force flush the output, default is False.
        """
        ...

    def __tubiu__(self, error: Exception) -> None:
        """
        Handle errors that occur during output and raise a TubiuError exception.
        :param error: The exception that occurred.
        """
        ...

# Custom class for enhanced printing with ANSI color support
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
    _STYLES: Dict[str, int]
    _NAMED_COLORS: Dict[str, int]

      
    def __init__(self, *args,
                 color: Optional[str] = None,
                 file: TextIO = sys.stdout,
                 sep: str = " ",
                 end: str = "\n",
                 flush: bool = False):
        """
        Initialize an instance of the print class and set parameters such as output color, stream, and separator.
        :param args: The content to be printed.
        :param color: The color and style specification.
        :param file: The output stream, default is sys.stdout.
        :param sep: The separator between arguments, default is a space.
        :param end: The ending character of the output, default is a newline character.
        :param flush: Whether to force flush the output, default is False.
        """
        ...

    def _enable_ansi(self, file: TextIO) -> None:
        """
        Enable ANSI color support on Windows systems.
        :param file: The output stream.
        """
        ...

    def _parse_color(self, color: Optional[str]) -> bytes:
        """
        Parse the color specification into ANSI codes.
        :param color: The color specification string.
        :return: The parsed ANSI code byte string.
        """
        ...

# Custom class for asynchronously executing external commands
class Popen:
      
    def __init__(self, args, shell: bool = False, stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout, stderr: TextIO = sys.stderr):
        """
        Initialize an instance of the Popen class and start an external process.
        :param args: The command and its arguments to be executed.
        :param shell: Whether to use the shell to execute the command, default is False.
        :param stdin: The standard input stream, default is sys.stdin.
        :param stdout: The standard output stream, default is sys.stdout.
        :param stderr: The standard error stream, default is sys.stderr.
        """
        ...

    def _start_process(self) -> None:
        """
        Start an external process and create threads to read the standard output and standard error.
        """
        ...

    def _read_output(self, stream, data_list) -> None:
        """
        Read output data from the stream and store it in a list.
        :param stream: The input stream.
        :param data_list: The list to store the output data.
        """
        ...

    def communicate(self, input_data: Optional[str] = None) -> CommunicationResult:
        """
        Communicate with the child process, wait for the process to end, and return the output result.
        :param input_data: The input data to be sent to the child process (optional).
        :return: A CommunicationResult object containing the standard output, standard error, and return status.
        """
        ...

    def wait(self) -> int:
        """
        Wait for the child process to end and return its return code.
        :return: The return code of the child process.
        """
        ...

# Custom class for handling file byte encoding operations
class Bytes:
    """
    Handling of bytes encoding.
    """
    def __init__(self, file_path: str, encoding: str = 'utf-8'):
        """
        Initialize a Bytes class instance to read the file and convert its content into byte data.
        :param file_path: The path of the file to be processed.
        :param encoding: The encoding used to read the file, default is 'utf-8'.
        """
        ...

    def _is_binary_file(self) -> bool:
        """
        Simply determine whether the file is a binary file.
        :return: True if it is a binary file, False otherwise.
        """
        ...

    def __str__(self) -> str:
        """
        Return a string representation of the object. If the byte data is available, return its string form; otherwise, return an error message.
        :return: A string representing the byte data or an error message.
        """
        ...

      
    def getbytes(self) -> Optional[bytes]:
        """
        Get the byte encoding data of the file.
        :return: The byte data of the file. If an error occurs during the process, return None.
        """
        ...

      
    def bytestofile(self, output_file_path: str, bytes_content: Optional[bytes] = None) -> None:
        """
        Convert byte encoding data into a file.
        :param output_file_path: The path of the output file.
        :param bytes_content: The byte data to be written to the file. If not provided, use the internal byte data of the instance.
        """
        ...

# Custom class for sending system notifications
class notify:
    """
    This class is used to send system notifications, supporting Windows systems (requires the pywin32 and plyer libraries).
    """
      
    def __init__(self, title: str, message: str, app_name: Optional[str] = None, timeout: int = 5, icon: Optional[str] = None):
        """
        Initialize a notify class instance to send a system notification.
        :param title: The title of the notification.
        :param message: The content of the notification.
        :param app_name: The name of the application sending the notification, optional.
        :param timeout: The display duration of the notification in seconds, default is 5 seconds.
        :param icon: The path to the icon of the notification, optional.
        """
        ...

    def __notify__(self) -> None:
        """
        Send the system notification. If an error occurs during the process, raise a TubiuError exception.
        """
        ...

# Custom class for suppressing specific types of warnings
class Restrain:
    """
    Initialize the Restrain class to specify the type of warning you want to suppress.

    :param warning_type: The type of warning that needs to be suppressed.
    """
      
    def __init__(self, warning_type: type[Warning]):
        """
        Initialize the Restrain class to specify the type of warning to be suppressed.
        :param warning_type: The type of warning to suppress.
        """
        ...

    def __enter__(self) -> 'Restrain':
        """
        Activate warning suppression when entering the context.
        :return: The Restrain instance itself for chained calls.
        """
        ...

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Revert to the original warning settings when exiting the context.
        :param exc_type: The type of the exception (if any) that occurred within the context.
        :param exc_value: The exception object (if any) that occurred within the context.
        :param traceback: The traceback object (if any) that occurred within the context.
        """
        ...

# Custom warning class, inheriting from the built - in Warning class
class TubiuWarning(Warning):
    """
    A custom warning class, used to define specific types of warnings in the application.
    """
    ...

# Custom warning class, indicating that the pywin32 library is not installed
class PyWin32NotInstalledWarning(TubiuWarning):
    """
    A custom warning indicating that the pywin32 library is not installed, which may limit the functionality of some features.
    """
    ...

# Custom warning class, indicating that the plyer library is not installed
class PlyerNotInstalledWarning(TubiuWarning):
    """
    A custom warning indicating that the plyer library is not installed, which may limit the functionality of some features.
    """
    ...

# Function to check if the necessary modules are installed
def __check__() -> bool:
    """
    Check if the necessary modules (such as tubiu and its sub - modules) are installed.
    If not installed, issue a warning and exit the program.
    :return: True if all necessary modules are installed, False otherwise.
    """
    ...

# Function to check if the pywin32 library is installed
def __check_pywin32_installed__() -> bool:
    """
    Check if the pywin32 library is installed. If not installed, issue a warning.
    :return: True if the pywin32 library is installed, False otherwise.
    """
    ...

# Function to check if the plyer library is installed
def __check_plyer_installed__() -> bool:
    """
    Check if the plyer library is installed. If not installed, issue a warning.
    :return: True if the plyer library is installed, False otherwise.
    """
    ...


def pi(numbers: int) -> float:
    """
    Calculate the value of pi with the specified number of decimal places.
    :param numbers: The number of decimal places for the result.
    :return: The value of pi with the specified precision.
    """
    ...

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non - negative integer.
    :param n: The non - negative integer for which to calculate the factorial.
    :return: The factorial of n.
    """
    ...

def sin(x: float, num_terms: int = 10) -> float:
    """
    Calculate the sine function using Taylor series expansion.
    :param x: The input value in radians.
    :param num_terms: The number of terms in the Taylor series expansion, default is 10.
    :return: The approximate value of sin(x).
    """
    ...

def cos(x: float, num_terms: int = 10) -> float:
    """
    Calculate the cosine function using Taylor series expansion.
    :param x: The input value in radians.
    :param num_terms: The number of terms in the Taylor series expansion, default is 10.
    :return: The approximate value of cos(x).
    """
    ...

def tan(x: float, num_terms: int = 10) -> float:
    """
    Calculate the tangent function.
    :param x: The input value in radians.
    :param num_terms: The number of terms in the Taylor series expansion for sin and cos, default is 10.
    :return: The approximate value of tan(x). Returns infinity if cos(x) is 0.
    """
    ...

def cot(x: float, num_terms: int = 10) -> float:
    """
    Calculate the cotangent function.
    :param x: The input value in radians.
    :param num_terms: The number of terms in the Taylor series expansion for tan, default is 10.
    :return: The approximate value of cot(x). Returns infinity if tan(x) is 0.
    """
    ...

class ComplexNumber:
    def __init__(self, real: float, imag: float):
        """
        Initialize a complex number.
        :param real: The real part of the complex number.
        :param imag: The imaginary part of the complex number.
        """
        ...

    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Add two complex numbers.
        :param other: Another complex number to be added.
        :return: The sum of the two complex numbers.
        """
        ...

    def __sub__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Subtract two complex numbers.
        :param other: Another complex number to be subtracted.
        :return: The difference of the two complex numbers.
        """
        ...

    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Multiply two complex numbers.
        :param other: Another complex number to be multiplied.
        :return: The product of the two complex numbers.
        """
        ...

    def __truediv__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """
        Divide two complex numbers.
        :param other: Another complex number to be the divisor.
        :return: The quotient of the two complex numbers.
        """
        ...

    def __str__(self) -> str:
        """
        Return a string representation of the complex number.
        :return: A string in the form of "real + imagi".
        """
        ...

def sqrt(a: float, tolerance: float = 1e-6, max_iterations: int = 100) -> float:
    """
    Calculate the square root of a number using the Newton - Raphson method.
    :param a: The number for which to calculate the square root.
    :param tolerance: The tolerance for convergence, default is 1e - 6.
    :param max_iterations: The maximum number of iterations, default is 100.
    :return: The approximate square root of a.
    """
    ...

def exp(x: float, num_terms: int = 10) -> float:
    """
    Calculate the exponential function using Taylor series expansion.
    :param x: The input value.
    :param num_terms: The number of terms in the Taylor series expansion, default is 10.
    :return: The approximate value of exp(x).
    """
    ...


def ln(x: float, tolerance: float = 1e-6, max_iterations: int = 100) -> Union[float, str]:
    """
    Calculate the natural logarithm of a positive number using the Newton - Raphson method.

    This function attempts to find the natural logarithm of the input `x` by iteratively
    applying the Newton - Raphson algorithm. It starts with an initial guess and refines
    the estimate until the difference between successive approximations is within the
    specified `tolerance` or the maximum number of iterations `max_iterations` is reached.

    :param x: The positive number for which to calculate the natural logarithm.
    :param tolerance: The tolerance for convergence. If the change in the estimate
                      between iterations is less than this value, the algorithm stops.
                      Defaults to 1e-6.
    :param max_iterations: The maximum number of iterations allowed. If the algorithm
                           does not converge within this number of iterations, a
                           `TubiuError` is raised. Defaults to 100.
    :return: The natural logarithm of `x` if the algorithm converges. In case of an
             overflow during the calculation, the string "inf" is returned.
    :raises ValueError: If the input `x` is less than or equal to 0.
    :raises TubiuError: If the algorithm fails to converge within `max_iterations` iterations.
    """
    ...

def power(x: float, n: int) -> float:
    """
    Calculate the power of a number.
    :param x: The base number.
    :param n: The exponent.
    :return: The result of x raised to the power of n.
    """
    ...

def combination(n: int, k: int) -> int:
    """
    Calculate the binomial coefficient C(n, k).
    :param n: The total number of items.
    :param k: The number of items to choose.
    :return: The binomial coefficient C(n, k). Returns 0 if k > n or k < 0.
    """
    ...

def log10(x: float, tolerance: float = 1e-6, max_iterations: int = 100) -> float:
    """
    Calculate the base - 10 logarithm of a number.
    :param x: The input value.
    :param tolerance: The tolerance for convergence, default is 1e - 6.
    :param max_iterations: The maximum number of iterations, default is 100.
    :return: The approximate base - 10 logarithm of x.
    """
    ...

def sinh(x: float, num_terms: int = 10) -> float:
    """
    Calculate the hyperbolic sine function.
    :param x: The input value.
    :param num_terms: The number of terms in the Taylor series expansion for exp, default is 10.
    :return: The approximate value of sinh(x).
    """
    ...

def cosh(x: float, num_terms: int = 10) -> float:
    """
    Calculate the hyperbolic cosine function.
    :param x: The input value.
    :param num_terms: The number of terms in the Taylor series expansion for exp, default is 10.
    :return: The approximate value of cosh(x).
    """
    ...

def tanh(x: float, num_terms: int = 10) -> float:
    """
    Calculate the hyperbolic tangent function.
    :param x: The input value.
    :param num_terms: The number of terms in the Taylor series expansion for sinh and cosh, default is 10.
    :return: The approximate value of tanh(x).
    """
    ...

def floor(x: float) -> int:
    """
    Calculate the floor of a number.
    :param x: The input value.
    :return: The largest integer less than or equal to x.
    """
    ...

def absolute_value(x: float) -> float:
    """
    Calculate the absolute value of a number.
    :param x: The input value.
    :return: The absolute value of x.
    """
    ...

def cmd(command: str) -> int:
    """
    Execute a shell command.
    :param command: The shell command to be executed.
    :return: The return code of the shell command.
    """
    ...

def increase(
    file_extension: Optional[str] = None,
    file_type: Optional[str] = None,
    icon_path: Optional[str] = None,
    associated_program: Optional[str] = None
) -> None:
    """
    Customize file associations.
    :param file_extension: The custom file extension.
    :param file_type: The custom file type name.
    :param icon_path: The path to the icon file. Ensure the icon file exists.
    :param associated_program: The path to the associated program.
    """
    ...

def delete(file_extension: str, file_type: str) -> None:
    """
    Delete file extension associations.
    :param file_extension: The file extension for which to delete the association.
    :param file_type: The file type for which to delete the association.
    """
    ...

def modify(
    old_file_extension: Optional[str] = None,
    old_file_type: Optional[str] = None,
    new_file_extension: Optional[str] = None,
    new_file_type: Optional[str] = None,
    new_icon_path: Optional[str] = None,
    new_associated_program: Optional[str] = None
) -> None:
    """
    Modify file extension associations.
    :param old_file_extension: The old file extension to be modified.
    :param old_file_type: The old file type to be modified.
    :param new_file_extension: The new file extension.
    :param new_file_type: The new file type.
    :param new_icon_path: The new path to the icon file.
    :param new_associated_program: The new path to the associated program.
    """
    ...