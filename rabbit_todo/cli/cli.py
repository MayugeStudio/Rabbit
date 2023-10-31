"""
Rabbit Todo CLI
"""

# --- Third Party Library ---
import click

# --- Local Library ---
from rabbit_todo.application.command.add import add_task
from rabbit_todo.application.command.done import done_task
from rabbit_todo.application.command.list import list_task
from rabbit_todo.application.command.remove import remove_task


@click.group
def cli() -> None:
    """Main entry point for the Rabbit Todo CLI"""


cli.add_command(add_task)
cli.add_command(remove_task)
cli.add_command(list_task)
cli.add_command(done_task)
