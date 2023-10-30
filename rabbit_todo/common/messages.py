"""
This module contains common messages used in the todo project.
"""
# --- Third Party Library ---
from colorama import Fore


def info_prefix() -> str:
    return Fore.GREEN + "INFO" + Fore.RESET + ": "


def add_task_success_message(task_name: str) -> str:
    return info_prefix() + f"Added task {task_name} successfully!"


def remove_task_success_message(task_name: str) -> str:
    return info_prefix() + f"Removed task {task_name} successfully!"


def mark_task_as_complete_success_message(task_name: str) -> str:
    return info_prefix() + f"Marked {task_name} as completed successfully!"
