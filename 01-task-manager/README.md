# Python Command-Line Task Manager

A simple and practical command-line Task Manager developed using Python.

This application allows users to add, view, complete, and delete tasks while saving task information locally in a JSON file.

The project demonstrates essential Python concepts such as functions, loops, lists, dictionaries, file handling, JSON data processing, exception handling, input validation, type hints, and modular programming.

---

## Features

- Add new tasks
- View all saved tasks
- Mark tasks as completed
- Delete existing tasks
- Save task information automatically in a JSON file
- Load previously saved tasks when the application starts
- Display completed and pending task statuses
- Validate user input
- Handle invalid menu options
- Handle incorrect task numbers
- Handle missing or corrupted JSON files
- Support local and compatible browser-based Python environments

---

## Technologies Used

- Python 3
- JSON
- Python `pathlib` module
- Python type hints
- Command-Line Interface
- Git
- GitHub

---

## Python Concepts Demonstrated

This project demonstrates the following Python concepts:

- Variables and data types
- Functions
- Lists
- Dictionaries
- Conditional statements
- Loops
- User input
- String handling
- File handling
- JSON data processing
- Exception handling
- Input validation
- Type hints
- Function documentation
- Modular programming
- Main program execution using:

```python
if __name__ == "__main__":
    main()
```

---

## Project Structure

```text
python-mini-projects/
│
└── 01-task-manager/
    │
    ├── task_manager.py
    ├── tasks.json
    └── README.md
```

The `tasks.json` file is automatically created after the user successfully adds the first task.

---

## How the Application Works

When the application starts, it checks whether a `tasks.json` file already exists.

- If the file exists, saved tasks are loaded.
- If the file does not exist, the application starts with an empty task list.
- When a task is added, completed, or deleted, the updated task list is saved automatically.
- Each task is stored as a Python dictionary and saved in JSON format.

Example task:

```json
{
    "title": "Complete Python assignment",
    "completed": false
}
```

---

## Installation

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installed version using:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

---

### Step 2: Clone the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/ipenetikarthik/python-mini-projects.git
```

---

### Step 3: Open the Project Folder

```bash
cd python-mini-projects/01-task-manager
```

---

### Step 4: Run the Application

```bash
python task_manager.py
```

On some systems, use:

```bash
python3 task_manager.py
```

---

## Application Menu

After running the program, the following menu will appear:

```text
========================================
       PYTHON TASK MANAGER
========================================
1. View tasks
2. Add task
3. Complete task
4. Delete task
5. Exit
========================================
Choose an option from 1 to 5:
```

---

## How to Use the Application

### 1. View Tasks

Select option:

```text
1
```

The application displays all available tasks with their current status.

Example:

```text
Your Tasks
--------------------------------------------------
1. ○ Complete Python assignment [Pending]
2. ✓ Practice SQL queries [Completed]
--------------------------------------------------
```

---

### 2. Add a Task

Select option:

```text
2
```

Enter a task title when prompted.

Example:

```text
Enter the task: Complete Python assignment
Task added successfully.
```

The new task is saved automatically in the `tasks.json` file.

---

### 3. Mark a Task as Completed

Select option:

```text
3
```

The application displays all tasks.

Enter the number of the task you want to complete.

Example:

```text
Enter the task number to complete: 1
Task marked as completed successfully.
```

The task status changes from `Pending` to `Completed`.

---

### 4. Delete a Task

Select option:

```text
4
```

Enter the number of the task you want to delete.

Example:

```text
Enter the task number to delete: 2
Deleted task: Practice SQL queries
```

The selected task is removed from the task list and the JSON file is updated.

---

### 5. Exit the Application

Select option:

```text
5
```

The application closes safely.

Example:

```text
Thank you for using the Python Task Manager.
```

---

## Example JSON Data

Tasks are stored in the following format:

```json
[
    {
        "title": "Complete Python assignment",
        "completed": false
    },
    {
        "title": "Practice SQL queries",
        "completed": true
    }
]
```

Each task contains:

- `title`: The task name
- `completed`: The task completion status

A value of `false` means the task is pending.

A value of `true` means the task is completed.

---

## Main Functions

### `load_tasks()`

Loads existing tasks from the `tasks.json` file.

It also handles:

- Missing files
- Invalid JSON data
- File-reading errors

---

### `save_tasks()`

Saves the current task list to the `tasks.json` file.

It uses formatted JSON output for better readability.

---

### `display_tasks()`

Displays all tasks with:

- Task number
- Task title
- Completion symbol
- Completion status

---

### `add_task()`

Accepts a task title from the user and adds it to the task list.

Empty task names are not accepted.

---

### `get_task_index()`

Validates the task number entered by the user.

It ensures that:

- The entered value is a number
- The task number is within the available range

---

### `complete_task()`

Marks a selected task as completed.

It also prevents users from completing an already completed task.

---

### `delete_task()`

Deletes a selected task from the task list and updates the JSON file.

---

### `main()`

Controls the complete application flow and continuously displays the main menu until the user selects the exit option.

---

## Error Handling

The application handles the following situations:

- Empty task names
- Invalid menu options
- Incorrect task numbers
- Non-numeric task input
- Missing JSON files
- Invalid JSON content
- File-reading problems
- File-writing problems
- Attempts to complete an already completed task
- Task numbers outside the available range

Example invalid input response:

```text
Please enter a valid number.
```

Example invalid menu response:

```text
Invalid option. Please choose a number from 1 to 5.
```

---

## Browser-Based Runner Compatibility

The project includes the following path-handling logic:

```python
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()
```

This allows the program to work in:

- Normal Python files
- Local development environments
- Some browser-based Python runners where `__file__` is unavailable

---

## Learning Outcomes

By developing this project, I practised:

- Dividing a program into reusable functions
- Managing structured data using dictionaries
- Storing application data using JSON
- Reading and writing files
- Validating user input
- Handling runtime errors
- Creating menu-driven applications
- Using Python type hints
- Writing readable and maintainable code
- Organizing a Python project professionally
- Using GitHub for project documentation and version control

---

## Future Enhancements

The following features may be added in future versions:

- Edit an existing task
- Add task descriptions
- Add due dates
- Add task priorities
- Add task categories
- Search tasks
- Filter tasks by status
- Sort tasks by date or priority
- Display overdue tasks
- Add confirmation before deleting a task
- Add multiple user accounts
- Store task data in an SQL database
- Create a graphical user interface
- Develop a REST API version
- Build a web-based Task Manager
- Add user authentication
- Add unit tests
- Package the application for installation

---

## Repository

The complete source code is available at:

[github.com/ipenetikarthik/python-mini-projects](https://github.com/ipenetikarthik/python-mini-projects)

---

## Author

### Peneti Karthik

Python Developer focused on building practical applications and strengthening backend-development, database, API, and problem-solving skills.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## Purpose

This project was created for learning, practice, portfolio development, and demonstration of fundamental Python programming skills.

---

## License

This project is available for educational and portfolio purposes.

---

## Feedback

Suggestions and feedback are welcome.

You can explore the repository, review the code, and follow my GitHub profile to see future Python projects.

---

<p align="center">
  <strong>Thank you for visiting the Python Command-Line Task Manager project.</strong>
</p>

<p align="center">
  Developed by Peneti Karthik
</p>
