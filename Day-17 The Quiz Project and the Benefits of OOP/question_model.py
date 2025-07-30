# Part-01 Creating the Question Class:
# Create a Question class with an __init__() method with two attributes: text and anshwer attribute

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
