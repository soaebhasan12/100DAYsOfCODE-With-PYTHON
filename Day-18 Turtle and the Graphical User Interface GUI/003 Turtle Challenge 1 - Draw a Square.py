from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("square")
timmy.color("Blue")

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)


# timmy.backward(100)
# timmy.left(90)


for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.forward(100)

# for _ in range(4):
#     timmy.backward(100)
#     timmy.left(90)
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


screen = Screen()
screen.exitonclick()