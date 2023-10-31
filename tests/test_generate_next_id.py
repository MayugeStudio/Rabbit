# --- Third Party Library ---
import pytest

# --- First Party Library ---
from rabbit_todo.common.error_code import TASK_NOT_FOUND_ERROR_CODE
from rabbit_todo.common.rabbit_exception import RabbitTodoException
from rabbit_todo.core_models.i_task_repository import ITaskRepository
from rabbit_todo.core_models.task import Task
from rabbit_todo.core_models.task_id_generator import generate_next_id


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._tasks = [Task(1, "Test Task 1"), Task(2, "Test Task 2"), Task(3, "Test Task 3")]

    def get_all(self) -> list[Task]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                return task

        raise RabbitTodoException(TASK_NOT_FOUND_ERROR_CODE)

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def remove(self, task: Task) -> None:
        self._tasks.remove(task)

    def update(self, task: Task) -> None:
        self._tasks.remove(task)
        self._tasks.append(task)


@pytest.fixture()
def task_repository():
    return InMemoryTaskRepository()


def test_generate_next_id(task_repository):
    next_id = generate_next_id(task_repository)
    assert next_id == 4
