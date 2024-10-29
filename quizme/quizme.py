"""
QuizMe: An adaptive quiz Command Line Interface (CLI) application.

This script allows users to take an adaptive quiz based on questions loaded from a JSON file.
It uses the Adaptive Review System (ARS) to manage the quiz session.
"""
import json
from pathlib import Path
from quizme.ars.arcontroller import ARController


def load_questions(file_path: Path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        raise

def run_quiz(name, questions):
    print(f"Welcome to the QuizMe session, {name}!")
    controller = ARController(questions)
    controller.start()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="QuizMe: An adaptive quiz application.")
    parser.add_argument("name", help="Name of the quiz taker.")
    parser.add_argument("--questions", required=True, type=Path, help="Path to the JSON file with questions.")
    args = parser.parse_args()
    questions = load_questions(args.questions)
    run_quiz(args.name, questions)

if __name__ == "__main__":
    main()
