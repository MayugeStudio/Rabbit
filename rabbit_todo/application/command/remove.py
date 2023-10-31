"""
Remove Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.application.exit_with_error import exit_with_error
from rabbit_todo.application.success_messages import remove_task_success_message
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.errors.error_handler import get_message_from_exception
from rabbit_todo.errors.rabbit_error import RabbitTodoError
from rabbit_todo.storage.file_handler import FileHandler
from rabbit_todo.storage.task_storage import TaskStorage


@click.command("remove")
@click.argument("task-id", type=click.INT)
def remove_task(task_id: int) -> None:
    """Removes a task with the given ID from the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    storage = TaskStorage(file_handler)

    try:
        # Get task instance
        task = storage.get_by_id(task_id)

        # Execute
        storage.remove(task)

        # Message
        print(remove_task_success_message(task.name))

    except RabbitTodoError as e:
        message = get_message_from_exception(e)
        exit_with_error(message)
