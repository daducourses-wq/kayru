class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if title.strip():
            self.tasks.append({"title": title, "completed": False})
            print(f"Added task: '{title}'")
        else:
            print("Task title cannot be empty.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['title']}")
        print()

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f"Marked task {index} as complete.")
        else:
            print("Invalid task number.")