from quizme.ars.qtype.question import Question

class TrueFalse(Question):
    def __init__(self, question, answer, explanation=""):
        super().__init__(question, answer)
        if not isinstance(answer, bool):
            raise ValueError("The answer must be a boolean (True or False).")
        self._explanation = explanation

    def ask(self):
        super().ask()
        return f"{self._question} (True/False)"

    def check_answer(self, answer):
        normalized_answer = answer.strip().lower()
        if normalized_answer in ["true", "t"]:
            user_answer = True
        elif normalized_answer in ["false", "f"]:
            user_answer = False
        else:
            raise ValueError("Answer must be 'True' or 'False'.")
        return user_answer == self._answer

    def incorrect_feedback(self):
        return f"Incorrect. {self._explanation}" if self._explanation else "Incorrect."
 
