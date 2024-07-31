def display_menu():
    print("\nTask Manager")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Remove a task")
    print("4. View all tasks")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"description": task, "completed": False})
    print(f'Task added: "{task}"')

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter the task number to complete: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks[task_id]["completed"] = True
            print(f'Task "{tasks[task_id]["description"]}" marked as completed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_id < len(tasks):
            removed_task = tasks.pop(task_id)
            print(f'Task "{removed_task["description"]}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{idx + 1}. {task['description']} [{status}]")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
