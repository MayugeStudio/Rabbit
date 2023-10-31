"""
Success Messages
"""

from colorama import Fore


def info_prefix() -> str:
    """Return info-prefix"""
    return Fore.GREEN + "INFO" + Fore.RESET + ": "


def add_task_success_message(task_name: str) -> str:
    """Return adding a task success-message"""
    return info_prefix() + f"Added task {task_name} successfully!"


def remove_task_success_message(task_name: str) -> str:
    """Return removing a task success-message"""
    return info_prefix() + f"Removed task {task_name} successfully!"


def mark_task_as_complete_success_message(task_name: str) -> str:
    """Return mark a task as complete success-message"""
    return info_prefix() + f"Marked {task_name} as completed successfully!"
