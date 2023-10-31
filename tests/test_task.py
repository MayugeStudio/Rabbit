# --- Standard Library ---
from datetime import datetime

# --- First Party Library ---
from rabbit_todo.entity.task import Task


class TestTask:
    def test_task_creation(self):
        task = Task(1, "Test Task")
        assert task.id == 1
        assert task.name == "Test Task"
        assert task.completed is False

    def test_from_dict(self):
        now = datetime.now().replace(microsecond=0)
        data = {
            "id": 1,
            "name": "Test Task",
            "completed": True,
            "notes": "Test Notes",
            "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": now.strftime("%Y-%m-%d %H:%M:%S"),
        }
        task = Task.from_dict(data)
        assert task.id == 1
        assert task.name == "Test Task"
        assert task.completed is True
        assert task.created_at == now
        assert task.updated_at == now

    def test_to_dict(self):
        task = Task(1, "Test Task")
        data = task.to_dict()
        assert data["id"] == 1
        assert data["name"] == "Test Task"
        assert data["completed"] is False

    def test_to_dict_with_time(self):
        created_at = datetime.now().replace(microsecond=0)
        updated_at = datetime.now().replace(microsecond=0)
        task = Task(1, "Test Task", created_at=datetime.now(), updated_at=updated_at)
        data = task.to_dict()
        assert data["id"] == 1
        assert data["name"] == "Test Task"
        assert data["completed"] is False
        assert data["created_at"] == created_at.strftime("%Y-%m-%d %H:%M:%S")
        assert data["updated_at"] == updated_at.strftime("%Y-%m-%d %H:%M:%S")

    def test_mark_as_complete(self):
        task = Task(1, "Test Task")
        task.mark_as_complete()
        assert task.completed is True

    def test_task_equal_method(self):
        task = Task(1, "Test Task")
        task2 = Task(1, "Test Task")

        assert task == task2
