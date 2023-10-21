"""
Task class.

Main Class:
- Task: Represents a single task.

Dependencies:
    This class doesn't have any dependencies.

Note:
    The identity of task classes managed by ID.
    Task classes with the same ID are considered the same.
"""

from __future__ import annotations

# --- Standard Library ---
from typing import Any


class Task:
    """Represents a single task"""

    def __init__(self, id_: int, name: str, notes: str = "") -> None:
        self._id = id_
        self._name = name
        self._notes = notes
        self._completed = False

    @classmethod
    def from_dict(cls, data: dict[str, int | str | bool]) -> Task:
        """Instantiates a Task from a dictionary"""
        id_ = data["id"]
        name = data["name"]
        completed = data["completed"]
        notes = data["notes"]

        assert isinstance(id_, int)
        assert isinstance(name, str)
        assert isinstance(completed, bool)
        assert isinstance(notes, str)

        instance = cls(id_, name, notes=notes)
        instance._completed = completed
        return instance

    def to_dict(self) -> dict[str, int | str | bool]:
        """Converts the task to dictionary"""
        return {"id": self._id, "name": self._name, "completed": self._completed, "notes": self._notes}

    @property
    def id(self) -> int:
        """Returns the id of the task"""
        return self._id

    @property
    def name(self) -> str:
        """Returns the name of the task"""
        return self._name

    @property
    def notes(self) -> str:
        """Returns the notes of the task"""
        return self._notes

    @property
    def completed(self) -> bool:
        """Returns whether the task is completed or not"""
        return self._completed

    def mark_as_complete(self) -> None:
        """Marks the task as complete"""
        self._completed = True

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Task):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
