# 006 Add the ball bouncing logic

# Cahllenge-01: Create the Screen
# Challenge-02: Create and move a paddle
# Challenge 03: Create another paddle
# Challenge 04: Create the Ball and make it move
# Challenge 05: Detect collision with wall and bounce

from turtle import Turtle, Screen
from f_Paddle_006 import Paddle
from f_Ball_006 import Ball
import time


screen = Screen()
screen.tracer(0)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
moving_ball = Ball()

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
    

    # Detect collision with wall
    if moving_ball.ycor() > 280 or moving_ball.ycor() < -280:
        print(moving_ball.y_move)
        print(moving_ball.x_move)
        moving_ball.bounce()
    


screen.exitonclick()