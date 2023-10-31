"""
Done Command
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.application.exit_with_error import exit_with_error
from rabbit_todo.application.success_messages import mark_task_as_complete_success_message
from rabbit_todo.errors.error_handler import get_message_from_exception
from rabbit_todo.errors.rabbit_error import RabbitTodoError
from rabbit_todo.storage.task_storage import TaskStorage


@click.command("done")
@click.argument("task-id", type=click.INT)
@click.pass_obj
def done_task(storage: TaskStorage, task_id: int) -> None:
    """Marks a task with the given ID as completed."""
    try:
        # Get task instance
        task = storage.get_by_id(task_id)

        # Execute
        task.mark_as_complete()
        storage.update(task)

        # Message
        print(mark_task_as_complete_success_message(task.name))

    except RabbitTodoError as e:
        message = get_message_from_exception(e)
        exit_with_error(message)
