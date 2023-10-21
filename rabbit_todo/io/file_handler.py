"""
FileHandler
"""

# --- Standard Library ---
import json

# --- First Party Library ---
from rabbit_todo.io.io_utils import Directory
from rabbit_todo.io.io_utils import FileType


class FileHandler:
    """Handles file and directory operations for the Rabbit-Todo application."""

    def __init__(self, directory: Directory) -> None:
        self._directory = directory

    def initialize(self) -> None:
        """Creates the required directory and files if they don't exist."""
        self._directory.path.mkdir(parents=True, exist_ok=True)

        for file in self._directory.children_files:
            file_path = self._directory.path / file.name

            if not file_path.exists():
                with file_path.open("w", encoding="utf-8") as f:
                    if file.type == FileType.JSON:
                        json.dump(json.loads(file.default_content), f, indent=4, ensure_ascii=False)

    def exists(self) -> bool:
        """Returns true if the directory exists, false otherwise."""
        return self._directory.path.exists()
