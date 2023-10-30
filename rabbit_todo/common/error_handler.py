from __future__ import annotations

# --- Third Party Library ---
from colorama import Fore

ERROR_PREFIX = Fore.RED + "ERROR" + Fore.RESET + ": "
ERROR_MESSAGES = {"0": "Task file was corrupted.", "1": "Task not found. Please try again."}

FILE_CORRUPTED_ERROR_CODE = "0"
TASK_NOT_FOUND_ERROR_CODE = "1"


class RabbitTodoException(Exception):
    def __init__(self, code: str, rabbit_exception: RabbitTodoException = None) -> None:
        self._code = code + ";"
        if rabbit_exception is not None:
            self._code += rabbit_exception.code

    @property
    def code(self) -> str:
        return self._code + ";"


class ErrorHandler:
    def __init__(self, exc: RabbitTodoException) -> None:
        self._exc = exc

    def get_message(self) -> str:
        message = self._parse_exception()
        return ERROR_PREFIX + message

    def _parse_exception(self) -> str:
        error_codes = self._exc.code.split(";")
        return ERROR_MESSAGES.get(error_codes[0])
