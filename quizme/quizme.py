import json
from pathlib import Path
import argparse
from ars.arcontroller import ARController 

def load_questions(file_path: Path):
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
            return questions
    except FileNotFoundError:
        print(f"Error: Question file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in question file {file_path}")
        raise

def run_quiz(name: str, questions):
    print(f"Welcome, {name}! Let's start your adaptive quiz session.")
    controller = ARController(questions)
    controller.start()

def main():
    parser = argparse.ArgumentParser(description="QuizMe: An adaptive quiz Command Line Interface (CLI) application.")
    parser.add_argument("name", help="Name of the user")
    parser.add_argument("--questions", default='python_fundamental_questions.json', help="Path to the questions JSON file")
    args = parser.parse_args()

    try:
        questions = load_questions(Path(args.questions))
        run_quiz(args.name, questions)
    except FileNotFoundError:
        print("Exiting due to error in loading questions.")

if __name__ == "__main__":
    main()
