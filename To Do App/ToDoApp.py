
def print_menu():
    """Display the main menu options."""
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    """Prompt user to add a task to the list."""
    try:
        task = input("Enter the task: ").strip()
        if not task:
            raise ValueError("Task cannot be empty.")
        tasks.append(task)
    except ValueError as ve:
        print(ve)
    else:
        print("Task added.")

def view_tasks(tasks):
    """Display all tasks in the list."""
    try:
        if not tasks:
            raise LookupError("No tasks to view.")
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    except LookupError as le:
        print(le)

def delete_task(tasks):
    """Prompt user to delete a task by its number."""
    try:
        if not tasks:
            raise LookupError("No tasks to delete.")
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        del_input = input("Enter the task number to delete: ").strip()
        if not del_input.isdigit():
            raise ValueError("Please enter a valid number.")
        del_idx = int(del_input)
        if 1 <= del_idx <= len(tasks):
            removed = tasks.pop(del_idx - 1)
        else:
            raise IndexError("Task number does not exist.")
    except (LookupError, ValueError, IndexError) as e:
        print(f"Error: {e}")
    else:
        print(f"Removed task: {removed}")

def get_menu_choice():
    """Prompt user for menu choice and validate input."""
    choice = input("Enter your choice (1-4): ").strip()
    if not choice.isdigit():
        raise ValueError("Invalid input. Please enter a number between 1 and 4.")
    return int(choice)

def main():
    """Main loop for the To-Do CLI App."""
    tasks = []
    print("Welcome to the To-Do CLI App!")
    while True:
        print_menu()
        try:
            choice_num = get_menu_choice()
            if choice_num == 1:
                add_task(tasks)
            elif choice_num == 2:
                view_tasks(tasks)
            elif choice_num == 3:
                delete_task(tasks)
            elif choice_num == 4:
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please select a number between 1 and 4.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()