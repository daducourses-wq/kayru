from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n--- Simple Todo App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            title = input("Enter task description: ")
            manager.add_task(title)
        elif choice == "3":
            manager.list_tasks()
            try:
                idx = int(input("Enter task number to complete: "))
                manager.complete_task(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()