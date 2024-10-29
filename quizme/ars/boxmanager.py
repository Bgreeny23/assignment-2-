from datetime import timedelta
from quizme.ars.box import Box
from quizme.ars.qtype.shortanswer import ShortAnswer
from quizme.ars.qtype.truefalse import TrueFalse

class BoxManager:
    def __init__(self):
        self._boxes = [
            Box("Missed Questions", timedelta(seconds=60)),
            Box("Unasked Questions", timedelta(seconds=0)),
            Box("Correctly Answered Once", timedelta(seconds=180)),
            Box("Correctly Answered Twice", timedelta(seconds=360)),
            Box("Known Questions", timedelta.max)
        ]
        self._question_location = {}

    def add_new_question(self, question):
        self._boxes[1].add_question(question)
        self._question_location[str(question.id)] = 1

    def move_question(self, question, answered_correctly):
        current_index = self._question_location[str(question.id)]
        if answered_correctly:
            new_index = min(current_index + 1, len(self._boxes) - 1)
        else:
            new_index = 0
        self._boxes[current_index].remove_question(question)
        self._boxes[new_index].add_question(question)
        self._question_location[str(question.id)] = new_index
        self._log_box_counts()

    def get_next_question(self):
        for box in self._boxes[:-1]:
            question = box.get_next_priority_question()
            if question:
                return question
        return None

    def _log_box_counts(self):
        for box in self._boxes:
            print(f"{box.name}: {len(box)} questions")
