"""Module for the Box class in the Adaptive Review System."""
from datetime import timedelta, datetime
from typing import List, Optional
from question import Question

class Box:
    def __init__(self, name, priority_interval):
        self._name = name
        self._priority_interval = priority_interval
        self._questions = []

    @property
    def name(self):
        return self._name

    @property
    def priority_interval(self):
        return self._priority_interval

    def add_question(self, question):
        if question not in self._questions:
            self._questions.append(question)

    def remove_question(self, question):
        if question in self._questions:
            self._questions.remove(question)

    def get_next_priority_question(self) -> Optional[Question]:
        sorted_questions = sorted(self._questions, key=lambda q: q.last_asked or datetime.min)
        now = datetime.now()
        for question in sorted_questions:
            if question.last_asked is None or (now - question.last_asked) >= self._priority_interval:
                return question
        return None

    def __len__(self):
        return len(self._questions)

    def __str__(self):
        return f"Box(name='{self._name}', questions_count={len(self._questions)})"
