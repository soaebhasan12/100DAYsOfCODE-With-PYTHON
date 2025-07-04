# 003 Create a Paddle that responds to Key Presses copy

# Cahllenge-01: Create the Screen
# Challenge-02: Create and move a paddle


from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")

paddle = Turtle()

r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))


paddle.color("white")
paddle.shape("square")

paddle.shapesize(stretch_wid=5, stretch_len=1)

paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()