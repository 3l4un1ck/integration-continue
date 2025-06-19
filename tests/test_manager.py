import pytest
from todo.manager import TodoManager

@pytest.fixture
def manager():
    return TodoManager()

def test_add_task(manager):
    task = manager.add_task("Write tests")
    assert task.title == "Write tests"
    assert not task.completed

def test_mark_completed(manager):
    task = manager.add_task("Test task")
    manager.mark_completed(task.id)
    assert manager.list_tasks(completed=True)[0].id == task.id

def test_remove_task(manager):
    task = manager.add_task("To be deleted")
    manager.remove_task(task.id)
    assert len(manager.list_tasks()) == 0

def test_list_incomplete_tasks(manager):
    manager.add_task("Incomplete task")
    assert len(manager.list_tasks(completed=False)) == 1
