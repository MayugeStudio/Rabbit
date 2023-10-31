"""
Remove Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.cli.exit_with_error import exit_with_error
from rabbit_todo.common.error_handler import ErrorHandler
from rabbit_todo.common.error_handler import RabbitTodoException
from rabbit_todo.common.messages import remove_task_success_message
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.io.file_handler import FileHandler
from rabbit_todo.io.json_task_repository import JsonTaskRepository


@click.command("remove")
@click.argument("task-id", type=click.INT)
def remove_task(task_id: int) -> None:
    """Removes a task with the given ID from the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    try:
        # Get task instance
        task = repo.get_by_id(task_id)

        # Execute
        repo.remove(task)

        # Message
        print(remove_task_success_message(task.name))

    except RabbitTodoException as e:
        handler = ErrorHandler(e)
        exit_with_error(handler.get_message())
