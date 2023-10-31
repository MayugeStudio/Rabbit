"""
ID Generator for Task class.
"""

# --- First Party Library ---
from rabbit_todo.storage.task_storage import TaskStorage


def generate_next_id(storage: TaskStorage) -> int:
    """Generates the task id based on the current max task id"""
    tasks = storage.get_all()

    if len(tasks) == 0:
        return 0

    max_id = max(task.id for task in tasks)
    return max_id + 1
