from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You completed the quiz. Your final score is {quiz.score}/{quiz.question_number}")