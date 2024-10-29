from ars.qtype.question import Question
import re

class ShortAnswer(Question):
    def __init__(self, question, answer, case_sensitive=False):
        super().__init__(question, answer)
        self._case_sensitive = case_sensitive

    def _normalize(self, text):
        text = text.strip()
        if not self._case_sensitive:
            text = text.lower()
        return re.sub(r'[^\w\s]', '', text)

    def check_answer(self, answer):
        return self._normalize(answer) == self._normalize(self._answer)

    def incorrect_feedback(self):
        return f"Incorrect. The correct answer is: {self._answer}"
