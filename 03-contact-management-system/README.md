# Python Command-Line Contact Management System

A practical command-line Contact Management System developed using Python.

The application allows users to create, view, search, edit, and delete contact records while storing the information locally in a JSON file. It also validates phone numbers and email addresses, prevents duplicate records, and provides basic contact statistics.

This project demonstrates Python programming, JSON file handling, regular expressions, input validation, searching, exception handling, type hints, `TypedDict`, and modular application design.

---

## Features

- Add new contacts
- View all saved contacts
- Search contacts by:
  - Name
  - Phone number
  - Email address
  - Address
- Edit existing contacts
- Delete contacts with confirmation
- Store contact records in JSON format
- Load previously saved contacts automatically
- Validate phone numbers
- Validate email addresses
- Prevent duplicate phone numbers
- Prevent duplicate email addresses
- Allow optional email and address fields
- Display contact statistics
- Handle missing and corrupted JSON files
- Use strict type annotations compatible with Pylance

---

## Technologies Used

- Python 3
- JSON
- Regular expressions
- Python `pathlib`
- Python `typing`
- Command-Line Interface
- Git
- GitHub

---

## Python Concepts Demonstrated

This project demonstrates:

- Variables and data types
- Functions
- Lists and dictionaries
- `TypedDict`
- Conditional statements
- Loops
- User input
- String operations
- List comprehensions
- Generator expressions
- Regular expressions
- File handling
- JSON serialization and deserialization
- Exception handling
- Input validation
- Searching and filtering
- Duplicate-record detection
- Type hints
- Constants using `Final`
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
└── 03-contact-management-system/
    │
    ├── contact_manager.py
    ├── contacts.json
    └── README.md
```

The `contacts.json` file is created automatically after the first contact is saved successfully.

---

## Contact Data Structure

Each contact is stored with the following fields:

```json
{
    "name": "Karthik Peneti",
    "phone": "9876543210",
    "email": "karthik@example.com",
    "address": "Hyderabad, Telangana"
}
```

The contact fields are:

- `name`: Contact's full name
- `phone`: Contact's phone number
- `email`: Contact's email address
- `address`: Contact's address

Email and address are optional, but name and phone number are required.

---

## Installation

### 1. Install Python

Make sure Python 3 is installed.

Check the Python version:

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
cd python-mini-projects/03-contact-management-system
```

---

### 4. Run the Application

```bash
python contact_manager.py
```

On some systems:

```bash
python3 contact_manager.py
```

---

## Application Menu

After running the program, the following menu appears:

```text
==================================================
       PYTHON CONTACT MANAGEMENT SYSTEM
==================================================
1. View all contacts
2. Add a new contact
3. Search contacts
4. Edit a contact
5. Delete a contact
6. View contact statistics
7. Exit
==================================================
Choose an option from 1 to 7:
```

---

## How to Use the Application

### 1. View All Contacts

Select:

```text
1
```

The application displays all saved contacts in a table.

Example:

```text
CONTACT LIST
=========================================================================================================
No.   Name                    Phone             Email                         Address
---------------------------------------------------------------------------------------------------------
1     Karthik Peneti          9876543210        karthik@example.com           Hyderabad, Telangana
=========================================================================================================
```

---

### 2. Add a New Contact

Select:

```text
2
```

Enter the requested contact information.

Example:

```text
Enter the name: Karthik Peneti
Enter the phone number: 9876543210
Enter the email address or press Enter to skip: karthik@example.com
Enter the address or press Enter to skip: Hyderabad, Telangana
```

After successful validation:

```text
Contact added successfully.
```

---

### 3. Search Contacts

Select:

```text
3
```

Enter any part of a:

- Name
- Phone number
- Email address
- Address

Example:

```text
Enter a name, phone, email, or address to search: Karthik
```

The search is case-insensitive and supports partial matches.

---

### 4. Edit a Contact

Select:

```text
4
```

The application displays the saved contacts.

Enter the contact number that you want to edit.

Example:

```text
Enter the contact number: 1
```

The current values are displayed:

```text
Name [Karthik Peneti]:
Phone [9876543210]:
Email [karthik@example.com]:
Address [Hyderabad, Telangana]:
```

Press Enter without typing anything to retain the current value.

---

### 5. Delete a Contact

Select:

```text
5
```

Enter the contact number to delete.

Example:

```text
Enter the contact number: 1
Delete 'Karthik Peneti'? (y/n): y
```

After confirmation:

```text
Deleted contact: Karthik Peneti
```

Entering `n` cancels the deletion.

---

### 6. View Contact Statistics

Select:

```text
6
```

The application displays:

- Total number of contacts
- Contacts containing an email address
- Contacts containing an address

Example:

```text
CONTACT STATISTICS
=============================================
Total contacts                               5
Contacts with email                          4
Contacts with address                        3
=============================================
```

---

### 7. Exit the Application

Select:

```text
7
```

The application closes safely.

```text
Thank you for using the Python Contact Management System.
```

---

## Phone Number Validation

Phone numbers are validated after removing non-numeric characters.

The application accepts phone numbers containing between:

```text
7 and 15 digits
```

Examples of accepted input:

```text
9876543210
+91 98765 43210
040-12345678
```

The application compares normalised phone numbers to prevent duplicates.

---

## Email Validation

Email addresses are validated using a regular expression.

Example of a valid email:

```text
karthik@example.com
```

Email addresses are optional. A user may press Enter to skip the email field.

---

## Duplicate Prevention

The application prevents:

- Duplicate phone numbers
- Duplicate email addresses

Phone numbers are normalised before comparison.

Email addresses are compared without considering uppercase or lowercase differences.

During editing, the selected contact's existing details are excluded from duplicate checks.

---

## JSON Data Validation

When contacts are loaded from `contacts.json`, every record is validated.

A valid record must contain:

- A non-empty name
- A valid phone number
- A valid or empty email
- A valid string address

Invalid records are ignored instead of causing the application to stop unexpectedly.

Example message:

```text
Ignored 2 invalid contact record(s).
```

---

## Error Handling

The application handles:

- Missing JSON files
- Invalid JSON content
- File-reading errors
- File-writing errors
- Empty names
- Invalid phone numbers
- Invalid email addresses
- Duplicate phone numbers
- Duplicate email addresses
- Invalid menu selections
- Non-numeric contact numbers
- Contact numbers outside the available range
- Empty search queries
- Cancelled deletion operations

---

## Main Functions

### `get_base_dir()`

Returns the directory containing the Python file.

### `normalize_phone()`

Removes all non-numeric characters from a phone number.

### `is_valid_phone()`

Checks whether a phone number contains between 7 and 15 digits.

### `is_valid_email()`

Validates an email address using a regular expression.

### `parse_contact()`

Validates one contact record loaded from JSON.

### `load_contacts()`

Loads and validates contacts from `contacts.json`.

### `save_contacts()`

Saves the current contact list to the JSON file.

### `phone_exists()`

Checks whether a phone number already exists.

### `email_exists()`

Checks whether an email address already exists.

### `display_contacts()`

Displays all contacts or selected search results in a table.

### `get_contact_index()`

Receives and validates a contact number.

### `add_contact()`

Creates and saves a new contact.

### `search_contacts()`

Searches contacts using multiple fields.

### `edit_contact()`

Updates an existing contact while preserving unchanged values.

### `delete_contact()`

Deletes a selected contact after confirmation.

### `display_statistics()`

Displays basic contact statistics.

### `main()`

Controls the application menu and execution flow.

---

## Pylance Type Safety

The project uses a `TypedDict` to define the structure of each contact:

```python
class Contact(TypedDict):
    name: str
    phone: str
    email: str
    address: str
```

Constants are declared using `Final`:

```python
BASE_DIR: Final[Path] = get_base_dir()
DATA_FILE: Final[Path] = BASE_DIR / "contacts.json"
```

This improves code clarity and prevents partially unknown type errors in strict Pylance mode.

---

## Learning Outcomes

By developing this project, I practised:

- Building a complete CRUD application
- Organising code into reusable functions
- Managing structured records with `TypedDict`
- Reading and writing JSON files
- Validating phone numbers
- Validating email addresses
- Using regular expressions
- Searching across multiple fields
- Editing existing records
- Preventing duplicate records
- Handling invalid data safely
- Writing strict type-safe Python code
- Designing menu-driven applications
- Creating professional project documentation
- Managing source code using Git and GitHub

---

## Future Enhancements

Future versions may include:

- Contact categories
- Favourite contacts
- Contact profile pictures
- Date-of-birth fields
- Company and job-title fields
- Import contacts from CSV
- Export contacts to CSV
- Sort contacts alphabetically
- Filter contacts by category
- Contact groups
- Automatic data backup
- Restore deleted contacts
- SQL database storage
- User accounts
- Password protection
- Graphical user interface
- Flask or FastAPI backend
- Web-based contact manager
- Automated unit tests

---

## Repository

The complete source code is available in:

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
  <strong>Thank you for visiting the Python Contact Management System project.</strong>
</p>

<p align="center">
  Developed by Karthik Peneti
</p>
