# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.cli.exit_with_error import exit_with_error
from rabbit_todo.common.error_handler import ErrorHandler
from rabbit_todo.common.error_handler import RabbitTodoException
from rabbit_todo.common.messages import mark_task_as_complete_success_message
from rabbit_todo.config import ROOT_DIR_PATH
from rabbit_todo.io.file_handler import FileHandler
from rabbit_todo.io.json_task_repository import JsonTaskRepository


@click.command("done")
@click.argument("task-id", type=click.INT)
def done_task(task_id: int) -> None:
    """Marks a task with the given ID as completed."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    try:
        # Get task instance
        task = repo.get_by_id(task_id)

        # Execute
        task.mark_as_complete()
        repo.update(task)

        # Message
        print(mark_task_as_complete_success_message(task.name))

    except RabbitTodoException as e:
        handler = ErrorHandler(e)
        exit_with_error(handler.get_message())
