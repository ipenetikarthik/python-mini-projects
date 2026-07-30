# Python Mini Projects

<p align="center">
  A growing collection of practical Python projects created to strengthen programming, problem-solving, file-handling, database, API, and backend-development skills.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Projects-Learning%20Portfolio-brightgreen" alt="Portfolio">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License">
</p>
---

## About This Repository

This repository contains practical Python mini projects developed to strengthen programming fundamentals, problem-solving, database knowledge, application design and professional software-development practices.

The projects progress from beginner-friendly command-line applications using JSON storage to a database-driven Inventory Management System using SQLite, SQL relationships, transactions, reports and CSV exports.

Each project focuses on:

- Clear and readable Python code
- Practical problem-solving
- Input validation
- Exception handling
- Persistent data storage
- Modular programming
- Type annotations
- Professional documentation
- Git and GitHub workflows
- Continuous learning

---

## Completed Projects

| No. | Project | Main Concepts | Storage | Folder |
|:---:|---|---|---|---|
| 01 | Command-Line Task Manager | CRUD, functions, validation, file handling | JSON | [`01-task-manager`](01-task-manager/) |
| 02 | Expense Tracker | Transactions, summaries, dates, categories | JSON | [`02-expense-tracker`](02-expense-tracker/) |
| 03 | Contact Management System | CRUD, regex, search, duplicate prevention | JSON | [`03-contact-management-system`](03-contact-management-system/) |
| 04 | Secure Password Generator | `secrets`, dataclasses, password analysis | Runtime only | [`04-password-generator`](04-password-generator/) |
| 05 | Python Quiz Application | Question loading, scoring, menus, high scores | JSON | [`05-quiz-application`](05-quiz-application/) |
| 06 | Inventory Management System | SQLite, SQL, transactions, stock and sales | SQLite and CSV | [`06-inventory-management-system`](06-inventory-management-system/) |

---

## Project 01 — Command-Line Task Manager

A menu-driven application for organising and tracking daily tasks.

### Features

- Add tasks
- View saved tasks
- Mark tasks as completed
- Delete tasks
- Store data in JSON
- Validate user input
- Handle missing or invalid files

### Run

```bash
cd 01-task-manager
python task_manager.py
```

[Open Project 01](01-task-manager/)

---

## Project 02 — Expense Tracker

A command-line application for recording expenses and analysing spending.

### Features

- Add expenses
- Record description, category, amount and date
- View all expenses
- Calculate total spending
- Generate category summaries
- Generate monthly summaries
- Delete expenses with confirmation
- Store records in JSON

### Run

```bash
cd 02-expense-tracker
python expense_tracker.py
```

[Open Project 02](02-expense-tracker/)

---

## Project 03 — Contact Management System

A complete contact-management application with validation and persistent storage.

### Features

- Add, view, search, update and delete contacts
- Store name, phone, email and location
- Validate phone numbers
- Validate email addresses using regular expressions
- Prevent duplicate contacts
- Display contact statistics
- Store data in JSON

### Run

```bash
cd 03-contact-management-system
python contact_manager.py
```

[Open Project 03](03-contact-management-system/)

---

## Project 04 — Secure Password Generator

A secure and customizable password generator developed using Python's cryptographically secure `secrets` module.

### Features

- Generate secure passwords
- Configure password length and character groups
- Exclude ambiguous characters
- Generate multiple passwords
- Guarantee selected character-group inclusion
- Securely shuffle generated passwords
- Evaluate password strength
- Detect common patterns, sequences and repeated characters

### Run

```bash
cd 04-password-generator
python password_generator.py
```

[Open Project 04](04-password-generator/)

---

## Project 05 — Python Quiz Application

A menu-driven quiz application that loads questions, evaluates answers and tracks performance.

### Features

- Start a quiz
- Load questions from stored data
- Display multiple-choice questions
- Validate answers
- Calculate the final score
- Store and display high scores
- Reload questions
- Handle missing or invalid question data

### Run

```bash
cd 05-quiz-application
python quiz.py
```

[Open Project 05](05-quiz-application/)

---

## Project 06 — Inventory Management System

A professional command-line Inventory Management System developed using Python and SQLite.

This project marks the transition from JSON-based applications to a relational, database-driven system.

### Product Management

- Add products
- View all products
- Search by ID, SKU, name, category or supplier
- Update product details
- Adjust stock quantities
- Delete eligible products
- Prevent duplicate SKUs

### Stock and Sales

- Add opening stock
- Restock products
- Record sales
- Validate stock availability
- Prevent sales above available quantity
- Automatically reduce inventory
- Track every stock movement

### Reports and Exports

- Inventory summary
- Inventory-value calculation
- Low-stock report
- Category-wise summary
- Top-selling products
- Stock-movement history
- Product CSV export
- Sales CSV export

### Database Concepts

- SQLite database creation
- SQL CRUD operations
- Primary and foreign keys
- Constraints and indexes
- SQL joins
- Aggregate functions
- Database transactions
- Relational data modelling

### Run

```bash
cd 06-inventory-management-system
python inventory_management.py
```

[Open Project 06](06-inventory-management-system/)

---

## Project Progression

```text
01 Task Manager
       ↓
02 Expense Tracker
       ↓
03 Contact Management System
       ↓
04 Secure Password Generator
       ↓
05 Quiz Application
       ↓
06 Inventory Management System
```

The series demonstrates progress across:

1. Python fundamentals and application flow
2. JSON file handling and persistent storage
3. CRUD operations and data validation
4. Security-focused programming
5. Quiz processing and score management
6. SQLite databases, SQL relationships and transactions

---

## Repository Structure

```text
python-mini-projects/
│
├── 01-task-manager/
│   ├── task_manager.py
│   ├── tasks.json
│   └── README.md
│
├── 02-expense-tracker/
│   ├── expense_tracker.py
│   ├── expenses.json
│   └── README.md
│
├── 03-contact-management-system/
│   ├── contact_manager.py
│   ├── contacts.json
│   └── README.md
│
├── 04-password-generator/
│   ├── password_generator.py
│   └── README.md
│
├── 05-quiz-application/
│   ├── quiz.py
│   ├── questions.json
│   ├── high_scores.json
│   └── README.md
│
├── 06-inventory-management-system/
│   ├── inventory_management.py
│   ├── README.md
│   ├── requirements.txt
│   ├── database/
│   │   └── inventory.db
│   ├── exports/
│   └── screenshots/
│
├── LICENSE
└── README.md
```

Some JSON or database files are generated automatically when their applications run.

---

## Technologies Used

### Programming Language

- Python 3

### Data Storage

- JSON
- SQLite
- CSV

### Python Standard-Library Modules

- `json`
- `csv`
- `sqlite3`
- `secrets`
- `string`
- `re`
- `datetime`
- `decimal`
- `pathlib`
- `dataclasses`
- `typing`

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Pylance

---

## Skills Demonstrated

- Python fundamentals
- Data structures
- Functions and modular programming
- File handling
- JSON data processing
- SQLite integration
- SQL CRUD operations
- Relational database design
- SQL joins and aggregate functions
- Database transactions
- Regular expressions
- Secure random generation
- Date and time handling
- Decimal-based currency calculations
- Search, filtering and sorting
- Input validation
- Exception handling
- CSV report generation
- Type annotations
- Dataclasses
- Documentation
- Version control

---

## Installation

### 1. Install Python

Python 3.10 or later is recommended.

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/ipenetikarthik/python-mini-projects.git
```

### 3. Open the Repository

```bash
cd python-mini-projects
```

### 4. Open and Run a Project

Example:

```bash
cd 06-inventory-management-system
python inventory_management.py
```

On Windows:

```bash
py inventory_management.py
```

---

## Requirements

The completed projects currently use only modules included in the Python standard library.

No third-party package installation is required.

---

## Project Status

| Project | Status |
|---|:---:|
| Command-Line Task Manager | ✅ Completed |
| Expense Tracker | ✅ Completed |
| Contact Management System | ✅ Completed |
| Secure Password Generator | ✅ Completed |
| Python Quiz Application | ✅ Completed |
| Inventory Management System | ✅ Completed |

**Total completed projects: 6**

---

## Learning Approach

```text
Learn → Build → Test → Document → Commit → Share → Improve
```

Every project supports:

- Consistency
- Discipline
- Accountability
- Problem-solving
- Code quality
- Documentation
- Continuous improvement

> Success is not built in a single day. It is built through consistency, discipline and accountability.

---

## Future Direction

Future projects may explore:

- Object-oriented application architecture
- Automated testing
- Logging
- REST APIs with FastAPI
- Authentication and authorization
- Advanced SQL
- Data analysis
- Desktop applications
- Web applications
- Deployment
- Backend development

---

## Author

### Peneti Karthik

Python Developer focused on practical application development, backend fundamentals, databases, APIs, automation and continuous learning.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **LinkedIn:** [linkedin.com/in/ipenetikarthik](https://www.linkedin.com/in/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## License

This repository is licensed under the [MIT License](LICENSE).

---

<div align="center">

### Thank you for visiting the Python Mini Projects repository.

**Developed by Peneti Karthik**

</div>
