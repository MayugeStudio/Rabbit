"""
Rabbit Todo CLI

This module provides command-line interface functionality for Rabbit Todo application.
"""

# --- Standard Library ---
import sys

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.common.messages import add_task_success_message
from rabbit_todo.common.messages import mark_task_as_complete_success_message
from rabbit_todo.common.messages import remove_task_success_message
from rabbit_todo.core.task import Task
from rabbit_todo.core.task_id_generator import TaskIdGenerator
from rabbit_todo.io.file_handler import FileHandler
from rabbit_todo.io.json_task_repository import JsonTaskRepository
from rabbit_todo.io.path_config import ROOT_DIR_PATH


def exit_with_error(message: str) -> None:
    """Prints the provided message and exits the application with an error status."""
    print(message)
    sys.exit(1)


@click.group
def cli() -> None:
    """Main entry point for the Rabbit Todo CLI"""


@cli.command("add")
@click.argument("task-name", type=click.STRING)
def add_task(task_name: str) -> None:
    """Adds a new task with the given name to the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    # Create task instance
    generator = TaskIdGenerator(repo)
    next_id = generator.next_id()
    task = Task(next_id, task_name)

    # Execute
    repo.add(task)

    # Message
    add_task_success_message(task.name)


@cli.command("remove")
@click.argument("task-id", type=click.INT)
def remove_task(task_id: int) -> None:
    """Removes a task with the given ID from the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    # Get task instance
    task = repo.get_by_id(task_id)

    # Execute
    repo.remove(task)

    # Message
    remove_task_success_message(task.name)


@cli.command("done")
@click.argument("task-id", type=click.INT)
def done_task(task_id: int) -> None:
    """Marks a task with the given ID as completed."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    # Get task instance
    task = repo.get_by_id(task_id)

    # Execute
    task.mark_as_complete()
    repo.update(task)

    # Message
    mark_task_as_complete_success_message(task.name)


@cli.command("list")
def list_task() -> None:
    """Lists all tasks in the repository."""
    file_handler = FileHandler(ROOT_DIR_PATH)
    repo = JsonTaskRepository(file_handler)

    # Get task instances
    tasks = repo.get_all()

    # Execute
    for task in tasks:
        completed_mark = "[X]" if task.completed else "[ ]"
        print(f"{completed_mark}: ID -{task.id:^3}  {task.name}")
