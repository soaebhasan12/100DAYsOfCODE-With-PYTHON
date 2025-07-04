# 005 Write the Ball Class and Make the Ball Move

# Challenge 05: Create the Ball and make it move

from turtle import Turtle, Screen
from e_Paddle_005 import Paddle
from e_Ball_005 import Ball
import time


screen = Screen()
screen.tracer(0)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

moving_ball = Ball((0, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    moving_ball.move()


screen.exitonclick()