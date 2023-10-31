"""
ID Generator for Task class.
"""

# --- First Party Library ---
from rabbit_todo.core.i_task_repository import ITaskRepository


def generate_next_id(repository: ITaskRepository) -> int:
    """Generates the task id based on the current max task id"""
    tasks = repository.get_all()

    if len(tasks) == 0:
        return 0

    max_id = max(task.id for task in tasks)
    return max_id + 1
