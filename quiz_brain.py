class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer,question.answer)


    def check_answer(self,user,correct):
        if user.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

