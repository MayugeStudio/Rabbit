# --- Third Party Library ---
import json

import pytest

# --- First Party Library ---
from rabbit_todo.domain.generate_next_id import generate_next_id
from rabbit_todo.domain.task import Task
from rabbit_todo.storage.file_handler import FileHandler
from rabbit_todo.storage.task_storage import TaskStorage


@pytest.fixture()
def json_content() -> str:
    tasks = [Task(1, "Test Task 1"), Task(2, "Test Task 2"), Task(3, "Test Task 3")]
    tasks = {"tasks": [task.to_dict() for task in tasks]}
    return json.dumps(tasks)


@pytest.fixture()
def rabbit_file_handler(tmp_path):
    return FileHandler(tmp_path)


def test_generate_next_id(rabbit_file_handler, json_content):
    storage = TaskStorage(rabbit_file_handler, json_content)
    next_id = generate_next_id(storage)
    assert next_id == 4
