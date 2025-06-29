# Challenge: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")

# First Solution:-

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)




## Second Solution:-

# timmy.right(120)
# # triangle
# for _ in range(3):
#     timmy.forward(100)
#     timmy.right(120)
#
#
# # Square:-
# for _ in range(4):
#     timmy.color("blue")
#     timmy.forward(100)
#     timmy.right(90)
#
#
# # Pentagon
# for _ in range(5):
#     timmy.color("red")
#     timmy.forward(100)
#     timmy.right(72)
#
# # hexagon
# for _ in range(6):
#     timmy.color("green")
#     timmy.forward(100)
#     timmy.right(60)
#
# # heptagon
# for _ in range(7):
#     timmy.color("black")
#     timmy.forward(100)
#     timmy.right(51.4285)
#
#
# # octagon
# for _ in range(8):
#     timmy.color("darkgreen")
#     timmy.forward(100)
#     timmy.right(45)
#
#
# # nonagon
# for _ in range(9):
#     timmy.color("purple")
#     timmy.forward(100)
#     timmy.right(40)
#
#
# # decagon
# for _ in range(10):
#     timmy.color("purple")
#     timmy.forward(100)
#     timmy.right(36)

screen = Screen()
screen.exitonclick()