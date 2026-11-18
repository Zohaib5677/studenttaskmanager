"""Student Task Manager - console application.

Run with:
    python main.py

Menu:
    1. Add task
    2. Display tasks
    3. Complete task
    4. Delete task
    5. Exit
"""

from task_manager import TaskManager


def show_menu():
    print("\n--- Student Task Manager ---")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def display_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet. Add a task first.")
        return
    print("\nYour tasks:")
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f'{status} {task["id"]}. {task["title"]}')


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            task = manager.add_task(title)
            if task is None:
                print("Error: Task title cannot be empty.")
            else:
                print(f'Task added: {task["id"]}. {task["title"]}')

        elif choice == "2":
            display_tasks(manager)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
            except ValueError:
                print("Error: Please enter a valid task ID (a number).")
                continue
            if manager.complete_task(task_id):
                print(f"Task {task_id} marked as completed.")
            else:
                print(f"Error: No task found with ID {task_id}.")

        elif choice == "4":
                    try:
                        task_id = int(input("Enter task ID to delete: "))
                    except ValueError:
                        print("Error: Please enter a valid task ID (a number).")
                        continue
                    if manager.delete_task(task_id):
                        print(f"Task {task_id} deleted.")
                    else:
                        print(f"Error: No task found with ID {task_id}.")
        

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
