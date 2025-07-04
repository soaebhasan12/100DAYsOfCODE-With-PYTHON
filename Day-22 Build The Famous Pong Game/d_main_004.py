# 004-Write the Paddle Class and Create the Second Paddle.

# Cahllenge-01: Create the Screen
# Challenge-02: Create and move a paddle


from turtle import Turtle, Screen
from Codes.d_Paddle_004 import Paddle

screen = Screen()
screen.tracer(0)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()