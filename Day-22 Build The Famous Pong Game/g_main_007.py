# 007 How to detect collision with paddle.

# Cahllenge-01: Create the Screen
# Challenge-02: Create and move a paddle
# Challenge 03: Create another paddle
# Challenge 04: Create the Ball and make it move
# Challenge 05: Detect collision with wall and bounce
# Challenge 06: Detect collision with paddle (more challenging)

from turtle import Turtle, Screen
from g_Paddle_007 import Paddle
from g_Ball_007 import Ball
import time


screen = Screen()
screen.tracer(0)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with both paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()