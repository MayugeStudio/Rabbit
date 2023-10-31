"""
This module provides create-application-function
"""
# --- First Party Library ---
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.storage.file_handler import FileHandler
from rabbit_todo.storage.task_storage import TaskStorage


def create_app() -> TaskStorage:
    """Create Application Method"""
    file_handler = FileHandler(ROOT_DIR_PATH)
    task_storage = TaskStorage(file_handler)
    return task_storage
