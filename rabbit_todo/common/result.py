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
from typing import Callable
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

T = TypeVar("T")
B = TypeVar("B")


class Result(Generic[T]):
    """Contains value or error message"""

    def __init__(self, value: T | None, error_message: str | None = None) -> None:
        self._value = value
        self._message = error_message

    @classmethod
    def ok(cls, value: T) -> Result[T]:
        """Constructs the result with the given value"""
        return cls(value=value)

    @classmethod
    @overload
    def error(cls, error_message: str) -> Result[T]:
        ...

    @classmethod
    @overload
    def error(cls, result: Result[B]) -> Result[T]:
        ...

    @classmethod
    def error(cls, arg: Union[str, Result[B]]) -> Result[T]:
        """Constructs the result with the given error message"""
        if isinstance(arg, str):
            return cls(value=None, error_message=arg)
        elif isinstance(arg, Result):
            return cls(value=None, error_message=arg.message)

        raise TypeError(arg)

    @property
    def message(self) -> str:
        """Returns the error message if it exists"""
        return self._message or "Unknown error occurred."

    def is_success(self) -> bool:
        """Returns true if the result is success otherwise false"""
        return True if self._value is not None else False

    def map(self, func: Callable[[T], B]) -> Result[B]:
        if self.is_success():
            assert self._value is not None
            return Result.ok(func(self._value))
        else:
            return Result.error(self._message or "Unknown error occurred.")

    def unwrap(self) -> T:
        """Retrieves the value from the result. If not success, raises a RuntimeError."""
        if not self.is_success():
            raise RuntimeError("Result is not a success")
        assert self._value is not None
        return self._value
