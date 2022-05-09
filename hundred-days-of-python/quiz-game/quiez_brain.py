class QuizeBrain:
    def __init__(self, question_list: list):
        self.question_number: int = 0
        self.question_list: list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
  

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans =  str(input(f"Q.{self.question_number}: {current_question.text} ('True/False'): "))
        self.check_answer(ans, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You Got it right")
        else:
            self.score -= 1
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"you'r current score is: {self.score}/{self.question_number}")
        print("\n")