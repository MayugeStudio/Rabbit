# --- Standard Library ---
import json

# --- Third Party Library ---
import pytest

# --- First Party Library ---
from rabbit_todo.core.task import Task
from rabbit_todo.io.json_task_repository import JsonTaskRepository


@pytest.fixture()
def json_content_path(tmp_path):
    tasks = [Task(1, "Test Task 1"), Task(2, "Test Task 2"), Task(3, "Test Task 3")]
    path = str(tmp_path / "test.json")
    with open(path, "w") as file:
        content = {"tasks": [task.to_dict() for task in tasks]}
        json.dump(content, file, indent=4, ensure_ascii=False)
    return path


@pytest.fixture()
def corrupted_json_content_path(tmp_path):
    path = str(tmp_path / "corrupted.json")
    with open(path, "w") as file:
        file.write("This file is corrupted")
    return path


@pytest.fixture()
def task():
    return Task(100, "Test Task 1")


@pytest.fixture()
def existent_task():
    return Task(1, "Test Task 1")


class TestJsonRepository:
    def test_get_all(self, json_content_path):
        repo = JsonTaskRepository(file_path=json_content_path)
        result = repo.get_all()
        assert result.is_success() is True
        tasks = result.unwrap()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3

    def test_file_not_found(self, tmp_path):
        repo = JsonTaskRepository(file_path=str(tmp_path / "not_found.json"))
        result = repo.get_all()
        assert result.is_success() is True
        assert len(result.unwrap()) == 0

    def test_file_corrupted(self, corrupted_json_content_path):
        repo = JsonTaskRepository(file_path=corrupted_json_content_path)
        result = repo.get_all()
        assert result.is_success() is False

    def test_get_task_by_id(self, json_content_path):
        repo = JsonTaskRepository(file_path=json_content_path)
        result = repo.get_by_id(1)
        assert result.is_success() is True
        task = result.unwrap()
        assert task.id == 1
        assert task.name == "Test Task 1"

    def test_add_task(self, task, json_content_path):
        repo = JsonTaskRepository(file_path=json_content_path)
        result = repo.add(task)
        assert result.unwrap() is True

        with open(json_content_path, "r") as file:
            tasks = [Task.from_dict(task_dict) for task_dict in json.load(file)["tasks"]]
        assert len(tasks) == 4

    def test_remove_task(self, existent_task, json_content_path):
        repo = JsonTaskRepository(file_path=json_content_path)
        result = repo.remove(existent_task)
        assert result.unwrap() is True

        with open(json_content_path, "r") as file:
            tasks = [Task.from_dict(task_dict) for task_dict in json.load(file)["tasks"]]
        assert len(tasks) == 2

    def test_update_task(self, existent_task, json_content_path):
        repo = JsonTaskRepository(file_path=json_content_path)
        existent_task.mark_as_complete()
        result = repo.update(existent_task)
        assert result.unwrap() is True

        result = repo.get_by_id(existent_task.id)
        assert result.unwrap().completed is True
