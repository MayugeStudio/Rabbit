"""
Rabbit Todo CLI
"""

# --- Third Party Library ---
import click

# --- Local Library ---
from .command_add import add_task
from .command_done import done_task
from .command_list import list_task
from .command_remove import remove_task


@click.group
def cli() -> None:
    """Main entry point for the Rabbit Todo CLI"""


cli.add_command(add_task)  # type: ignore
cli.add_command(remove_task)  # type: ignore
cli.add_command(list_task)  # type: ignore
cli.add_command(done_task)  # type: ignore
