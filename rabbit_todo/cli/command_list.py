"""
List Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.cli.exit_with_error import exit_with_error
from rabbit_todo.common.error_handler import get_message_from_exception
from rabbit_todo.common.rabbit_error import RabbitTodoError
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.io.file_handler import FileHandler
from rabbit_todo.io.task_storage import TaskStorage


@click.command("list")
def list_task() -> None:
    """Lists all tasks in the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = TaskStorage(file_handler)
    try:
        # Get task instances
        tasks = repo.get_all()

        # Execute
        for task in tasks:
            completed_mark = "[X]" if task.completed else "[ ]"
            print(f"{completed_mark}: ID -{task.id:^3}  {task.name}")

    except RabbitTodoError as e:
        message = get_message_from_exception(e)
        exit_with_error(message)
