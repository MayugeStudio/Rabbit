"""
ITaskRepository class.

Main Class:
- ITaskRepository: The abstract base class for all Task Repositories.

Dependencies:
- rabbit_todo.core.task: task class to be instantiated from ITaskRepository.
- rabbit_todo.common.result: Result class used for error handling.
"""

# --- Standard Library ---
from abc import ABC
from abc import abstractmethod

# --- First Party Library ---
from rabbit_todo.core.task import Task


class ITaskRepository(ABC):
    """Abstract base class for all Task Repositories"""

    @abstractmethod
    def get_all(self) -> list[Task]:
        """Get all tasks."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task:
        """Get the task by id."""
        raise NotImplementedError

    @abstractmethod
    def add(self, task: Task) -> None:
        """Add the task to the repository."""
        raise NotImplementedError

    @abstractmethod
    def remove(self, task: Task) -> None:
        """Remove the task from the repository."""
        raise NotImplementedError

    @abstractmethod
    def update(self, task: Task) -> None:
        """Update the task in the repository."""
        raise NotImplementedError
