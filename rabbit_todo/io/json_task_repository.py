"""
JSON Task Repository
"""

from __future__ import annotations

# --- Standard Library ---
import json

# --- First Party Library ---
from rabbit_todo.common.error_code import FILE_CORRUPTED_ERROR_CODE
from rabbit_todo.common.error_code import TASK_NOT_FOUND_ERROR_CODE
from rabbit_todo.common.rabbit_exception import RabbitTodoException
from rabbit_todo.config import INITIAL_TASKS_CONTENT
from rabbit_todo.config import TASKS_KEY
from rabbit_todo.entity.i_task_repository import ITaskRepository
from rabbit_todo.entity.task import Task
from rabbit_todo.io.file_handler import FileHandler


class JsonTaskRepository(ITaskRepository):
    """Saves tasks to json file and loads tasks from json file"""

    def __init__(self, file_handler: FileHandler, initial_content: str = INITIAL_TASKS_CONTENT):
        self._file_handler = file_handler
        self._file_handler.initialize(initial_content)

    def _load_json(self) -> dict[str, list[dict[str, int | bool | str]]]:
        try:
            with self._file_handler.open_file_r(TASKS_KEY) as file:
                content: dict[str, list[dict[str, int | bool | str]]] = json.load(file)
                return content
        except json.decoder.JSONDecodeError:
            raise RabbitTodoException(FILE_CORRUPTED_ERROR_CODE) from None

    def _save_tasks(self, tasks: list[Task]) -> None:
        content = {"tasks": [t.to_dict() for t in tasks]}
        with self._file_handler.open_file_w("tasks") as file:
            json.dump(content, file, indent=4, ensure_ascii=False)

    def get_all(self) -> list[Task]:
        tasks = self._load_json()
        return [Task.from_dict(task) for task in tasks["tasks"]]

    def get_by_id(self, task_id: int) -> Task:
        # Get tasks
        tasks = self.get_all()

        # Execute
        for task in tasks:
            if task.id == task_id:
                return task

        raise RabbitTodoException(TASK_NOT_FOUND_ERROR_CODE) from None

    def add(self, task: Task) -> None:
        # Get tasks
        tasks = self.get_all()

        # Execute
        tasks.append(task)

        # Save
        self._save_tasks(tasks)

    def remove(self, task: Task) -> None:
        # Get tasks
        tasks = self.get_all()

        # Execute
        for task_ in tasks[:]:
            if task_.id == task.id:
                tasks.remove(task_)
                self._save_tasks(tasks)
                return

        raise RabbitTodoException(TASK_NOT_FOUND_ERROR_CODE) from None

    def update(self, task: Task) -> None:
        # Get tasks
        tasks = self.get_all()

        # Execute
        for task_ in tasks[:]:
            if task_.id == task.id:
                idx = tasks.index(task_)
                tasks[idx] = task
                self._save_tasks(tasks)
                return

        raise RabbitTodoException(TASK_NOT_FOUND_ERROR_CODE) from None
