"""
ID Generator for Task class.
"""

# --- First Party Library ---
from rabbit_todo.core.i_task_repository import ITaskRepository


class TaskIdGenerator:
    """Generates the task id based on the current max task id"""

    def __init__(self, repository: ITaskRepository) -> None:
        self._repository = repository

    def next_id(self) -> int:
        """Retrieves the current max task id, increments it by one and returns the result."""
        tasks = self._repository.get_all()

        if not tasks:
            return 0

        max_id = max(task.id for task in tasks)
        return max_id + 1
