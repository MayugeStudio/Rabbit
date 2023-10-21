# --- First Party Library ---
from rabbit_todo.core.task import Task


class TestTask:
    def test_task_creation(self):
        task = Task(1, "Test Task")
        assert task.id == 1
        assert task.name == "Test Task"
        assert task.completed is False

    def test_from_dict(self):
        data = {"id": 1, "name": "Test Task", "completed": True, "notes": "Test Notes"}
        task = Task.from_dict(data)
        assert task.id == 1
        assert task.name == "Test Task"
        assert task.completed is True
        assert task.notes == "Test Notes"

    def test_to_dict(self):
        task = Task(1, "Test Task")
        data = task.to_dict()
        assert data["id"] == 1
        assert data["name"] == "Test Task"
        assert data["completed"] is False

    def test_mark_as_complete(self):
        task = Task(1, "Test Task")
        task.mark_as_complete()
        assert task.completed is True

    def test_task_equal_method(self):
        task = Task(1, "Test Task")
        task2 = Task(1, "Test Task")

        assert task == task2
