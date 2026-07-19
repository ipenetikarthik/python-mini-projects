# Python Secure Password Generator

A secure and customizable command-line Password Generator developed using Python.

The application generates strong passwords using cryptographically secure randomness. Users can customize password length, character types, ambiguous-character exclusion, and the number of passwords to generate.

It also includes a password-strength checker that evaluates password length, character diversity, common patterns, repeated characters, and predictable sequences.

---

## Features

- Generate cryptographically secure passwords
- Customize password length
- Include or exclude lowercase letters
- Include or exclude uppercase letters
- Include or exclude numbers
- Include or exclude symbols
- Exclude visually ambiguous characters
- Generate multiple passwords at once
- Guarantee inclusion of every selected character category
- Shuffle passwords securely
- Evaluate password strength
- Detect common and predictable patterns
- Detect alphabetical and numerical sequences
- Detect repeated characters
- Provide password-strength feedback
- Validate all menu and configuration inputs
- Use strict Pylance-compatible type annotations

---

## Security Approach

The project uses Python’s built-in `secrets` module instead of the standard `random` module.

The `secrets` module is designed for generating cryptographically secure values suitable for passwords, authentication tokens, and other security-sensitive information.

```python
secrets.choice(character_pool)
```

The application also uses a secure Fisher–Yates shuffle implementation with:

```python
secrets.randbelow()
```

This helps prevent predictable password generation.

> This project is intended for educational and portfolio purposes. For real accounts, passwords should be stored in a trusted password manager and never reused.

---

## Technologies Used

- Python 3
- Python `secrets` module
- Python `string` module
- Python dataclasses
- Python type hints
- Command-Line Interface
- Git
- GitHub

---

## Python Concepts Demonstrated

This project demonstrates:

- Functions
- Constants using `Final`
- Dataclasses
- Frozen data structures
- Lists, tuples and sets
- Conditional statements
- Loops
- List comprehensions
- Generator expressions
- String manipulation
- Input validation
- Exception handling
- Secure random generation
- Password analysis
- Modular programming
- Type-safe application design
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
└── 04-password-generator/
    │
    ├── password_generator.py
    └── README.md
```

This project does not store generated passwords in a file.

Passwords exist only during the current program execution.

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

### 3. Open the Project Folder

```bash
cd python-mini-projects/04-password-generator
```

---

### 4. Run the Application

```bash
python password_generator.py
```

On some systems:

```bash
python3 password_generator.py
```

---

## Application Menu

After running the application, the following menu appears:

```text
====================================================
        PYTHON SECURE PASSWORD GENERATOR
====================================================
1. Generate secure passwords
2. Check password strength
3. Exit
====================================================
Choose an option from 1 to 3:
```

---

## Generate Secure Passwords

Select:

```text
1
```

The program asks for the following preferences:

- Password length
- Lowercase letters
- Uppercase letters
- Numbers
- Symbols
- Ambiguous-character exclusion
- Number of passwords

Example:

```text
Password length (8-128) [default 16]: 20
Include lowercase letters? (Y/n): y
Include uppercase letters? (Y/n): y
Include numbers? (Y/n): y
Include symbols? (Y/n): y
Exclude ambiguous characters such as 0, O, 1, I and l? (y/N): y
How many passwords should be generated (1-20) [default 1]? 3
```

Example output:

```text
GENERATED PASSWORDS
======================================================================
 1. X9@pR7!vK2#mT6$wQ8&z [Very Strong — 95/100]
 2. H4!sN8@qY6#dP3$kM7&x [Very Strong — 95/100]
 3. V5$gT9!mC2@rL8#nQ7%j [Very Strong — 95/100]
======================================================================
```

Every generated password contains at least one character from each selected character group.

---

## Check Password Strength

Select:

```text
2
```

The program evaluates a sample password.

Do not enter a password currently used for a real account.

Example weak password:

```text
password123
```

Possible result:

```text
PASSWORD STRENGTH
==================================================
Strength                                     Weak
Score                                      30/100
--------------------------------------------------
• Increase the password length.
• Use lowercase letters, uppercase letters, numbers and symbols.
• Avoid common words and predictable patterns.
• Avoid alphabetical or numerical sequences.
==================================================
```

Example stronger password:

```text
R7!mQ2@vL9#xP4$k
```

Possible result:

```text
PASSWORD STRENGTH
==================================================
Strength                              Very Strong
Score                                      95/100
--------------------------------------------------
• This password has strong length and character diversity.
==================================================
```

---

## Password Configuration

The application supports password lengths between:

```text
8 and 128 characters
```

The maximum number of passwords generated in one operation is:

```text
20
```

Supported character groups include:

### Lowercase Letters

```text
abcdefghijklmnopqrstuvwxyz
```

### Uppercase Letters

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### Numbers

```text
0123456789
```

### Symbols

```text
!@#$%^&*()-_=+[]{};:,.?/
```

---

## Ambiguous Characters

Users may exclude characters that can be visually confusing.

Examples include:

```text
0 O o 1 I l |
```

Excluding these characters can improve readability when passwords are copied, typed manually, or communicated visually.

---

## Password Generation Process

The generator follows these steps:

1. Collect the user’s password preferences.
2. Create a list of selected character groups.
3. Remove ambiguous characters when requested.
4. Select at least one character from every chosen group.
5. Generate the remaining characters securely.
6. Combine all generated characters.
7. Shuffle the password using secure randomness.
8. Evaluate the generated password’s strength.
9. Display the password and strength score.

This ensures that every selected character category is represented.

---

## Password Strength Evaluation

The strength checker evaluates:

- Password length
- Lowercase-letter usage
- Uppercase-letter usage
- Number usage
- Symbol usage
- Character diversity
- Common password patterns
- Alphabetical sequences
- Numerical sequences
- Repeated characters

The final score is limited to:

```text
0 to 100
```

Strength labels include:

| Score | Strength |
|---|---|
| 85–100 | Very Strong |
| 70–84 | Strong |
| 50–69 | Moderate |
| 30–49 | Weak |
| 0–29 | Very Weak |

---

## Common Pattern Detection

The application checks for common and predictable text such as:

```text
password
qwerty
admin
welcome
letmein
python
1234
abcd
```

Passwords containing these patterns receive a lower strength score.

---

## Sequence Detection

The program detects common sequences such as:

```text
abcd
dcba
1234
4321
```

Predictable sequences reduce password security and therefore lower the final strength score.

---

## Repeated-Character Detection

The strength checker detects the same character repeated three or more times consecutively.

Examples:

```text
aaa
111
###
```

Repeated characters reduce password diversity and may make a password easier to guess.

---

## Input Validation

The application validates:

- Invalid menu selections
- Non-numeric password lengths
- Password lengths outside the accepted range
- Invalid yes-or-no responses
- Missing character-group selections
- Password lengths shorter than selected groups
- Invalid password-count values
- Empty password-strength input

Users are repeatedly prompted until valid menu and configuration input is entered.

---

## Main Classes

### `PasswordOptions`

Stores password-generation settings.

```python
@dataclass(frozen=True, slots=True)
class PasswordOptions:
    length: int
    include_lowercase: bool
    include_uppercase: bool
    include_digits: bool
    include_symbols: bool
    exclude_ambiguous: bool
```

### `StrengthResult`

Stores the password-strength result.

```python
@dataclass(frozen=True, slots=True)
class StrengthResult:
    score: int
    label: str
    feedback: tuple[str, ...]
```

Using frozen dataclasses prevents accidental modification after creation.

---

## Main Functions

### `get_integer()`

Receives and validates a whole number within an accepted range.

### `get_yes_no()`

Receives and validates yes-or-no input.

### `remove_ambiguous_characters()`

Removes visually confusing characters from a character group.

### `get_character_groups()`

Builds the selected password character groups.

### `secure_shuffle()`

Securely shuffles generated password characters.

### `generate_password()`

Generates one password using selected options.

### `generate_passwords()`

Generates multiple passwords.

### `contains_sequence()`

Detects alphabetical and numerical sequences.

### `contains_repeated_characters()`

Detects consecutive repeated characters.

### `evaluate_password_strength()`

Calculates the password-strength score and feedback.

### `collect_password_options()`

Collects password-generation preferences from the user.

### `display_strength_result()`

Displays the password score, label and recommendations.

### `generate_password_flow()`

Controls the complete password-generation workflow.

### `check_password_flow()`

Controls the password-strength-checking workflow.

### `main()`

Controls the application menu and execution flow.

---

## Pylance Type Safety

The application uses strict type annotations, `Final` constants and typed dataclasses.

Example constants:

```python
MIN_PASSWORD_LENGTH: Final[int] = 8
MAX_PASSWORD_LENGTH: Final[int] = 128
MAX_PASSWORD_COUNT: Final[int] = 20
```

Example function annotation:

```python
def generate_password(
    options: PasswordOptions,
) -> str:
```

These annotations improve readability, maintainability and compatibility with strict Pylance checking.

---

## Learning Outcomes

By developing this project, I practised:

- Generating secure random values
- Understanding the difference between `random` and `secrets`
- Designing customizable command-line workflows
- Validating numerical and yes-or-no input
- Working with dataclasses
- Using immutable configuration objects
- Managing multiple character groups
- Implementing a secure shuffle algorithm
- Analysing password strength
- Detecting common patterns and sequences
- Providing useful security feedback
- Writing modular and reusable functions
- Applying strict Python type annotations
- Creating professional project documentation
- Managing source code with Git and GitHub

---

## Future Enhancements

Future versions may include:

- Copy generated passwords to the clipboard
- Generate memorable passphrases
- Add custom character sets
- Add password-generation profiles
- Export generated passwords securely
- Estimate password-cracking time
- Check passwords against breached-password databases
- Add graphical password-strength indicators
- Add a desktop graphical interface
- Build a web-based password generator
- Create a Flask or FastAPI backend
- Add automated unit tests
- Package the application as a Python module
- Create a browser extension

---

## Repository

The complete source code is available in:

[Python Mini Projects](https://github.com/ipenetikarthik/python-mini-projects)

---

## Author

### Peneti Karthik

Python Developer focused on practical application development, backend fundamentals, databases, APIs, security and continuous learning.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **LinkedIn:** [linkedin.com/in/ipenetikarthik](https://www.linkedin.com/in/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## License

This project is part of the `python-mini-projects` repository and is licensed under the [MIT License](../LICENSE).

---

<p align="center">
  <strong>Thank you for visiting the Python Secure Password Generator project.</strong>
</p>

<p align="center">
  Developed by Peneti Karthik
</p>
