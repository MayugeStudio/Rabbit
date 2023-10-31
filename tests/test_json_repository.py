# --- Standard Library ---
import json

# --- Third Party Library ---
import pytest

# --- First Party Library ---
from rabbit_todo.domain.task import Task
from rabbit_todo.errors.rabbit_error import RabbitTodoError
from rabbit_todo.storage.file_handler import FileHandler
from rabbit_todo.storage.task_storage import TaskStorage


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


class TestTaskStorage:
    def test_get_all(self, json_content, rabbit_file_handler):
        storage = TaskStorage(rabbit_file_handler, json_content)
        tasks = storage.get_all()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3

    def test_file_corrupted(self, rabbit_file_handler):
        storage = TaskStorage(rabbit_file_handler, "Corrupted Json Content")
        with pytest.raises(RabbitTodoError):
            storage.get_all()

    def test_get_task_by_id(self, json_content, rabbit_file_handler):
        storage = TaskStorage(rabbit_file_handler, json_content)
        task = storage.get_by_id(1)
        assert task.id == 1
        assert task.name == "Test Task 1"

    def test_add_task(self, task, json_content, rabbit_file_handler):
        storage = TaskStorage(rabbit_file_handler, json_content)
        storage.add(task)

        with rabbit_file_handler.open_file_r("tasks") as file:
            tasks = [Task.from_dict(task_dict) for task_dict in json.load(file)["tasks"]]
        assert len(tasks) == 4

    def test_remove_task(self, existent_task, json_content, rabbit_file_handler):
        storage = TaskStorage(rabbit_file_handler, json_content)
        storage.remove(existent_task)

        with rabbit_file_handler.open_file_r("tasks") as file:
            tasks = [Task.from_dict(task_dict) for task_dict in json.load(file)["tasks"]]
        assert len(tasks) == 2

    def test_update_task(self, existent_task, json_content, rabbit_file_handler):
        storage = TaskStorage(rabbit_file_handler, json_content)
        existent_task.mark_as_complete()
        storage.update(existent_task)

        task = storage.get_by_id(existent_task.id)
        assert task.completed is True
