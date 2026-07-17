# Python Command-Line Expense Tracker

A practical command-line Expense Tracker developed using Python.

The application allows users to record, view, analyse, and delete expenses while storing the data locally in a JSON file. It provides category-wise and monthly summaries to help users understand their spending.

This project demonstrates Python programming, JSON file handling, date validation, numerical calculations, exception handling, type hints, input validation, and modular application design.

---

## Features

- Add new expense records
- Record expense description
- Assign an expense category
- Enter and validate expense amounts
- Enter a custom date or use the current date
- View all saved expenses
- Automatically calculate total spending
- Display category-wise expense summaries
- Display monthly expense summaries
- Delete expenses with confirmation
- Save expenses automatically in JSON format
- Load previously saved expenses
- Handle invalid input and corrupted files
- Support local and compatible browser-based Python environments

---

## Technologies Used

- Python 3
- JSON
- Python `datetime` module
- Python `pathlib` module
- Python type hints
- Command-Line Interface
- Git
- GitHub

---

## Python Concepts Demonstrated

This project demonstrates:

- Variables and data types
- Functions
- Lists and dictionaries
- Conditional statements
- Loops
- User input
- String formatting
- Lambda expressions
- Sorting data
- File handling
- JSON serialization and deserialization
- Date parsing and formatting
- Numerical calculations
- Exception handling
- Input validation
- Type hints
- Modular programming
- Main-program execution

```python
if __name__ == "__main__":
    main()
```

---

## Project Structure

```text
python-mini-projects/
│
└── 02-expense-tracker/
    │
    ├── expense_tracker.py
    ├── expenses.json
    └── README.md
```

The `expenses.json` file is created automatically after the first expense is saved successfully.

---

## How the Application Works

When the program starts, it checks whether an `expenses.json` file exists.

- If the file exists, previously saved expenses are loaded.
- If the file does not exist, the application starts with an empty list.
- Every added or deleted expense updates the JSON file automatically.
- Expense summaries are calculated from the saved records.

Each expense is stored as a dictionary containing:

```json
{
    "description": "Monthly groceries",
    "category": "Food",
    "amount": 2500.00,
    "date": "2026-07-17"
}
```

---

## Installation

### 1. Install Python

Make sure Python 3 is installed.

Check the installed version:

```bash
python --version
```

On some systems:

```bash
python3 --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/ipenetikarthik/python-mini-projects.git
```

---

### 3. Open the Project Directory

```bash
cd python-mini-projects/02-expense-tracker
```

---

### 4. Run the Application

```bash
python expense_tracker.py
```

On some systems:

```bash
python3 expense_tracker.py
```

---

## Application Menu

After running the program, the following menu appears:

```text
================================================
          PYTHON EXPENSE TRACKER
================================================
1. View all expenses
2. Add a new expense
3. View category summary
4. View monthly summary
5. Delete an expense
6. Exit
================================================
Choose an option from 1 to 6:
```

---

## How to Use the Application

### 1. View All Expenses

Select:

```text
1
```

The application displays all saved expenses with:

- Expense number
- Date
- Category
- Description
- Amount
- Total spending

Example:

```text
ALL EXPENSES
==================================================================================
No.  Date          Category          Description                         Amount
----------------------------------------------------------------------------------
1    2026-07-17    Food              Monthly groceries                ₹2500.00
2    2026-07-16    Transport         Bus pass                         ₹1200.00
----------------------------------------------------------------------------------
Total Expenses                                                    ₹3700.00
==================================================================================
```

---

### 2. Add a New Expense

Select:

```text
2
```

Enter the requested information.

Example:

```text
Enter the description: Monthly groceries
Enter the category: Food
Enter the amount: ₹2500
Enter the date (YYYY-MM-DD) or press Enter for today:
```

When the date field is left empty, the current date is used automatically.

After successful validation:

```text
Expense added successfully.
```

---

### 3. View Category Summary

Select:

```text
3
```

The program groups expenses by category and calculates the total amount for each category.

Example:

```text
CATEGORY SUMMARY
==================================================
Category                                    Amount
--------------------------------------------------
Food                                      ₹2500.00
Transport                                 ₹1200.00
--------------------------------------------------
Grand Total                               ₹3700.00
==================================================
```

---

### 4. View Monthly Summary

Select:

```text
4
```

The application groups expenses by month.

Example:

```text
MONTHLY SUMMARY
==================================================
Month                                       Amount
--------------------------------------------------
July 2026                                 ₹3700.00
--------------------------------------------------
Grand Total                               ₹3700.00
==================================================
```

---

### 5. Delete an Expense

Select:

```text
5
```

The program displays the available expenses and asks for the expense number.

Example:

```text
Enter the expense number: 2
Delete 'Bus pass'? (y/n): y
Deleted expense: Bus pass
```

Entering `n` cancels the deletion.

---

### 6. Exit the Application

Select:

```text
6
```

The application closes safely.

```text
Thank you for using the Python Expense Tracker.
```

---

## Input Validation

The application validates:

- Empty descriptions
- Empty categories
- Non-numeric amounts
- Zero or negative amounts
- Incorrect date formats
- Invalid menu choices
- Non-numeric expense numbers
- Expense numbers outside the available range
- Delete confirmations

The accepted date format is:

```text
YYYY-MM-DD
```

Example:

```text
2026-07-17
```

---

## Error Handling

The application handles:

- Missing JSON files
- Corrupted JSON data
- File-reading errors
- File-writing errors
- Invalid dates
- Invalid numeric values
- Empty expense records
- Incorrect menu selections
- Invalid deletion requests

If the stored JSON file cannot be read, the application starts with an empty expense list instead of stopping unexpectedly.

---

## Main Functions

### `load_expenses()`

Loads saved expense records from `expenses.json`.

It handles missing files, invalid JSON, and file-reading errors.

### `save_expenses()`

Saves the current expense list to the JSON file.

### `get_valid_amount()`

Receives and validates the expense amount.

### `get_valid_date()`

Receives a date in `YYYY-MM-DD` format or automatically uses the current date.

### `add_expense()`

Creates and saves a new expense record.

### `display_expenses()`

Displays all saved expenses and calculates the total amount.

### `display_category_summary()`

Groups expenses by category and calculates category totals.

### `display_monthly_summary()`

Groups expenses by month and calculates monthly totals.

### `get_expense_index()`

Validates the expense number selected by the user.

### `delete_expense()`

Deletes an expense after receiving confirmation.

### `main()`

Controls the application menu and overall execution flow.

---

## Browser-Based Runner Compatibility

The project uses this path-handling logic:

```python
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()
```

This allows the program to work in normal Python files and in some browser-based Python environments where `__file__` is unavailable.

---

## Learning Outcomes

By developing this project, I practised:

- Building a menu-driven Python application
- Organising code into reusable functions
- Working with lists and dictionaries
- Storing structured data using JSON
- Reading and writing files
- Validating numerical input
- Parsing and formatting dates
- Sorting records
- Grouping and summarising data
- Performing financial calculations
- Handling runtime errors
- Using type hints
- Writing maintainable Python code
- Documenting a project professionally
- Managing source code with Git and GitHub

---

## Future Enhancements

Future versions may include:

- Edit an existing expense
- Search expenses
- Filter expenses by date
- Filter expenses by category
- Set monthly budgets
- Display remaining budget
- Warn users when spending exceeds the budget
- Export expenses to CSV
- Import expense records
- Generate weekly and yearly reports
- Add income tracking
- Calculate savings
- Add charts and visual reports
- Store data in an SQL database
- Add user accounts
- Develop a graphical user interface
- Create a Flask or FastAPI backend
- Build a web-based Expense Tracker
- Add automated tests

---

## Repository

The source code is available in:

[Python Mini Projects](https://github.com/ipenetikarthik/python-mini-projects)

---

## Author

### Peneti Karthik

Python Developer focused on practical application development, backend fundamentals, databases, APIs, and continuous learning.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **LinkedIn:** [linkedin.com/in/ipenetikarthik](https://www.linkedin.com/in/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## License

This project is part of the `python-mini-projects` repository and is licensed under the [MIT License](../LICENSE).

---

<p align="center">
  <strong>Thank you for visiting the Python Expense Tracker project.</strong>
</p>

<p align="center">
  Developed by Karthik Peneti
</p>
