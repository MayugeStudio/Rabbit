"""
Add Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.cli.exit_with_error import exit_with_error
from rabbit_todo.common.error_handler import get_message_from_exception
from rabbit_todo.common.rabbit_error import RabbitTodoError
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.entity.generate_next_id import generate_next_id
from rabbit_todo.entity.task import Task
from rabbit_todo.io.file_handler import FileHandler
from rabbit_todo.io.json_task_repository import JsonTaskRepository
from rabbit_todo.success_messages import add_task_success_message


@click.command("add")
@click.argument("task-name", type=click.STRING)
def add_task(task_name: str) -> None:
    """Adds a new task with the given name to the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    try:
        # Create task instance
        next_id = generate_next_id(repo)
        task = Task(next_id, task_name)

        # Execute
        repo.add(task)

        # Message
        print(add_task_success_message(task.name))
    except RabbitTodoError as e:
        message = get_message_from_exception(e)
        exit_with_error(message)
