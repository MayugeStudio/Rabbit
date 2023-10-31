"""
List Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.application.exit_with_error import exit_with_error
from rabbit_todo.errors.error_handler import get_message_from_exception
from rabbit_todo.errors.rabbit_error import RabbitTodoError
from rabbit_todo.storage.task_storage import TaskStorage


@click.command("list")
@click.pass_obj
def list_task(storage: TaskStorage) -> None:
    """Lists all tasks in the repository."""
    try:
        # Get task instances
        tasks = storage.get_all()

        # Execute
        for task in tasks:
            completed_mark = "[X]" if task.completed else "[ ]"
            print(f"{completed_mark}: ID -{task.id:^3}  {task.name}")

    except RabbitTodoError as e:
        message = get_message_from_exception(e)
        exit_with_error(message)
