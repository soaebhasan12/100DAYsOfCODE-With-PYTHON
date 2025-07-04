# 005 Write the Ball Class and Make the Ball Move

from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(position)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

