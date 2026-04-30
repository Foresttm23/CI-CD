from src.models import Task


class TaskService:
    def __init__(self):
        self._tasks = []

    def add_task(self, title: str) -> Task:
        """Створює нове завдання та додає його до списку."""
        if not title:
            raise ValueError("Title cannot be empty")

        task = Task(id=len(self._tasks) + 1, title=title)
        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> list[Task]:
        return self._tasks

    def complete_task(self, task_id: int) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False