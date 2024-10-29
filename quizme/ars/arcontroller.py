from ars.boxmanager import BoxManager
from ars.qtype.shortanswer import ShortAnswer
from ars.qtype.truefalse import TrueFalse

class ARController:
    def __init__(self, question_data):
        self._box_manager = BoxManager()
        self._initialize_questions(question_data)

    def _initialize_questions(self, question_data):
        for data in question_data:
            question_type = data["type"]
            try:
                if question_type == "shortanswer":
                    question = ShortAnswer(data["question"], data["correct_answer"], data.get("case_sensitive", False))
                elif question_type == "truefalse":
                    question = TrueFalse(data["question"], data["correct_answer"], data.get("explanation", ""))
                else:
                    print(f"Unsupported question type: {question_type}")
                    continue
                self._box_manager.add_new_question(question)
            except KeyError as e:
                print(f"Error initializing question: missing {e}")

    def start(self):
        print("Type 'q' at any time to quit the session.")
        while True:
            question = self._box_manager.get_next_question()
            if not question:
                print("All questions have been reviewed. Session complete!")
                break
            print(question.ask())
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'q':
                break
            correct = question.check_answer(user_answer)
            print("Correct!" if correct else question.incorrect_feedback())
            self._box_manager.move_question(question, correct)
        print("Thank you, goodbye!")
