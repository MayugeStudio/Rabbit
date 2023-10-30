# --- Standard Library ---
import json

# --- Third Party Library ---
import pytest

# --- First Party Library ---
from rabbit_todo.core.task import Task
from rabbit_todo.io.file_handler import FileHandler
from rabbit_todo.io.json_task_repository import JsonTaskRepository


@pytest.fixture()
def json_content() -> str:
    tasks = [Task(1, "Test Task 1"), Task(2, "Test Task 2"), Task(3, "Test Task 3")]
    tasks = {"tasks": [task.to_dict() for task in tasks]}
    return json.dumps(tasks)


@pytest.fixture()
def corrupted_json_content() -> str:
    return "Corrupted Json Content"


@pytest.fixture()
def task():
    return Task(100, "Test Task 1")


@pytest.fixture()
def existent_task():
    return Task(1, "Test Task 1")


@pytest.fixture()
def rabbit_file_handler(tmp_path):
    return FileHandler(tmp_path)


class TestJsonRepository:
    def test_get_all(self, json_content, rabbit_file_handler):
        repo = JsonTaskRepository(rabbit_file_handler, json_content)
        result = repo.get_all()
        assert result.is_success() is True
        tasks = result.unwrap()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3

    def test_file_corrupted(self, rabbit_file_handler):
        repo = JsonTaskRepository(rabbit_file_handler, "Corrupted Json Content")
        result = repo.get_all()
        assert result.is_success() is False

    def test_get_task_by_id(self, json_content, rabbit_file_handler):
        repo = JsonTaskRepository(rabbit_file_handler, json_content)
        result = repo.get_by_id(1)
        assert result.is_success() is True
        task = result.unwrap()
        assert task.id == 1
        assert task.name == "Test Task 1"

    def test_add_task(self, task, json_content, rabbit_file_handler):
        repo = JsonTaskRepository(rabbit_file_handler, json_content)
        result = repo.add(task)
        assert result.unwrap() is True

        with rabbit_file_handler.open_file_r("tasks") as file:
            tasks = [Task.from_dict(task_dict) for task_dict in json.load(file)["tasks"]]
        assert len(tasks) == 4

    def test_remove_task(self, existent_task, json_content, rabbit_file_handler):
        repo = JsonTaskRepository(rabbit_file_handler, json_content)
        result = repo.remove(existent_task)
        assert result.unwrap() is True

        with rabbit_file_handler.open_file_r("tasks") as file:
            tasks = [Task.from_dict(task_dict) for task_dict in json.load(file)["tasks"]]
        assert len(tasks) == 2

    def test_update_task(self, existent_task, json_content, rabbit_file_handler):
        repo = JsonTaskRepository(rabbit_file_handler, json_content)
        existent_task.mark_as_complete()
        result = repo.update(existent_task)
        assert result.unwrap() is True

        result = repo.get_by_id(existent_task.id)
        assert result.unwrap().completed is True
