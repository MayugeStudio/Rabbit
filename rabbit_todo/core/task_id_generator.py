"""
ID Generator for Task class.

Main Class:
- TaskIdGenerator: Generates the task id based on the current max task id.

Dependencies:
- rabbit_todo.core.i_task_repository: ITaskRepository class used for generating task ids.
- rabbit_todo.common.result: Result class used for error handling.

Usage:
    Instantiate TaskIdGenerator with ITaskRepository implementation class.
    Use next_id to generate task id.

Note:
    The next_id() method retrieves the current max task id, increments it by one and returns the result.
    Therefore, be aware that the next_id() method introduces a side effect.
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
