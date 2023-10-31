"""
ErrorHandler
"""

# --- Third Party Library ---
from colorama import Fore

# --- First Party Library ---
from rabbit_todo.common.rabbit_error import RabbitTodoError


def error_prefix() -> str:
    """Return error-prefix"""
    return Fore.RED + "ERROR" + Fore.RESET + ": "


def task_file_corrupted_error_message() -> str:
    """Code: 0, Task File Corrupted Error Message"""
    return "Task file was corrupted."


def task_not_found_error_message() -> str:
    """Code: 1, Task Not Found Error Message"""
    return "Task not found."


def unknown_error_message() -> str:
    """Code: None, Unknown Error Message"""
    return "Unknown Error."


def get_error_message(code: str) -> str:
    """Get the error message from code"""
    function_dict = {"0": task_file_corrupted_error_message, "1": task_not_found_error_message}
    message_function = function_dict.get(code, unknown_error_message)
    return message_function()


def get_message_from_exception(exception: RabbitTodoError) -> str:
    """Return error-message with error-prefix"""
    error_codes = exception.code.split(";")
    message = get_error_message(error_codes[0])
    return error_prefix() + message
