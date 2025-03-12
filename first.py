# Simple To-Do List Application

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks(todo_list):
    if not todo_list:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("\nEnter the task description: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def update_task(todo_list):
    view_tasks(todo_list)
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(todo_list):
            new_task = input("Enter the updated task description: ")
            todo_list[task_num - 1] = new_task
            print(f"Task {task_num} updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(todo_list):
    view_tasks(todo_list)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []

    while True:
        display_menu()
        try:
            choice = int(input("\nChoose an option (1-5): "))
            if choice == 1:
                view_tasks(todo_list)
            elif choice == 2:
                add_task(todo_list)
            elif choice == 3:
                update_task(todo_list)
            elif choice == 4:
                remove_task(todo_list)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
