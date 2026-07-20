# Python Quiz Application

A command-line Quiz Application developed using Python.

The application loads multiple-choice questions from a JSON file and allows users to select a category, difficulty level and number of questions. It provides immediate answer feedback, explanations, score calculation, grading, incorrect-answer review and high-score storage.

---

## Features

- Load quiz questions from JSON
- Validate question records before use
- Select a quiz category
- Select a difficulty level
- Choose the number of questions
- Randomize questions for every attempt
- Display quiz progress
- Validate answer input
- Show immediate correct or incorrect feedback
- Display the correct answer
- Provide an explanation for every question
- Calculate the final score
- Calculate the final percentage
- Assign a performance grade
- Review incorrectly answered questions
- Save high scores locally
- Display the top ten high scores
- Reload questions without restarting the application
- Handle missing and invalid JSON files safely
- Use strict Pylance-compatible type annotations

---

## Technologies Used

- Python 3
- JSON
- Python `random` module
- Python `datetime` module
- Python dataclasses
- Python `pathlib`
- Python type hints
- Git
- GitHub

---

## Question Categories

The application currently contains questions from:

- Python
- SQL
- Git
- REST API
- Programming Fundamentals
- Data Structures

---

## Difficulty Levels

Each category contains questions with the following difficulty levels:

```text
Easy
Medium
Hard
```

Users may also select:

```text
All Difficulties
```

---

## Project Structure

```text
05-quiz-application/
│
├── quiz_app.py
├── questions.json
├── README.md
└── high_scores.json
```

The `high_scores.json` file is created automatically after completing the first quiz.

It stores local quiz results and should not be committed to GitHub.

---

## Installation

### 1. Install Python

Check whether Python 3 is installed:

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

### 3. Open the Project Folder

```bash
cd python-mini-projects/05-quiz-application
```

---

### 4. Run the Application

```bash
python quiz_app.py
```

On some systems:

```bash
python3 quiz_app.py
```

---

## Application Menu

After starting the program, the following menu appears:

```text
==========================================================
              PYTHON QUIZ APPLICATION
==========================================================
1. Start Quiz
2. View High Scores
3. Reload Questions
4. Exit
==========================================================
Choose an option from 1 to 4:
```

---

## Starting a Quiz

Select:

```text
1
```

The program asks for:

- Player name
- Category
- Difficulty level
- Number of questions

Example:

```text
Enter your name: Peneti Karthik

SELECT A CATEGORY
-------------------------------------------------------
1. All Categories
2. Data Structures
3. Git
4. Programming Fundamentals
5. Python
6. REST API
7. SQL
```

The quiz questions are selected randomly from the available records matching the chosen category and difficulty.

---

## Question Format

Each question displays:

- Current question number
- Total number of questions
- Progress percentage
- Category
- Difficulty
- Question
- Four answer options

Example:

```text
======================================================================
Question 1/4 (25% complete)
Category: Python | Difficulty: Hard
----------------------------------------------------------------------
Which Python feature produces values lazily instead of storing all
values in memory at once?

1. Generator
2. Dictionary
3. Decorator
4. Class variable
======================================================================
Enter your answer from 1 to 4:
```

---

## Answer Feedback

When the selected answer is correct:

```text
Correct! ✅
Explanation: Generators yield values one at a time and can reduce
memory usage.
```

When the selected answer is incorrect:

```text
Incorrect. ❌
Correct answer: Generator
Explanation: Generators yield values one at a time and can reduce
memory usage.
```

---

## Quiz Result

After completing the quiz, the application displays:

- Player name
- Correct answers
- Incorrect answers
- Total questions
- Percentage
- Grade
- Performance message

Example:

```text
======================================================================
                           QUIZ RESULT
======================================================================
Player                                                Peneti Karthik
Correct Answers                                                    3
Incorrect Answers                                                  1
Total Questions                                                    4
Percentage                                                    75.00%
Grade                                                              B
======================================================================
Good work! Review the incorrect answers and continue practising.
```

---

## Grading System

| Percentage | Grade |
|---|---|
| 90–100% | A+ |
| 80–89.99% | A |
| 70–79.99% | B |
| 60–69.99% | C |
| 50–59.99% | D |
| Below 50% | Needs Improvement |

---

## Incorrect-Answer Review

After displaying the final result, the application shows every incorrectly answered question.

The review includes:

- Question
- Player’s answer
- Correct answer
- Explanation

When the player receives a perfect score, the application displays:

```text
Perfect score! There are no incorrect answers to review.
```

---

## High Scores

Select:

```text
2
```

The application displays the ten best quiz attempts.

Each record contains:

- Rank
- Player name
- Score
- Percentage
- Grade
- Completion date and time

High scores are sorted by:

1. Percentage
2. Number of correct answers

Only the best ten records are retained.

---

## Question Storage

Questions are stored in:

```text
questions.json
```

Each question follows this structure:

```json
{
    "id": 1,
    "category": "Python",
    "difficulty": "Easy",
    "question": "Which keyword is used to define a function in Python?",
    "options": [
        "function",
        "define",
        "def",
        "func"
    ],
    "correct_answer": 3,
    "explanation": "Python uses the def keyword to define a function."
}
```

The `correct_answer` value represents the option number, beginning from `1`.

---

## Question Validation

Every question loaded from JSON is validated before being used.

The application checks:

- Question ID
- Category
- Difficulty
- Question text
- Number of answer options
- Correct-answer range
- Explanation
- Data types
- Empty values

Invalid question records are ignored safely.

---

## High-Score Storage

High scores are stored locally in:

```text
high_scores.json
```

Each record contains:

```json
{
    "player_name": "Peneti Karthik",
    "score": 3,
    "total_questions": 4,
    "percentage": 75.0,
    "grade": "B",
    "category": "Python",
    "difficulty": "All Difficulties",
    "completed_at": "20-07-2026 10:30 AM"
}
```

The file is generated automatically and is not required to run the project for the first time.

---

## Input Validation

The application validates:

- Empty player names
- Invalid menu selections
- Non-numeric input
- Invalid category selections
- Invalid difficulty selections
- Invalid question counts
- Answer values outside `1–4`
- Missing question files
- Invalid JSON syntax
- Invalid question records
- Corrupted high-score records

The application asks the user to enter a valid value instead of closing unexpectedly.

---

## Main Data Structures

### `Question`

The `Question` TypedDict defines the structure of a quiz question:

```python
class Question(TypedDict):
    id: int
    category: str
    difficulty: str
    question: str
    options: list[str]
    correct_answer: int
    explanation: str
```

### `HighScoreEntry`

The `HighScoreEntry` TypedDict defines a stored quiz result:

```python
class HighScoreEntry(TypedDict):
    player_name: str
    score: int
    total_questions: int
    percentage: float
    grade: str
    category: str
    difficulty: str
    completed_at: str
```

### `AnswerResult`

The immutable `AnswerResult` dataclass stores the result of one answered question:

```python
@dataclass(frozen=True, slots=True)
class AnswerResult:
    question: str
    selected_answer: str
    correct_answer: str
    is_correct: bool
    explanation: str
```

---

## Main Functions

### `load_questions()`

Loads and validates questions from `questions.json`.

### `parse_question()`

Validates one raw question record.

### `filter_questions()`

Filters questions according to the selected category and difficulty.

### `ask_question()`

Displays one question, validates the answer and returns the result.

### `calculate_grade()`

Calculates the grade based on the final percentage.

### `display_quiz_summary()`

Displays the player’s final score, percentage and grade.

### `display_answer_review()`

Displays incorrectly answered questions with explanations.

### `save_high_score()`

Stores the completed quiz result and retains the top ten entries.

### `display_high_scores()`

Displays the high-score leaderboard.

### `start_quiz()`

Controls the complete quiz workflow.

### `main()`

Controls the application menu.

---

## Python Concepts Demonstrated

This project demonstrates:

- Functions
- Lists
- Dictionaries
- Sets
- Tuples
- Loops
- Conditional statements
- List comprehensions
- Generator expressions
- JSON file handling
- Input validation
- Exception handling
- Random sampling
- Sorting
- Percentage calculation
- Dataclasses
- `TypedDict`
- `Final` constants
- Type casting
- Path handling
- Date and time formatting
- Modular programming
- Strict type-safe development

---

## Learning Outcomes

By developing this project, I practised:

- Designing a menu-driven Python application
- Loading structured data from JSON
- Validating external JSON records
- Randomly selecting quiz questions
- Filtering data by category and difficulty
- Calculating scores and percentages
- Implementing a grading system
- Providing immediate answer feedback
- Creating an incorrect-answer review
- Saving and sorting high scores
- Handling missing and corrupted files
- Using dataclasses and TypedDict
- Writing modular and reusable functions
- Applying strict Pylance-compatible type annotations
- Creating professional GitHub documentation

---

## Future Enhancements

Future versions may include:

- Quiz time limits
- Countdown timer
- Negative marking
- Multiple quiz modes
- Player accounts
- Category-wise high scores
- Difficulty-wise analytics
- Question import and export
- Administrator question management
- SQLite database storage
- Automated unit tests
- Desktop graphical interface
- Flask or FastAPI backend
- React web application
- Online multiplayer quizzes
- Question images
- Achievement badges
- Performance charts

---

## Repository

The complete source code is available in:

[Python Mini Projects](https://github.com/ipenetikarthik/python-mini-projects)

---

## Author

### Peneti Karthik

Python Developer focused on practical application development, backend fundamentals, databases, APIs and continuous learning.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **LinkedIn:** [linkedin.com/in/ipenetikarthik](https://www.linkedin.com/in/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## License

This project is part of the `python-mini-projects` repository and is licensed under the [MIT License](../LICENSE).

---

<p align="center">
  <strong>Thank you for visiting the Python Quiz Application project.</strong>
</p>

<p align="center">
  Developed by Peneti Karthik
</p>
