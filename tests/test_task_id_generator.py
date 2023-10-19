# --- Third Party Library ---
import pytest

# --- First Party Library ---
from rabbit_todo.common.result import Result
from rabbit_todo.core.i_task_repository import ITaskRepository
from rabbit_todo.core.task import Task
from rabbit_todo.core.task_id_generator import TaskIdGenerator


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._tasks = [Task(1, "Test Task 1"), Task(2, "Test Task 2"), Task(3, "Test Task 3")]

    def get_all(self) -> Result[list[Task]]:
        return Result.ok(self._tasks)

    def get_by_id(self, task_id: int) -> Result[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return Result.ok(task)

        return Result.error("Task not found")

    def add(self, task: Task) -> Result[bool]:
        self._tasks.append(task)
        return Result.ok(True)

    def remove(self, task: Task) -> Result[bool]:
        self._tasks.remove(task)
        return Result.ok(True)

    def update(self, task: Task) -> Result[bool]:
        self._tasks.remove(task)
        self._tasks.append(task)
        return Result.ok(True)


@pytest.fixture
def task_repository():
    return InMemoryTaskRepository()


class TestTaskIdGenerator:
    def test_next_id(self, task_repository):
        gen = TaskIdGenerator(task_repository)
        result = gen.next_id()
        assert result.is_success() is True
        assert result.unwrap() == 4
