import json
from pathlib import Path
from typing import Any

# Works in normal Python files and browser-based Python runners.
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()

DATA_FILE = BASE_DIR / "tasks.json"


def load_tasks() -> list[dict[str, Any]]:
    """Load tasks from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Invalid task data found. Starting with an empty task list.")
        return []

    except json.JSONDecodeError:
        print("The tasks file contains invalid JSON.")
        print("Starting with an empty task list.")
        return []

    except OSError as error:
        print(f"Unable to read the tasks file: {error}")
        return []


def save_tasks(tasks: list[dict[str, Any]]) -> bool:
    """Save tasks to the JSON file."""

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

        return True

    except OSError as error:
        print(f"Unable to save tasks: {error}")
        return False


def display_tasks(tasks: list[dict[str, Any]]) -> None:
    """Display all tasks."""

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks")
    print("-" * 50)

    for index, task in enumerate(tasks, start=1):
        title = task.get("title", "Untitled task")
        completed = task.get("completed", False)

        status = "Completed" if completed else "Pending"
        symbol = "✓" if completed else "○"

        print(f"{index}. {symbol} {title} [{status}]")

    print("-" * 50)


def add_task(tasks: list[dict[str, Any]]) -> None:
    """Add a new task."""

    title = input("\nEnter the task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    new_task = {
        "title": title,
        "completed": False,
    }

    tasks.append(new_task)

    if save_tasks(tasks):
        print("Task added successfully.")
    else:
        tasks.pop()
        print("The task was not added because it could not be saved.")


def get_task_index(
    tasks: list[dict[str, Any]],
    message: str,
) -> int | None:
    """Get and validate a task number from the user."""

    try:
        task_number = int(input(message).strip())
    except ValueError:
        print("Please enter a valid number.")
        return None

    if task_number < 1 or task_number > len(tasks):
        print(f"Please enter a number between 1 and {len(tasks)}.")
        return None

    return task_number - 1


def complete_task(tasks: list[dict[str, Any]]) -> None:
    """Mark a selected task as completed."""

    display_tasks(tasks)

    if not tasks:
        return

    task_index = get_task_index(
        tasks,
        "\nEnter the task number to complete: ",
    )

    if task_index is None:
        return

    if tasks[task_index].get("completed", False):
        print("This task is already completed.")
        return

    tasks[task_index]["completed"] = True

    if save_tasks(tasks):
        print("Task marked as completed successfully.")
    else:
        tasks[task_index]["completed"] = False
        print("The task could not be updated.")


def delete_task(tasks: list[dict[str, Any]]) -> None:
    """Delete a selected task."""

    display_tasks(tasks)

    if not tasks:
        return

    task_index = get_task_index(
        tasks,
        "\nEnter the task number to delete: ",
    )

    if task_index is None:
        return

    removed_task = tasks.pop(task_index)

    if save_tasks(tasks):
        print(f"Deleted task: {removed_task.get('title', 'Untitled task')}")
    else:
        tasks.insert(task_index, removed_task)
        print("The task could not be deleted.")


def main() -> None:
    """Run the Task Manager application."""

    tasks = load_tasks()

    while True:
        print("\n" + "=" * 40)
        print("       PYTHON TASK MANAGER")
        print("=" * 40)
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        print("=" * 40)

        choice = input("Choose an option from 1 to 5: ").strip()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using the Python Task Manager.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
