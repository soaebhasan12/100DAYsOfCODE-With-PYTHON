# 011 The hirst Painting Part 2 - Drawing the Dots


import turtle as turtle_module
import random

color_list = [
    (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69),
    (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
    (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
    (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62),
    (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
    (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
    (65, 231, 239), (217, 88, 51)
]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    # timmy.dot(size_of_dot, color)
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()