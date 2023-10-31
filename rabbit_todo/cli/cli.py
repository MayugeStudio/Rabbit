"""
Rabbit Todo CLI
"""

# --- Third Party Library ---
import click

# --- First Party Library ---
from rabbit_todo.application.command.add import add_task
from rabbit_todo.application.command.done import done_task
from rabbit_todo.application.command.list import list_task
from rabbit_todo.application.command.remove import remove_task
from rabbit_todo.application.create_app import create_app


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Main entry point for the Rabbit Todo CLI"""
    ctx.obj = create_app()


cli.add_command(add_task)
cli.add_command(remove_task)
cli.add_command(list_task)
cli.add_command(done_task)
