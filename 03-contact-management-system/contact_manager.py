from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Final, TypedDict, cast


class Contact(TypedDict):
    """Structure of a contact record."""

    name: str
    phone: str
    email: str
    address: str


def get_base_dir() -> Path:
    """Return the folder containing this Python file."""

    try:
        return Path(__file__).resolve().parent
    except NameError:
        return Path.cwd()


BASE_DIR: Final[Path] = get_base_dir()
DATA_FILE: Final[Path] = BASE_DIR / "contacts.json"

EMAIL_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


def normalize_phone(phone: str) -> str:
    """Return only the numeric characters from a phone number."""

    return "".join(character for character in phone if character.isdigit())


def is_valid_phone(phone: str) -> bool:
    """Validate a phone number."""

    normalized_phone = normalize_phone(phone)

    return 7 <= len(normalized_phone) <= 15


def is_valid_email(email: str) -> bool:
    """Validate an email address."""

    if not email:
        return True

    return EMAIL_PATTERN.fullmatch(email) is not None


def parse_contact(value: object) -> Contact | None:
    """Validate one contact loaded from the JSON file."""

    if not isinstance(value, dict):
        return None

    data = cast(dict[object, object], value)

    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    address = data.get("address")

    if not isinstance(name, str) or not name.strip():
        return None

    if (
        not isinstance(phone, str)
        or not phone.strip()
        or not is_valid_phone(phone)
    ):
        return None

    if not isinstance(email, str) or not is_valid_email(email.strip()):
        return None

    if not isinstance(address, str):
        return None

    contact: Contact = {
        "name": name.strip().title(),
        "phone": phone.strip(),
        "email": email.strip().lower(),
        "address": address.strip(),
    }

    return contact


def load_contacts() -> list[Contact]:
    """Load and validate contacts from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            raw_data = cast(object, json.load(file))

    except json.JSONDecodeError:
        print("The contacts file contains invalid JSON.")
        print("Starting with an empty contact list.")
        return []

    except OSError as error:
        print(f"Unable to read the contacts file: {error}")
        return []

    if not isinstance(raw_data, list):
        print("Invalid contact data found.")
        print("Starting with an empty contact list.")
        return []

    raw_contacts = cast(list[object], raw_data)

    contacts: list[Contact] = []
    invalid_records = 0

    for item in raw_contacts:
        contact = parse_contact(item)

        if contact is None:
            invalid_records += 1
        else:
            contacts.append(contact)

    if invalid_records:
        print(f"Ignored {invalid_records} invalid contact record(s).")

    return contacts


def save_contacts(contacts: list[Contact]) -> bool:
    """Save contacts to the JSON file."""

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                contacts,
                file,
                indent=4,
                ensure_ascii=False,
            )

        return True

    except OSError as error:
        print(f"Unable to save contacts: {error}")
        return False


def phone_exists(
    contacts: list[Contact],
    phone: str,
    exclude_index: int | None = None,
) -> bool:
    """Check whether a phone number already exists."""

    normalized_phone = normalize_phone(phone)

    for index, contact in enumerate(contacts):
        if exclude_index is not None and index == exclude_index:
            continue

        if normalize_phone(contact["phone"]) == normalized_phone:
            return True

    return False


def email_exists(
    contacts: list[Contact],
    email: str,
    exclude_index: int | None = None,
) -> bool:
    """Check whether an email address already exists."""

    if not email:
        return False

    normalized_email = email.casefold()

    for index, contact in enumerate(contacts):
        if exclude_index is not None and index == exclude_index:
            continue

        if contact["email"].casefold() == normalized_email:
            return True

    return False


def display_contacts(
    contacts: list[Contact],
    indexes: list[int] | None = None,
) -> None:
    """Display contacts in a table."""

    if not contacts:
        print("\nNo contacts are available.")
        return

    selected_indexes = (
        indexes if indexes is not None else list(range(len(contacts)))
    )

    if not selected_indexes:
        print("\nNo matching contacts found.")
        return

    print("\nCONTACT LIST")
    print("=" * 105)

    print(
        f"{'No.':<6}"
        f"{'Name':<24}"
        f"{'Phone':<18}"
        f"{'Email':<30}"
        f"{'Address':<27}"
    )

    print("-" * 105)

    for index in selected_indexes:
        contact = contacts[index]

        print(
            f"{index + 1:<6}"
            f"{contact['name'][:22]:<24}"
            f"{contact['phone'][:16]:<18}"
            f"{contact['email'][:28]:<30}"
            f"{contact['address'][:25]:<27}"
        )

    print("=" * 105)


def get_contact_index(contacts: list[Contact]) -> int | None:
    """Receive and validate a contact number."""

    try:
        contact_number = int(
            input("\nEnter the contact number: ").strip()
        )

    except ValueError:
        print("Please enter a valid number.")
        return None

    if contact_number < 1 or contact_number > len(contacts):
        print(
            f"Please enter a number between 1 and "
            f"{len(contacts)}."
        )
        return None

    return contact_number - 1


def add_contact(contacts: list[Contact]) -> None:
    """Add a new contact."""

    print("\nADD NEW CONTACT")
    print("-" * 45)

    name = input("Enter the name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter the phone number: ").strip()

    if not is_valid_phone(phone):
        print("Enter a valid phone number containing 7 to 15 digits.")
        return

    if phone_exists(contacts, phone):
        print("A contact with this phone number already exists.")
        return

    email = input(
        "Enter the email address or press Enter to skip: "
    ).strip().lower()

    if not is_valid_email(email):
        print("Please enter a valid email address.")
        return

    if email_exists(contacts, email):
        print("A contact with this email address already exists.")
        return

    address = input(
        "Enter the address or press Enter to skip: "
    ).strip()

    new_contact: Contact = {
        "name": name.title(),
        "phone": phone,
        "email": email,
        "address": address,
    }

    contacts.append(new_contact)

    if save_contacts(contacts):
        print("\nContact added successfully.")
    else:
        contacts.pop()
        print("The contact could not be saved.")


def search_contacts(contacts: list[Contact]) -> None:
    """Search contacts by name, phone, email, or address."""

    if not contacts:
        print("\nNo contacts are available.")
        return

    query = input(
        "\nEnter a name, phone, email, or address to search: "
    ).strip().casefold()

    if not query:
        print("Search text cannot be empty.")
        return

    matching_indexes: list[int] = []

    for index, contact in enumerate(contacts):
        searchable_values = (
            contact["name"],
            contact["phone"],
            contact["email"],
            contact["address"],
        )

        if any(
            query in value.casefold()
            for value in searchable_values
        ):
            matching_indexes.append(index)

    display_contacts(contacts, matching_indexes)


def edit_contact(contacts: list[Contact]) -> None:
    """Edit an existing contact."""

    if not contacts:
        print("\nNo contacts are available.")
        return

    display_contacts(contacts)

    contact_index = get_contact_index(contacts)

    if contact_index is None:
        return

    current_contact = contacts[contact_index]

    print("\nEDIT CONTACT")
    print("Press Enter to keep the current value.")
    print("-" * 45)

    name = input(
        f"Name [{current_contact['name']}]: "
    ).strip()

    phone = input(
        f"Phone [{current_contact['phone']}]: "
    ).strip()

    email = input(
        f"Email [{current_contact['email'] or 'Not provided'}]: "
    ).strip().lower()

    address = input(
        f"Address [{current_contact['address'] or 'Not provided'}]: "
    ).strip()

    updated_name = name.title() if name else current_contact["name"]
    updated_phone = phone if phone else current_contact["phone"]
    updated_email = email if email else current_contact["email"]
    updated_address = (
        address if address else current_contact["address"]
    )

    if not is_valid_phone(updated_phone):
        print("Enter a valid phone number containing 7 to 15 digits.")
        return

    if phone_exists(
        contacts,
        updated_phone,
        exclude_index=contact_index,
    ):
        print("Another contact already uses this phone number.")
        return

    if not is_valid_email(updated_email):
        print("Please enter a valid email address.")
        return

    if email_exists(
        contacts,
        updated_email,
        exclude_index=contact_index,
    ):
        print("Another contact already uses this email address.")
        return

    updated_contact: Contact = {
        "name": updated_name,
        "phone": updated_phone,
        "email": updated_email,
        "address": updated_address,
    }

    original_contact = contacts[contact_index]
    contacts[contact_index] = updated_contact

    if save_contacts(contacts):
        print("\nContact updated successfully.")
    else:
        contacts[contact_index] = original_contact
        print("The contact could not be updated.")


def delete_contact(contacts: list[Contact]) -> None:
    """Delete an existing contact."""

    if not contacts:
        print("\nNo contacts are available.")
        return

    display_contacts(contacts)

    contact_index = get_contact_index(contacts)

    if contact_index is None:
        return

    selected_contact = contacts[contact_index]

    confirmation = input(
        f"Delete '{selected_contact['name']}'? (y/n): "
    ).strip().lower()

    if confirmation not in {"y", "yes"}:
        print("Deletion cancelled.")
        return

    removed_contact = contacts.pop(contact_index)

    if save_contacts(contacts):
        print(f"Deleted contact: {removed_contact['name']}")
    else:
        contacts.insert(contact_index, removed_contact)
        print("The contact could not be deleted.")


def display_statistics(contacts: list[Contact]) -> None:
    """Display basic contact statistics."""

    total_contacts = len(contacts)

    contacts_with_email = sum(
        1 for contact in contacts if contact["email"]
    )

    contacts_with_address = sum(
        1 for contact in contacts if contact["address"]
    )

    print("\nCONTACT STATISTICS")
    print("=" * 45)
    print(f"{'Total contacts':<30}{total_contacts:>15}")
    print(
        f"{'Contacts with email':<30}"
        f"{contacts_with_email:>15}"
    )
    print(
        f"{'Contacts with address':<30}"
        f"{contacts_with_address:>15}"
    )
    print("=" * 45)


def main() -> None:
    """Run the Contact Management System."""

    contacts = load_contacts()

    while True:
        print("\n" + "=" * 50)
        print("       PYTHON CONTACT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. View all contacts")
        print("2. Add a new contact")
        print("3. Search contacts")
        print("4. Edit a contact")
        print("5. Delete a contact")
        print("6. View contact statistics")
        print("7. Exit")
        print("=" * 50)

        choice = input(
            "Choose an option from 1 to 7: "
        ).strip()

        if choice == "1":
            display_contacts(contacts)

        elif choice == "2":
            add_contact(contacts)

        elif choice == "3":
            search_contacts(contacts)

        elif choice == "4":
            edit_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            display_statistics(contacts)

        elif choice == "7":
            print(
                "\nThank you for using the "
                "Python Contact Management System."
            )
            break

        else:
            print(
                "Invalid option. "
                "Please choose a number from 1 to 7."
            )


if __name__ == "__main__":
    main()
