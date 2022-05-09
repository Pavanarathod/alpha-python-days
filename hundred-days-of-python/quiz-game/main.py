from questions_model import Question
from data import question_data
from quiez_brain import QuizeBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]

    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)


quiz = QuizeBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()