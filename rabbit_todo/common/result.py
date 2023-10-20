"""
Result class

MainClass
- Result: Contains value or error message.
          This class is used for error handling.

Dependencies:
    This class doesn't have any dependencies.

Note:
    This class is implemented similarly to the `Result` type in Rust.
"""

from __future__ import annotations

# --- Standard Library ---
from typing import Generic
from typing import TypeVar

T = TypeVar("T")
B = TypeVar("B")


class Result(Generic[T]):
    """Contains value or error message"""

    def __init__(self, value: T | None, is_success: bool, error_message: str | None = None) -> None:
        self._value = value
        self._is_success = is_success
        self._message = error_message

    @classmethod
    def ok(cls, value: T) -> Result[T]:
        """Constructs the result with the given value"""
        return cls(value=value, is_success=True)

    @classmethod
    def error(cls, error_message: str) -> Result[T]:
        """Constructs the result with the given error message"""
        return cls(value=None, is_success=False, error_message=error_message)

    @classmethod
    def from_result(cls, result: Result[B]) -> Result[T]:
        """Constructs a new result from an existing result."""
        if result.is_success():
            return cls.ok(result.unwrap())
        return cls.error(result.message)

    @property
    def message(self) -> str | None:
        """Returns the error message if it exists"""
        return self._message

    def is_success(self) -> bool:
        """Returns true if the result is success otherwise false"""
        return self._is_success

    def unwrap(self) -> T:
        """Retrieves the value from the result. If not success, raises a RuntimeError."""
        if not self._is_success:
            raise RuntimeError("Result is not a success")
        return self._value
