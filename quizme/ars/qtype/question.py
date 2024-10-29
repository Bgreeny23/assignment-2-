"""Module for the base Question class in the Adaptive Review System."""
import uuid
from datetime import datetime
from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, question, answer):
        self._id = uuid.uuid4()
        self._question = question
        self._answer = answer
        self._last_asked = None

    @property
    def id(self):
        return self._id

    @property
    def last_asked(self):
        return self._last_asked

    def ask(self):
        self._last_asked = datetime.now()
        return self._question

    def reset(self):
        self._last_asked = None

    @abstractmethod
    def check_answer(self, answer):
        pass

    @abstractmethod
    def incorrect_feedback(self):
        pass

    def __eq__(self, other):
        return isinstance(other, Question) and self._id == other.id

    def __hash__(self):
        return hash(self._id)
