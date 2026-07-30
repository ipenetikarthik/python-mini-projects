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

This repository contains Python mini projects developed as part of my continuous software-development learning journey.

Each project focuses on applying programming concepts to practical problems. The projects are organized into separate folders and include source code, instructions, feature explanations, usage examples, and future enhancement ideas.

The repository will continue to grow as I learn new Python, SQL, REST API, automation, testing, and backend-development concepts.
---

## Projects

| No. | Project | Description | Concepts |
|---|---|---|---|
| 01 | [Command-Line Task Manager](./01-task-manager) | A menu-driven application for adding, viewing, completing, deleting and saving tasks | Python, JSON, file handling, functions, exception handling, type hints |
| 02 | [Command-Line Expense Tracker](./02-expense-tracker) | An expense-management application with category-wise and monthly summaries | Python, JSON, datetime, calculations, sorting, validation, exception handling |
| 03 | [Contact Management System](./03-contact-management-system) | A contact manager supporting search, validation, duplicate prevention and complete CRUD operations | Python, JSON, regular expressions, CRUD, validation, TypedDict |
| 04 | [Secure Password Generator](./04-password-generator) | A customizable password generator with secure randomness and strength analysis | Python, secrets, dataclasses, security, validation, password analysis |
| 05 | [Python Quiz Application](./05-quiz-application) | A category-based quiz application with randomized questions, grading, explanations and high-score tracking | Python, JSON, random sampling, dataclasses, TypedDict, validation, file handling |
---

## Project 01: Command-Line Task Manager

The Command-Line Task Manager allows users to:

- Add new tasks
- View pending and completed tasks
- Mark tasks as completed
- Delete tasks
- Save task information in JSON format
- Load saved tasks automatically
- Handle invalid inputs and file-related errors

### Run the project

```bash
cd 01-task-manager
python task_manager.py
```

On some systems:

```bash
python3 task_manager.py
```

Read the complete documentation:

[View Task Manager README](./01-task-manager/README.md)

---

## Project 02: Command-Line Expense Tracker

The Python Expense Tracker is a menu-driven application for recording, viewing, analysing, and deleting expense information.

### Features

- Add expenses with description, category, amount, and date
- Automatically use the current date when no date is entered
- View all saved expense records
- Calculate total spending
- Generate category-wise summaries
- Generate monthly summaries
- Delete expenses with confirmation
- Store records using JSON
- Validate amounts, dates, menu options, and expense numbers
- Handle file and JSON-related errors

### Run the project

```bash
cd 02-expense-tracker
python expense_tracker.py
```

On some systems:

```bash
python3 expense_tracker.py
```

Read the complete documentation:

[View Expense Tracker README](./02-expense-tracker/README.md)

---

## Project 03: Contact Management System

The Contact Management System is a command-line application for creating, organising, searching, updating and deleting contact records.

### Features

- Add contacts with name, phone number, email and address
- View all saved contacts
- Search by name, phone number, email or address
- Edit existing contact details
- Delete contacts with confirmation
- Validate phone numbers and email addresses
- Prevent duplicate phone numbers and email addresses
- Display basic contact statistics
- Store records locally using JSON
- Validate data loaded from JSON
- Handle missing, corrupted and invalid data safely
- Use strict type annotations compatible with Pylance

### Run the project

```bash
cd 03-contact-management-system
python contact_manager.py
```

On some systems:

```bash
python3 contact_manager.py
```

Read the complete documentation:

[View Contact Management System README](./03-contact-management-system/README.md)

---

## Project 04: Secure Password Generator

The Secure Password Generator is a command-line application for creating strong and customizable passwords using cryptographically secure randomness.

It also includes a password-strength checker that evaluates length, character diversity, common patterns, predictable sequences and repeated characters.

### Features

- Generate cryptographically secure passwords
- Customize password length
- Include lowercase letters
- Include uppercase letters
- Include numbers
- Include symbols
- Exclude ambiguous characters
- Generate multiple passwords
- Guarantee inclusion of selected character groups
- Securely shuffle generated characters
- Evaluate password strength
- Detect common password patterns
- Detect alphabetical and numerical sequences
- Detect repeated characters
- Provide security recommendations
- Validate all user inputs
- Use strict Pylance-compatible type annotations

### Run the project

```bash
cd 04-password-generator
python password_generator.py
```

On some systems:

```bash
python3 password_generator.py
```

Read the complete documentation:

[View Secure Password Generator README](./04-password-generator/README.md)

---

## Project 05: Python Quiz Application

The Python Quiz Application is a command-line program that loads multiple-choice questions from JSON and allows users to customize their quiz by category, difficulty and question count.

It provides immediate answer feedback, explanations, score calculation, grading, incorrect-answer review and local high-score tracking.

### Features

- Load questions from a JSON file
- Validate all question records
- Select categories and difficulty levels
- Choose the number of questions
- Randomize questions for every attempt
- Display quiz progress
- Validate answer input
- Show immediate answer feedback
- Display correct-answer explanations
- Calculate score and percentage
- Assign performance grades
- Review incorrect answers
- Store the ten best scores locally
- Reload questions without restarting
- Handle missing and corrupted files
- Use strict Pylance-compatible type annotations

### Run the project

```bash
cd 05-quiz-application
python quiz_app.py
```

On some systems:

```bash
python3 quiz_app.py
```

Read the complete documentation:

[View Python Quiz Application README](./05-quiz-application/README.md)

## Skills Demonstrated

The projects in this repository demonstrate and strengthen knowledge of:

- Python programming fundamentals
- Functions and modular programming
- Lists and dictionaries
- Object-oriented programming
- File handling
- JSON data processing
- Exception handling
- Input validation
- Type hints
- Command-line applications
- SQL and database fundamentals
- REST API concepts
- Git and GitHub
- Project documentation

---

## Repository Structure

```text
python-mini-projects/
│
├── 01-task-manager/
│   ├── task_manager.py
│   └── README.md
│
├── 02-expense-tracker/
│   ├── expense_tracker.py
│   └── README.md
│
├── 03-contact-management-system/
│   ├── contact_manager.py
│   └── README.md
│
├── 04-password-generator/
│   ├── password_generator.py
│   └── README.md
│
├── 05-quiz-application/
│   ├── quiz_app.py
│   ├── questions.json
│   └── README.md
│
├── .gitignore
├── LICENSE
└── README.md
```

Local JSON files such as task data, expense records and quiz high scores are created automatically when required and are excluded from version control where appropriate.
```

JSON data files are created automatically by projects that require persistent local storage. The Password Generator does not save generated passwords.
---

## Planned Projects

More projects will be added gradually, including:

- Library Management System
- Student Record Management System
- Weather API Application
- URL Shortener
- Python Automation Scripts
- Flask REST API
- Database-Based Task Manager
- User Authentication System
---

## Learning Goals

Through these projects, I aim to:

- Write clean and understandable Python code
- Strengthen logical and problem-solving abilities
- Build practical software applications
- Improve SQL and database knowledge
- Learn REST API development
- Understand backend application structure
- Practise debugging and testing
- Use Git and GitHub professionally
- Create a strong Python developer portfolio

---

## How to Use This Repository

Clone the repository:

```bash
git clone https://github.com/ipenetikarthik/python-mini-projects.git
```

Open the repository:

```bash
cd python-mini-projects
```

Select a project folder and follow its individual README instructions.

---

## Contributions and Feedback

Suggestions, improvements, and constructive feedback are welcome.

Each project is developed for learning, practice, and portfolio demonstration. The code will be improved as I gain more experience and learn development best practices.

---

## Author

### Peneti Karthik

Python Developer focused on practical application development, backend fundamentals, databases, APIs, and continuous learning.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## License

This repository is licensed under the [MIT License](./LICENSE).

---

<p align="center">
  <strong>More Python projects will be added soon.</strong>
</p>

<p align="center">
  Developed by Peneti Karthik
</p>
