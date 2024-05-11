tasks = {}

def add_task():
    task = input("Enter a task: ")
    tasks[len(tasks) + 1] = {"task": task, "completed": False}

def show_tasks():
    print("Tasks:")
    for task_id, task_info in tasks.items():
        task_status = "✓" if task_info["completed"] else "✗"
        print(f"{task_id}. [{task_status}] {task_info['task']}")

def mark_task_completed():
    task_id = int(input("Enter the task ID to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task ID.")

while True:
    print("\nTask Management Application")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")