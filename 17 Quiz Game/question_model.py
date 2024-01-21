from data import question_data
from quiz_brain import Question


class QuestionModel:
    def __init__(self):
        """Create a list of Question classes."""
        self.questions = [Question(data["text"], data["answer"]) for data in question_data]
        self.question_num = 0
        self.score = 0

    def next_question(self):
        """Return the next Question instance."""
        try:
            question = self.questions[self.question_num]
        except IndexError:
            return None
        self.question_num += 1
        return question

    def check_answer(self, question: Question, user_answer: str):
        """Check the user's answer. If correct return True, else return False."""
        if user_answer.title() == question.answer:
            self.score += 1
            return True
        return False

    def get_score(self):
        """Return current score."""
        return self.score
