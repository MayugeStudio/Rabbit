"""
Entry-point for rabbit-todo Tool.
"""

# --- First Party Library ---
from rabbit_todo.cmd import cli


def main() -> None:
    """This is the entry point for the rabbit-todo."""
    cli()
