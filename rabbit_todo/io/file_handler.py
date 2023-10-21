"""
FileHandler
"""

# --- Standard Library ---
import json
from pathlib import Path


class FileHandler:
    """Handles file and directory operations for the Rabbit-Todo application."""

    def __init__(self) -> None:
        self._directory = Path.cwd() / ".rabbit"
        self._files = ["tasks.json"]

    def initialize(self) -> None:
        """Creates the required directory and files if they don't exist."""
        self._directory.mkdir(parents=True, exist_ok=True)

        for file in self._files:
            file_path = self._directory / file

            if not file_path.exists():
                with file_path.open("w", encoding="utf-8") as f:
                    json.dump({"tasks": []}, f, indent=4, ensure_ascii=False)

    def exists(self) -> bool:
        """Returns true if the directory exists, false otherwise."""
        return self._directory.exists()
