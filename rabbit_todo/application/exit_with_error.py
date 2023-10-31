"""
Exit with error Function
"""

# --- Standard Library ---
import sys


def exit_with_error(message: str) -> None:
    """Prints the provided message and exits the application with an error status."""
    print(message)
    sys.exit(1)
