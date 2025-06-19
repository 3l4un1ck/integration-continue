from .models import Task

class TodoManager:
    def __init__(self):
        self.tasks = []
        self._id_counter = 1

    def add_task(self, title):
        task = Task(id=self._id_counter, title=title)
        self.tasks.append(task)
        self._id_counter += 1
        return task

    def remove_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return task
        raise ValueError("Task not found")

    def list_tasks(self, completed=None):
        if completed is None:
            return self.tasks
        return [t for t in self.tasks if t.completed == completed]
