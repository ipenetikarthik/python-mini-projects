import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# Supports normal Python files and browser-based Python runners.
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()

DATA_FILE = BASE_DIR / "expenses.json"


def load_expenses() -> list[dict[str, Any]]:
    """Load saved expenses from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Invalid expense data found. Starting with an empty list.")
        return []

    except json.JSONDecodeError:
        print("The expenses file contains invalid JSON.")
        print("Starting with an empty expense list.")
        return []

    except OSError as error:
        print(f"Unable to read the expenses file: {error}")
        return []


def save_expenses(expenses: list[dict[str, Any]]) -> bool:
    """Save expenses to the JSON file."""

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                expenses,
                file,
                indent=4,
                ensure_ascii=False,
            )

        return True

    except OSError as error:
        print(f"Unable to save expenses: {error}")
        return False


def get_valid_amount() -> Optional[float]:
    """Receive and validate an expense amount."""

    value = input("Enter the amount: ₹").strip()

    try:
        amount = float(value)
    except ValueError:
        print("Please enter a valid numeric amount.")
        return None

    if amount <= 0:
        print("The amount must be greater than zero.")
        return None

    return round(amount, 2)


def get_valid_date() -> Optional[str]:
    """Receive and validate a date in YYYY-MM-DD format."""

    date_value = input(
        "Enter the date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if not date_value:
        return datetime.now().strftime("%Y-%m-%d")

    try:
        valid_date = datetime.strptime(date_value, "%Y-%m-%d")
        return valid_date.strftime("%Y-%m-%d")

    except ValueError:
        print("Invalid date. Please use the YYYY-MM-DD format.")
        return None


def add_expense(expenses: list[dict[str, Any]]) -> None:
    """Add a new expense."""

    print("\nADD NEW EXPENSE")
    print("-" * 45)

    description = input("Enter the description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    category = input("Enter the category: ").strip().title()

    if not category:
        print("Category cannot be empty.")
        return

    amount = get_valid_amount()

    if amount is None:
        return

    expense_date = get_valid_date()

    if expense_date is None:
        return

    new_expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": expense_date,
    }

    expenses.append(new_expense)

    if save_expenses(expenses):
        print("\nExpense added successfully.")
    else:
        expenses.pop()
        print("The expense could not be saved.")


def display_expenses(expenses: list[dict[str, Any]]) -> None:
    """Display all recorded expenses."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: str(expense.get("date", "")),
        reverse=True,
    )

    print("\nALL EXPENSES")
    print("=" * 82)
    print(
        f"{'No.':<5}"
        f"{'Date':<14}"
        f"{'Category':<18}"
        f"{'Description':<28}"
        f"{'Amount':>15}"
    )
    print("-" * 82)

    total = 0.0

    for index, expense in enumerate(sorted_expenses, start=1):
        amount = float(expense.get("amount", 0))
        total += amount

        date = str(expense.get("date", "Unknown"))
        category = str(expense.get("category", "Other"))
        description = str(expense.get("description", "Untitled"))

        print(
            f"{index:<5}"
            f"{date:<14}"
            f"{category[:16]:<18}"
            f"{description[:26]:<28}"
            f"₹{amount:>13.2f}"
        )

    print("-" * 82)
    print(f"{'Total Expenses':<67}₹{total:>13.2f}")
    print("=" * 82)


def display_category_summary(
    expenses: list[dict[str, Any]],
) -> None:
    """Display total expenses grouped by category."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    category_totals: dict[str, float] = {}

    for expense in expenses:
        category = str(expense.get("category", "Other"))
        amount = float(expense.get("amount", 0))

        category_totals[category] = (
            category_totals.get(category, 0.0) + amount
        )

    print("\nCATEGORY SUMMARY")
    print("=" * 50)
    print(f"{'Category':<32}{'Amount':>18}")
    print("-" * 50)

    grand_total = 0.0

    for category, amount in sorted(category_totals.items()):
        grand_total += amount
        print(f"{category[:30]:<32}₹{amount:>16.2f}")

    print("-" * 50)
    print(f"{'Grand Total':<32}₹{grand_total:>16.2f}")
    print("=" * 50)


def display_monthly_summary(
    expenses: list[dict[str, Any]],
) -> None:
    """Display total expenses grouped by month."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    monthly_totals: dict[str, float] = {}

    for expense in expenses:
        date_value = str(expense.get("date", ""))

        try:
            parsed_date = datetime.strptime(
                date_value,
                "%Y-%m-%d",
            )
            month = parsed_date.strftime("%B %Y")
        except ValueError:
            month = "Unknown Date"

        amount = float(expense.get("amount", 0))

        monthly_totals[month] = (
            monthly_totals.get(month, 0.0) + amount
        )

    print("\nMONTHLY SUMMARY")
    print("=" * 50)
    print(f"{'Month':<32}{'Amount':>18}")
    print("-" * 50)

    grand_total = 0.0

    for month, amount in monthly_totals.items():
        grand_total += amount
        print(f"{month:<32}₹{amount:>16.2f}")

    print("-" * 50)
    print(f"{'Grand Total':<32}₹{grand_total:>16.2f}")
    print("=" * 50)


def get_expense_index(
    expenses: list[dict[str, Any]],
) -> Optional[int]:
    """Receive and validate an expense number."""

    try:
        expense_number = int(
            input("\nEnter the expense number: ").strip()
        )
    except ValueError:
        print("Please enter a valid number.")
        return None

    if expense_number < 1 or expense_number > len(expenses):
        print(
            f"Please enter a number between 1 and {len(expenses)}."
        )
        return None

    return expense_number - 1


def delete_expense(expenses: list[dict[str, Any]]) -> None:
    """Delete a selected expense."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    print("\nEXPENSES")
    print("-" * 70)

    for index, expense in enumerate(expenses, start=1):
        description = str(
            expense.get("description", "Untitled")
        )
        amount = float(expense.get("amount", 0))
        date = str(expense.get("date", "Unknown"))

        print(
            f"{index}. {description} | "
            f"{date} | ₹{amount:.2f}"
        )

    expense_index = get_expense_index(expenses)

    if expense_index is None:
        return

    selected_expense = expenses[expense_index]

    confirmation = input(
        f"Delete '{selected_expense.get('description')}'? "
        "(y/n): "
    ).strip().lower()

    if confirmation not in {"y", "yes"}:
        print("Deletion cancelled.")
        return

    removed_expense = expenses.pop(expense_index)

    if save_expenses(expenses):
        print(
            "Deleted expense: "
            f"{removed_expense.get('description', 'Untitled')}"
        )
    else:
        expenses.insert(expense_index, removed_expense)
        print("The expense could not be deleted.")


def main() -> None:
    """Run the Expense Tracker application."""

    expenses = load_expenses()

    while True:
        print("\n" + "=" * 48)
        print("          PYTHON EXPENSE TRACKER")
        print("=" * 48)
        print("1. View all expenses")
        print("2. Add a new expense")
        print("3. View category summary")
        print("4. View monthly summary")
        print("5. Delete an expense")
        print("6. Exit")
        print("=" * 48)

        choice = input(
            "Choose an option from 1 to 6: "
        ).strip()

        if choice == "1":
            display_expenses(expenses)

        elif choice == "2":
            add_expense(expenses)

        elif choice == "3":
            display_category_summary(expenses)

        elif choice == "4":
            display_monthly_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print(
                "\nThank you for using the "
                "Python Expense Tracker."
            )
            break

        else:
            print(
                "Invalid option. "
                "Please choose a number from 1 to 6."
            )


if __name__ == "__main__":
    main()
