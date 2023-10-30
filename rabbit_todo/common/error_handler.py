from __future__ import annotations


class RabbitTodoException(Exception):
    def __init__(self, code: str, rabbit_exception: RabbitTodoException = None) -> None:
        self._code = code + ";"
        if rabbit_exception is not None:
            self._code += rabbit_exception.code

    @property
    def code(self) -> str:
        return self._code + ";"
