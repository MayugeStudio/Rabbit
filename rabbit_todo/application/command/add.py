"""
Add Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.application.exit_with_error import exit_with_error
from rabbit_todo.application.success_messages import add_task_success_message
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.domain.generate_next_id import generate_next_id
from rabbit_todo.domain.task import Task
from rabbit_todo.errors.error_handler import get_message_from_exception
from rabbit_todo.errors.rabbit_error import RabbitTodoError
from rabbit_todo.storage.file_handler import FileHandler
from rabbit_todo.storage.task_storage import TaskStorage


@click.command("add")
@click.argument("task-name", type=click.STRING)
def add_task(task_name: str) -> None:
    """Adds a new task with the given name to the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    storage = TaskStorage(file_handler)

    try:
        # Create task instance
        next_id = generate_next_id(storage)
        task = Task(next_id, task_name)

        # Execute
        storage.add(task)

        # Message
        print(add_task_success_message(task.name))
    except RabbitTodoError as e:
        message = get_message_from_exception(e)
        exit_with_error(message)
