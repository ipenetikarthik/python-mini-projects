from __future__ import annotations

import json
import random
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Final, TypedDict, cast


class Question(TypedDict):
    """Structure of one quiz question."""

    id: int
    category: str
    difficulty: str
    question: str
    options: list[str]
    correct_answer: int
    explanation: str


class HighScoreEntry(TypedDict):
    """Structure of one saved high-score record."""

    player_name: str
    score: int
    total_questions: int
    percentage: float
    grade: str
    category: str
    difficulty: str
    completed_at: str


@dataclass(frozen=True, slots=True)
class AnswerResult:
    """Stores the result of one answered question."""

    question: str
    selected_answer: str
    correct_answer: str
    is_correct: bool
    explanation: str


def get_base_directory() -> Path:
    """Return the folder containing this Python file."""

    return Path(__file__).resolve().parent


BASE_DIRECTORY: Final[Path] = get_base_directory()
QUESTIONS_FILE: Final[Path] = BASE_DIRECTORY / "questions.json"
HIGH_SCORES_FILE: Final[Path] = BASE_DIRECTORY / "high_scores.json"

VALID_DIFFICULTIES: Final[frozenset[str]] = frozenset(
    {"Easy", "Medium", "Hard"}
)

MIN_OPTIONS: Final[int] = 4
MAX_HIGH_SCORES: Final[int] = 10


def parse_question(raw_question: object) -> Question | None:
    """Validate and convert raw JSON data into a Question."""

    if not isinstance(raw_question, dict):
        return None

    data = cast(dict[str, object], raw_question)

    question_id = data.get("id")
    category = data.get("category")
    difficulty = data.get("difficulty")
    question_text = data.get("question")
    options_value = data.get("options")
    correct_answer = data.get("correct_answer")
    explanation = data.get("explanation")

    if (
        not isinstance(question_id, int)
        or isinstance(question_id, bool)
        or question_id <= 0
    ):
        return None

    if not isinstance(category, str) or not category.strip():
        return None

    if not isinstance(difficulty, str):
        return None

    normalized_difficulty = difficulty.strip().title()

    if normalized_difficulty not in VALID_DIFFICULTIES:
        return None

    if not isinstance(question_text, str) or not question_text.strip():
        return None

    if not isinstance(options_value, list):
        return None

    options: list[str] = []

    for option in options_value:
        if not isinstance(option, str) or not option.strip():
            return None

        options.append(option.strip())

    if len(options) != MIN_OPTIONS:
        return None

    if (
        not isinstance(correct_answer, int)
        or isinstance(correct_answer, bool)
        or correct_answer < 1
        or correct_answer > len(options)
    ):
        return None

    if not isinstance(explanation, str) or not explanation.strip():
        return None

    return Question(
        id=question_id,
        category=category.strip(),
        difficulty=normalized_difficulty,
        question=question_text.strip(),
        options=options,
        correct_answer=correct_answer,
        explanation=explanation.strip(),
    )


def load_questions() -> list[Question]:
    """Load and validate quiz questions from the JSON file."""

    if not QUESTIONS_FILE.exists():
        print(
            "\nThe questions.json file was not found inside "
            "the project folder."
        )
        return []

    try:
        with QUESTIONS_FILE.open(
            mode="r",
            encoding="utf-8",
        ) as file:
            raw_data: object = json.load(file)

    except json.JSONDecodeError:
        print(
            "\nThe questions.json file contains invalid JSON data."
        )
        return []

    except OSError as error:
        print(f"\nUnable to read the questions file: {error}")
        return []

    if not isinstance(raw_data, list):
        print(
            "\nThe questions file must contain a JSON list."
        )
        return []

    questions: list[Question] = []
    invalid_question_count = 0

    for raw_question in raw_data:
        question = parse_question(raw_question)

        if question is None:
            invalid_question_count += 1
            continue

        questions.append(question)

    if invalid_question_count:
        print(
            f"\nWarning: {invalid_question_count} invalid "
            "question record(s) were ignored."
        )

    if not questions:
        print(
            "\nNo valid questions were found in questions.json."
        )

    return questions


def parse_high_score(
    raw_entry: object,
) -> HighScoreEntry | None:
    """Validate and convert one stored high-score entry."""

    if not isinstance(raw_entry, dict):
        return None

    data = cast(dict[str, object], raw_entry)

    player_name = data.get("player_name")
    score = data.get("score")
    total_questions = data.get("total_questions")
    percentage = data.get("percentage")
    grade = data.get("grade")
    category = data.get("category")
    difficulty = data.get("difficulty")
    completed_at = data.get("completed_at")

    if not isinstance(player_name, str) or not player_name.strip():
        return None

    if (
        not isinstance(score, int)
        or isinstance(score, bool)
        or score < 0
    ):
        return None

    if (
        not isinstance(total_questions, int)
        or isinstance(total_questions, bool)
        or total_questions <= 0
    ):
        return None

    if score > total_questions:
        return None

    if (
        not isinstance(percentage, (int, float))
        or isinstance(percentage, bool)
    ):
        return None

    percentage_value = float(percentage)

    if percentage_value < 0 or percentage_value > 100:
        return None

    string_values = (
        grade,
        category,
        difficulty,
        completed_at,
    )

    if any(
        not isinstance(value, str) or not value.strip()
        for value in string_values
    ):
        return None

    return HighScoreEntry(
        player_name=player_name.strip(),
        score=score,
        total_questions=total_questions,
        percentage=round(percentage_value, 2),
        grade=cast(str, grade).strip(),
        category=cast(str, category).strip(),
        difficulty=cast(str, difficulty).strip(),
        completed_at=cast(str, completed_at).strip(),
    )


def load_high_scores() -> list[HighScoreEntry]:
    """Load valid high-score records from JSON storage."""

    if not HIGH_SCORES_FILE.exists():
        return []

    try:
        with HIGH_SCORES_FILE.open(
            mode="r",
            encoding="utf-8",
        ) as file:
            raw_data: object = json.load(file)

    except (json.JSONDecodeError, OSError):
        return []

    if not isinstance(raw_data, list):
        return []

    high_scores: list[HighScoreEntry] = []

    for raw_entry in raw_data:
        entry = parse_high_score(raw_entry)

        if entry is not None:
            high_scores.append(entry)

    return high_scores


def save_high_score(entry: HighScoreEntry) -> None:
    """Save a high score and retain the best ten records."""

    high_scores = load_high_scores()
    high_scores.append(entry)

    high_scores.sort(
        key=lambda item: (
            item["percentage"],
            item["score"],
        ),
        reverse=True,
    )

    high_scores = high_scores[:MAX_HIGH_SCORES]

    try:
        with HIGH_SCORES_FILE.open(
            mode="w",
            encoding="utf-8",
        ) as file:
            json.dump(
                high_scores,
                file,
                indent=4,
                ensure_ascii=False,
            )

    except OSError as error:
        print(f"\nUnable to save the high score: {error}")


def get_integer(
    prompt: str,
    minimum: int,
    maximum: int,
) -> int:
    """Receive and validate an integer within a range."""

    while True:
        value = input(prompt).strip()

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


def get_player_name() -> str:
    """Receive a valid player name."""

    while True:
        player_name = input(
            "\nEnter your name: "
        ).strip()

        if player_name:
            return player_name

        print("Player name cannot be empty.")


def display_selection_menu(
    title: str,
    options: list[str],
) -> str:
    """Display options and return the selected value."""

    print(f"\n{title}")
    print("-" * 55)

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    choice = get_integer(
        prompt=f"Choose an option from 1 to {len(options)}: ",
        minimum=1,
        maximum=len(options),
    )

    return options[choice - 1]


def get_categories(
    questions: list[Question],
) -> list[str]:
    """Return unique categories in alphabetical order."""

    return sorted(
        {
            question["category"]
            for question in questions
        }
    )


def filter_questions(
    questions: list[Question],
    selected_category: str,
    selected_difficulty: str,
) -> list[Question]:
    """Filter questions by category and difficulty."""

    filtered_questions: list[Question] = []

    for question in questions:
        category_matches = (
            selected_category == "All Categories"
            or question["category"] == selected_category
        )

        difficulty_matches = (
            selected_difficulty == "All Difficulties"
            or question["difficulty"] == selected_difficulty
        )

        if category_matches and difficulty_matches:
            filtered_questions.append(question)

    return filtered_questions


def calculate_grade(percentage: float) -> str:
    """Return a grade based on the final percentage."""

    if percentage >= 90:
        return "A+"

    if percentage >= 80:
        return "A"

    if percentage >= 70:
        return "B"

    if percentage >= 60:
        return "C"

    if percentage >= 50:
        return "D"

    return "Needs Improvement"


def display_question(
    question: Question,
    current_number: int,
    total_questions: int,
) -> None:
    """Display one quiz question and its options."""

    progress_percentage = (
        current_number / total_questions
    ) * 100

    print("\n" + "=" * 70)
    print(
        f"Question {current_number}/{total_questions} "
        f"({progress_percentage:.0f}% complete)"
    )
    print(
        f"Category: {question['category']} | "
        f"Difficulty: {question['difficulty']}"
    )
    print("-" * 70)
    print(question["question"])
    print()

    for index, option in enumerate(
        question["options"],
        start=1,
    ):
        print(f"{index}. {option}")

    print("=" * 70)


def ask_question(
    question: Question,
    current_number: int,
    total_questions: int,
) -> AnswerResult:
    """Ask one question and return the result."""

    display_question(
        question,
        current_number,
        total_questions,
    )

    selected_number = get_integer(
        prompt="Enter your answer from 1 to 4: ",
        minimum=1,
        maximum=len(question["options"]),
    )

    selected_answer = question["options"][
        selected_number - 1
    ]

    correct_number = question["correct_answer"]

    correct_answer = question["options"][
        correct_number - 1
    ]

    is_correct = selected_number == correct_number

    if is_correct:
        print("\nCorrect! ✅")
    else:
        print("\nIncorrect. ❌")
        print(f"Correct answer: {correct_answer}")

    print(f"Explanation: {question['explanation']}")

    return AnswerResult(
        question=question["question"],
        selected_answer=selected_answer,
        correct_answer=correct_answer,
        is_correct=is_correct,
        explanation=question["explanation"],
    )


def display_quiz_summary(
    player_name: str,
    results: list[AnswerResult],
) -> tuple[int, float, str]:
    """Display final quiz results."""

    total_questions = len(results)

    score = sum(
        result.is_correct
        for result in results
    )

    percentage = (
        score / total_questions
    ) * 100

    grade = calculate_grade(percentage)

    incorrect_answers = total_questions - score

    print("\n" + "=" * 70)
    print("                       QUIZ RESULT")
    print("=" * 70)
    print(f"{'Player':<35}{player_name:>35}")
    print(f"{'Correct Answers':<35}{score:>35}")
    print(
        f"{'Incorrect Answers':<35}"
        f"{incorrect_answers:>35}"
    )
    print(
        f"{'Total Questions':<35}"
        f"{total_questions:>35}"
    )
    print(
        f"{'Percentage':<35}"
        f"{percentage:>31.2f}%"
    )
    print(f"{'Grade':<35}{grade:>35}")
    print("=" * 70)

    if percentage >= 90:
        print(
            "Excellent performance! "
            "You have a strong understanding of the topic."
        )

    elif percentage >= 70:
        print(
            "Good work! Review the incorrect answers "
            "and continue practising."
        )

    elif percentage >= 50:
        print(
            "You are making progress. "
            "More revision will improve your score."
        )

    else:
        print(
            "Keep learning and try again. "
            "Every attempt improves your understanding."
        )

    return score, percentage, grade


def display_answer_review(
    results: list[AnswerResult],
) -> None:
    """Display a review of all incorrectly answered questions."""

    incorrect_results = [
        result
        for result in results
        if not result.is_correct
    ]

    if not incorrect_results:
        print(
            "\nPerfect score! "
            "There are no incorrect answers to review."
        )
        return

    print("\n" + "=" * 70)
    print("                    INCORRECT ANSWER REVIEW")
    print("=" * 70)

    for index, result in enumerate(
        incorrect_results,
        start=1,
    ):
        print(f"\n{index}. {result.question}")
        print(
            f"Your answer: {result.selected_answer}"
        )
        print(
            f"Correct answer: {result.correct_answer}"
        )
        print(
            f"Explanation: {result.explanation}"
        )
        print("-" * 70)


def start_quiz(questions: list[Question]) -> None:
    """Configure and run a complete quiz."""

    if not questions:
        print(
            "\nThe quiz cannot start because no valid "
            "questions are available."
        )
        return

    player_name = get_player_name()

    category_options = [
        "All Categories",
        *get_categories(questions),
    ]

    difficulty_options = [
        "All Difficulties",
        "Easy",
        "Medium",
        "Hard",
    ]

    selected_category = display_selection_menu(
        title="SELECT A CATEGORY",
        options=category_options,
    )

    selected_difficulty = display_selection_menu(
        title="SELECT A DIFFICULTY",
        options=difficulty_options,
    )

    available_questions = filter_questions(
        questions,
        selected_category,
        selected_difficulty,
    )

    if not available_questions:
        print(
            "\nNo questions are available for the selected "
            "category and difficulty."
        )
        return

    print(
        f"\nAvailable questions: "
        f"{len(available_questions)}"
    )

    question_count = get_integer(
        prompt=(
            f"How many questions would you like "
            f"(1-{len(available_questions)})? "
        ),
        minimum=1,
        maximum=len(available_questions),
    )

    selected_questions = random.sample(
        available_questions,
        k=question_count,
    )

    results: list[AnswerResult] = []

    print("\nThe quiz is starting. Good luck!")

    for current_number, question in enumerate(
        selected_questions,
        start=1,
    ):
        result = ask_question(
            question,
            current_number,
            question_count,
        )

        results.append(result)

    score, percentage, grade = display_quiz_summary(
        player_name,
        results,
    )

    high_score_entry = HighScoreEntry(
        player_name=player_name,
        score=score,
        total_questions=question_count,
        percentage=round(percentage, 2),
        grade=grade,
        category=selected_category,
        difficulty=selected_difficulty,
        completed_at=datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        ),
    )

    save_high_score(high_score_entry)
    display_answer_review(results)


def display_high_scores() -> None:
    """Display the ten highest quiz scores."""

    high_scores = load_high_scores()

    if not high_scores:
        print(
            "\nNo high scores are available yet. "
            "Complete a quiz to create the first record."
        )
        return

    print("\n" + "=" * 100)
    print(" " * 40 + "HIGH SCORES")
    print("=" * 100)
    print(
        f"{'Rank':<7}"
        f"{'Player':<20}"
        f"{'Score':<12}"
        f"{'Percentage':<14}"
        f"{'Grade':<20}"
        f"{'Completed At':<25}"
    )
    print("-" * 100)

    for rank, entry in enumerate(
        high_scores,
        start=1,
    ):
        score_text = (
            f"{entry['score']}/"
            f"{entry['total_questions']}"
        )

        percentage_text = (
            f"{entry['percentage']:.2f}%"
        )

        print(
            f"{rank:<7}"
            f"{entry['player_name'][:18]:<20}"
            f"{score_text:<12}"
            f"{percentage_text:<14}"
            f"{entry['grade']:<20}"
            f"{entry['completed_at']:<25}"
        )

    print("=" * 100)


def main() -> None:
    """Run the Python Quiz Application."""

    questions = load_questions()

    while True:
        print("\n" + "=" * 58)
        print("              PYTHON QUIZ APPLICATION")
        print("=" * 58)
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Reload Questions")
        print("4. Exit")
        print("=" * 58)

        choice = input(
            "Choose an option from 1 to 4: "
        ).strip()

        if choice == "1":
            start_quiz(questions)

        elif choice == "2":
            display_high_scores()

        elif choice == "3":
            questions = load_questions()

            if questions:
                print(
                    f"\nSuccessfully loaded "
                    f"{len(questions)} questions."
                )

        elif choice == "4":
            print(
                "\nThank you for using the "
                "Python Quiz Application."
            )
            break

        else:
            print(
                "\nInvalid option. "
                "Please choose a number from 1 to 4."
            )


if __name__ == "__main__":
    main()
