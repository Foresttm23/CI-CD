import pytest
from src.logic import TaskService

def test_add_task_success():
    service = TaskService()
    task = service.add_task("Learn GitHub Actions")
    assert task.id == 1
    assert task.title == "Learn GitHub Actions"
    assert len(service.get_all_tasks()) == 1

def test_add_task_too_short_title():
    service = TaskService()
    # Перевірка валідації Pydantic (ValueError або ValidationError)
    with pytest.raises(Exception):
        service.add_task("Hi")

def test_complete_task():
    service = TaskService()
    service.add_task("Test Python code")
    result = service.complete_task(1)
    assert result is True
    assert service.get_all_tasks()[0].completed is True

@pytest.mark.parametrize("task_id", [99, 0, -1])
def test_complete_non_existent_task(task_id):
    service = TaskService()
    assert service.complete_task(task_id) is False