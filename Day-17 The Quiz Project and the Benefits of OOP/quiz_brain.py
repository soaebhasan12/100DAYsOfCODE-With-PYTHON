# 007 Quiz Part 3 The QuizBrain and the next_question() Method
    # 01. Create a class called QuizBrain.
    # 02. write an __int__() method.
    # 03. initialise the  question_number to 0.
    # 04. initialise the question_list to an input.

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # 008 Part-04 How to continue showing new Questions
        # 01. Create method called still_has_question().
        # 02. Return a boolean depending on value of question_number.
        # 03. Use the while loop (inside main.py) to show the next question until the end.

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False


    # 007 Part-03 The QuizBrain and the next_question() Method:
        # 0. Create a methode next_question() inside the QuizBrain class
        # 1. Retrieve the item at the current question_number from the question_list.
        # 2. Use the input() function to show the user the Question text and ask for the user's answer.

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # 009 Part-05 Checking Answers and Keeping Score:

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")
