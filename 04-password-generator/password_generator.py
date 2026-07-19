from __future__ import annotations

import secrets
import string
from dataclasses import dataclass
from typing import Final


LOWERCASE: Final[str] = string.ascii_lowercase
UPPERCASE: Final[str] = string.ascii_uppercase
DIGITS: Final[str] = string.digits
SYMBOLS: Final[str] = "!@#$%^&*()-_=+[]{};:,.?/"

AMBIGUOUS_CHARACTERS: Final[frozenset[str]] = frozenset(
    {"0", "O", "o", "1", "I", "l", "|"}
)

COMMON_PATTERNS: Final[tuple[str, ...]] = (
    "password",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "python",
    "1234",
    "abcd",
)

SEQUENCES: Final[tuple[str, ...]] = (
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba",
    "0123456789",
    "9876543210",
)

MIN_PASSWORD_LENGTH: Final[int] = 8
MAX_PASSWORD_LENGTH: Final[int] = 128
MAX_PASSWORD_COUNT: Final[int] = 20


@dataclass(frozen=True, slots=True)
class PasswordOptions:
    """Configuration used to generate passwords."""

    length: int
    include_lowercase: bool
    include_uppercase: bool
    include_digits: bool
    include_symbols: bool
    exclude_ambiguous: bool


@dataclass(frozen=True, slots=True)
class StrengthResult:
    """Result produced by the password-strength checker."""

    score: int
    label: str
    feedback: tuple[str, ...]


def get_integer(
    prompt: str,
    minimum: int,
    maximum: int,
    default: int | None = None,
) -> int:
    """Receive and validate an integer within a permitted range."""

    while True:
        value = input(prompt).strip()

        if not value and default is not None:
            return default

        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if number < minimum or number > maximum:
            print(
                f"Please enter a number between "
                f"{minimum} and {maximum}."
            )
            continue

        return number


def get_yes_no(
    prompt: str,
    default: bool | None = None,
) -> bool:
    """Receive and validate a yes-or-no response."""

    while True:
        response = input(prompt).strip().lower()

        if not response and default is not None:
            return default

        if response in {"y", "yes"}:
            return True

        if response in {"n", "no"}:
            return False

        print("Please enter y for yes or n for no.")


def remove_ambiguous_characters(characters: str) -> str:
    """Remove characters that may be visually confusing."""

    return "".join(
        character
        for character in characters
        if character not in AMBIGUOUS_CHARACTERS
    )


def get_character_groups(
    options: PasswordOptions,
) -> list[str]:
    """Return the selected character groups."""

    groups: list[str] = []

    if options.include_lowercase:
        groups.append(LOWERCASE)

    if options.include_uppercase:
        groups.append(UPPERCASE)

    if options.include_digits:
        groups.append(DIGITS)

    if options.include_symbols:
        groups.append(SYMBOLS)

    if options.exclude_ambiguous:
        groups = [
            remove_ambiguous_characters(group)
            for group in groups
        ]

    return [group for group in groups if group]


def secure_shuffle(value: str) -> str:
    """Shuffle characters using cryptographically secure randomness."""

    characters = list(value)

    for index in range(len(characters) - 1, 0, -1):
        random_index = secrets.randbelow(index + 1)

        characters[index], characters[random_index] = (
            characters[random_index],
            characters[index],
        )

    return "".join(characters)


def generate_password(options: PasswordOptions) -> str:
    """Generate one secure password."""

    groups = get_character_groups(options)

    if not groups:
        raise ValueError(
            "At least one character group must be selected."
        )

    if options.length < len(groups):
        raise ValueError(
            "Password length must be at least equal to the "
            "number of selected character groups."
        )

    required_characters: list[str] = [
        secrets.choice(group)
        for group in groups
    ]

    character_pool = "".join(groups)

    remaining_length = (
        options.length - len(required_characters)
    )

    additional_characters: list[str] = [
        secrets.choice(character_pool)
        for _ in range(remaining_length)
    ]

    password = "".join(
        required_characters + additional_characters
    )

    return secure_shuffle(password)


def generate_passwords(
    options: PasswordOptions,
    count: int,
) -> list[str]:
    """Generate the requested number of passwords."""

    return [
        generate_password(options)
        for _ in range(count)
    ]


def contains_sequence(password: str) -> bool:
    """Check whether a password contains a common sequence."""

    lowered_password = password.casefold()

    for sequence in SEQUENCES:
        for start_index in range(len(sequence) - 3):
            fragment = sequence[start_index : start_index + 4]

            if fragment in lowered_password:
                return True

    return False


def contains_repeated_characters(password: str) -> bool:
    """Check for the same character repeated three times."""

    return any(
        password[index]
        == password[index + 1]
        == password[index + 2]
        for index in range(len(password) - 2)
    )


def evaluate_password_strength(
    password: str,
) -> StrengthResult:
    """Evaluate password strength and return feedback."""

    if not password:
        return StrengthResult(
            score=0,
            label="Very Weak",
            feedback=("Password cannot be empty.",),
        )

    score = 0
    feedback: list[str] = []

    password_length = len(password)

    if password_length >= 16:
        score += 45
    elif password_length >= 12:
        score += 35
        feedback.append(
            "Use at least 16 characters for stronger protection."
        )
    elif password_length >= 8:
        score += 20
        feedback.append(
            "Increase the password length to at least 12 characters."
        )
    else:
        score += 5
        feedback.append(
            "Use at least 8 characters."
        )

    category_count = sum(
        (
            any(character.islower() for character in password),
            any(character.isupper() for character in password),
            any(character.isdigit() for character in password),
            any(character in SYMBOLS for character in password),
        )
    )

    score += category_count * 10

    if category_count < 4:
        feedback.append(
            "Use lowercase letters, uppercase letters, "
            "numbers and symbols."
        )

    unique_character_ratio = (
        len(set(password)) / password_length
    )

    if password_length >= 12 and unique_character_ratio >= 0.70:
        score += 10
    elif unique_character_ratio < 0.50:
        score -= 10
        feedback.append(
            "Avoid using too many repeated characters."
        )

    lowered_password = password.casefold()

    if any(
        pattern in lowered_password
        for pattern in COMMON_PATTERNS
    ):
        score -= 25
        feedback.append(
            "Avoid common words and predictable patterns."
        )

    if contains_sequence(password):
        score -= 15
        feedback.append(
            "Avoid alphabetical or numerical sequences."
        )

    if contains_repeated_characters(password):
        score -= 10
        feedback.append(
            "Avoid repeating the same character several times."
        )

    final_score = max(0, min(score, 100))

    if final_score >= 85:
        label = "Very Strong"
    elif final_score >= 70:
        label = "Strong"
    elif final_score >= 50:
        label = "Moderate"
    elif final_score >= 30:
        label = "Weak"
    else:
        label = "Very Weak"

    if not feedback and final_score >= 85:
        feedback.append(
            "This password has strong length and character diversity."
        )

    return StrengthResult(
        score=final_score,
        label=label,
        feedback=tuple(feedback),
    )


def collect_password_options() -> PasswordOptions | None:
    """Collect password-generation preferences."""

    print("\nPASSWORD OPTIONS")
    print("-" * 50)

    length = get_integer(
        prompt=(
            f"Password length "
            f"({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}) "
            "[default 16]: "
        ),
        minimum=MIN_PASSWORD_LENGTH,
        maximum=MAX_PASSWORD_LENGTH,
        default=16,
    )

    include_lowercase = get_yes_no(
        "Include lowercase letters? (Y/n): ",
        default=True,
    )

    include_uppercase = get_yes_no(
        "Include uppercase letters? (Y/n): ",
        default=True,
    )

    include_digits = get_yes_no(
        "Include numbers? (Y/n): ",
        default=True,
    )

    include_symbols = get_yes_no(
        "Include symbols? (Y/n): ",
        default=True,
    )

    if not any(
        (
            include_lowercase,
            include_uppercase,
            include_digits,
            include_symbols,
        )
    ):
        print(
            "\nAt least one character type must be selected."
        )
        return None

    exclude_ambiguous = get_yes_no(
        "Exclude ambiguous characters such as 0, O, 1, I and l? "
        "(y/N): ",
        default=False,
    )

    options = PasswordOptions(
        length=length,
        include_lowercase=include_lowercase,
        include_uppercase=include_uppercase,
        include_digits=include_digits,
        include_symbols=include_symbols,
        exclude_ambiguous=exclude_ambiguous,
    )

    selected_group_count = len(
        get_character_groups(options)
    )

    if length < selected_group_count:
        print(
            "\nThe password length is too short for the "
            "selected character groups."
        )
        return None

    return options


def display_strength_result(
    result: StrengthResult,
) -> None:
    """Display a password-strength result."""

    print("\nPASSWORD STRENGTH")
    print("=" * 50)
    print(f"{'Strength':<30}{result.label:>20}")
    print(f"{'Score':<30}{result.score:>17}/100")
    print("-" * 50)

    for message in result.feedback:
        print(f"• {message}")

    print("=" * 50)


def generate_password_flow() -> None:
    """Generate and display one or more secure passwords."""

    options = collect_password_options()

    if options is None:
        return

    count = get_integer(
        prompt=(
            f"How many passwords should be generated "
            f"(1-{MAX_PASSWORD_COUNT}) [default 1]? "
        ),
        minimum=1,
        maximum=MAX_PASSWORD_COUNT,
        default=1,
    )

    try:
        passwords = generate_passwords(options, count)
    except ValueError as error:
        print(f"\nUnable to generate passwords: {error}")
        return

    print("\nGENERATED PASSWORDS")
    print("=" * 70)

    for index, password in enumerate(passwords, start=1):
        strength = evaluate_password_strength(password)

        print(
            f"{index:>2}. {password} "
            f"[{strength.label} — {strength.score}/100]"
        )

    print("=" * 70)

    print(
        "\nSecurity reminder: Store passwords in a trusted "
        "password manager and never reuse them across accounts."
    )


def check_password_flow() -> None:
    """Check the strength of a sample password."""

    print(
        "\nDo not enter a password currently used for a real account."
    )

    password = input(
        "Enter a sample password to evaluate: "
    )

    result = evaluate_password_strength(password)

    display_strength_result(result)


def main() -> None:
    """Run the Secure Password Generator."""

    while True:
        print("\n" + "=" * 52)
        print("        PYTHON SECURE PASSWORD GENERATOR")
        print("=" * 52)
        print("1. Generate secure passwords")
        print("2. Check password strength")
        print("3. Exit")
        print("=" * 52)

        choice = input(
            "Choose an option from 1 to 3: "
        ).strip()

        if choice == "1":
            generate_password_flow()

        elif choice == "2":
            check_password_flow()

        elif choice == "3":
            print(
                "\nThank you for using the "
                "Secure Password Generator."
            )
            break

        else:
            print(
                "Invalid option. "
                "Please choose a number from 1 to 3."
            )


if __name__ == "__main__":
    main()
