from __future__ import annotations

import json
from datetime import datetime
from math import isfinite
from pathlib import Path
from typing import Final, TypedDict, cast


class Expense(TypedDict):
    """Structure of one expense record."""

    description: str
    category: str
    amount: float
    date: str


def get_base_dir() -> Path:
    """Return the folder containing this Python file."""

    try:
        return Path(__file__).resolve().parent
    except NameError:
        return Path.cwd()


# Assigned only once, so Pylance will not report constant redefinition.
BASE_DIR: Final[Path] = get_base_dir()
DATA_FILE: Final[Path] = BASE_DIR / "expenses.json"


def parse_expense(value: object) -> Expense | None:
    """Validate one expense loaded from the JSON file."""

    if not isinstance(value, dict):
        return None

    data = cast(dict[object, object], value)

    description = data.get("description")
    category = data.get("category")
    amount = data.get("amount")
    date_value = data.get("date")

    if not isinstance(description, str) or not description.strip():
        return None

    if not isinstance(category, str) or not category.strip():
        return None

    if (
        isinstance(amount, bool)
        or not isinstance(amount, (int, float))
        or not isfinite(float(amount))
        or amount <= 0
    ):
        return None

    if not isinstance(date_value, str):
        return None

    try:
        valid_date = datetime.strptime(date_value, "%Y-%m-%d")
    except ValueError:
        return None

    expense: Expense = {
        "description": description.strip(),
        "category": category.strip().title(),
        "amount": round(float(amount), 2),
        "date": valid_date.strftime("%Y-%m-%d"),
    }

    return expense


def load_expenses() -> list[Expense]:
    """Load and validate saved expenses from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            raw_data = cast(object, json.load(file))

    except json.JSONDecodeError:
        print("The expenses file contains invalid JSON.")
        print("Starting with an empty expense list.")
        return []

    except OSError as error:
        print(f"Unable to read the expenses file: {error}")
        return []

    if not isinstance(raw_data, list):
        print("Invalid expense data found.")
        print("Starting with an empty expense list.")
        return []

    raw_items = cast(list[object], raw_data)

    expenses: list[Expense] = []
    invalid_records = 0

    for item in raw_items:
        expense = parse_expense(item)

        if expense is None:
            invalid_records += 1
        else:
            expenses.append(expense)

    if invalid_records:
        print(f"Ignored {invalid_records} invalid expense record(s).")

    return expenses


def save_expenses(expenses: list[Expense]) -> bool:
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


def get_valid_amount() -> float | None:
    """Receive and validate an expense amount."""

    value = input("Enter the amount: ₹").strip()

    try:
        amount = float(value)

    except ValueError:
        print("Please enter a valid numeric amount.")
        return None

    if not isfinite(amount) or amount <= 0:
        print("The amount must be a finite number greater than zero.")
        return None

    return round(amount, 2)


def get_valid_date() -> str | None:
    """Receive and validate a date in YYYY-MM-DD format."""

    date_value = input(
        "Enter the date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if not date_value:
        return datetime.now().strftime("%Y-%m-%d")

    try:
        valid_date = datetime.strptime(date_value, "%Y-%m-%d")

    except ValueError:
        print("Invalid date. Please use the YYYY-MM-DD format.")
        return None

    return valid_date.strftime("%Y-%m-%d")


def add_expense(expenses: list[Expense]) -> None:
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

    # Explicit Expense type removes the partially unknown dictionary error.
    new_expense: Expense = {
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


def display_expenses(expenses: list[Expense]) -> None:
    """Display all recorded expenses."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    sorted_expenses: list[Expense] = sorted(
        expenses,
        key=lambda expense: expense["date"],
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
        total += expense["amount"]

        print(
            f"{index:<5}"
            f"{expense['date']:<14}"
            f"{expense['category'][:16]:<18}"
            f"{expense['description'][:26]:<28}"
            f"₹{expense['amount']:>13.2f}"
        )

    print("-" * 82)
    print(f"{'Total Expenses':<67}₹{total:>13.2f}")
    print("=" * 82)


def display_category_summary(expenses: list[Expense]) -> None:
    """Display total expenses grouped by category."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    category_totals: dict[str, float] = {}

    for expense in expenses:
        category = expense["category"]

        category_totals[category] = (
            category_totals.get(category, 0.0)
            + expense["amount"]
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


def display_monthly_summary(expenses: list[Expense]) -> None:
    """Display total expenses grouped by month."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    monthly_totals: dict[str, float] = {}

    for expense in expenses:
        month_key = datetime.strptime(
            expense["date"],
            "%Y-%m-%d",
        ).strftime("%Y-%m")

        monthly_totals[month_key] = (
            monthly_totals.get(month_key, 0.0)
            + expense["amount"]
        )

    print("\nMONTHLY SUMMARY")
    print("=" * 50)
    print(f"{'Month':<32}{'Amount':>18}")
    print("-" * 50)

    grand_total = 0.0

    for month_key in sorted(monthly_totals, reverse=True):
        amount = monthly_totals[month_key]

        month_name = datetime.strptime(
            month_key,
            "%Y-%m",
        ).strftime("%B %Y")

        grand_total += amount

        print(f"{month_name:<32}₹{amount:>16.2f}")

    print("-" * 50)
    print(f"{'Grand Total':<32}₹{grand_total:>16.2f}")
    print("=" * 50)


def get_expense_index(
    expenses: list[Expense],
) -> int | None:
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
            f"Please enter a number between 1 and "
            f"{len(expenses)}."
        )
        return None

    return expense_number - 1


def delete_expense(expenses: list[Expense]) -> None:
    """Delete a selected expense."""

    if not expenses:
        print("\nNo expenses are available.")
        return

    print("\nEXPENSES")
    print("-" * 70)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['description']} | "
            f"{expense['date']} | "
            f"₹{expense['amount']:.2f}"
        )

    expense_index = get_expense_index(expenses)

    if expense_index is None:
        return

    selected_expense = expenses[expense_index]

    confirmation = input(
        f"Delete '{selected_expense['description']}'? "
        "(y/n): "
    ).strip().lower()

    if confirmation not in {"y", "yes"}:
        print("Deletion cancelled.")
        return

    removed_expense = expenses.pop(expense_index)

    if save_expenses(expenses):
        print(
            f"Deleted expense: "
            f"{removed_expense['description']}"
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
