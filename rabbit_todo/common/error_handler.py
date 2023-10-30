"""
ErrorHandler
"""

from __future__ import annotations

# --- Third Party Library ---
from colorama import Fore


def error_prefix() -> str:
    """Return error-prefix"""
    return Fore.RED + "ERROR" + Fore.RESET + ": "


ERROR_MESSAGES = {"0": "Task file was corrupted.", "1": "Task not found. Please try again."}

FILE_CORRUPTED_ERROR_CODE = "0"
TASK_NOT_FOUND_ERROR_CODE = "1"


class RabbitTodoException(Exception):
    """The Exception to Rabbit Todo Application"""

    def __init__(self, code: str, rabbit_exception: RabbitTodoException | None = None) -> None:
        self._code = code + ";"
        if rabbit_exception is not None:
            self._code += rabbit_exception.code

    @property
    def code(self) -> str:
        """Return error code"""
        return self._code + ";"


class ErrorHandler:
    """Handle RabbitTodoException"""

    def __init__(self, exc: RabbitTodoException) -> None:
        self._exc = exc

    def get_message(self) -> str:
        """Return error-message with error-prefix"""
        message = self._parse_exception()
        return error_prefix() + message

    def _parse_exception(self) -> str:
        """Parse RabbitTodoException"""
        error_codes = self._exc.code.split(";")
        return ERROR_MESSAGES.get(error_codes[0], "")
