"""
This module contains common messages used in the todo project.
"""
# --- Third Party Library ---
from colorama import Fore

INFO_PREFIX = Fore.GREEN + "INFO" + Fore.RESET + ": "


class SuccessMessage:
    """Generates Success messages"""

    _ADD_TASK = INFO_PREFIX + "Added task {task_name} successfully!"
    _REMOVE_TASK = INFO_PREFIX + "Removed task {task_name} successfully!"
    _MARK_TASK_AS_COMPLETE = INFO_PREFIX + "Marked {task_name} as completed successfully!"

    @classmethod
    def add_task(cls, task_name: str) -> str:
        """Returns Added the task success message"""
        return cls._ADD_TASK.format(task_name=task_name)

    @classmethod
    def remove_task(cls, task_name: str) -> str:
        """Returns Removed the task success message"""
        return cls._REMOVE_TASK.format(task_name=task_name)

    @classmethod
    def mark_as_complete(cls, task_name: str) -> str:
        """Returns Marked the task as completed successful message"""
        return cls._MARK_TASK_AS_COMPLETE.format(task_name=task_name)
