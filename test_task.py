from task_manager import TaskManager

def test_task_manager():
    manager = TaskManager()
    
    # Test adding a task
    manager.add_task("Buy groceries")
    assert len(manager.tasks) == 1
    assert manager.tasks[0]["title"] == "Buy groceries"
    assert manager.tasks[0]["completed"] is False
    
    # Test completing a task
    manager.complete_task(1)
    assert manager.tasks[0]["completed"] is True
    
    print("All tests passed successfully!")

if __name__ == "__main__":
    test_task_manager()