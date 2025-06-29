# Challenge: Draw a Random Walk
import turtle as t
import random
from turtle import Screen

timmy = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

timmy.pensize(15)

timmy.speed("fastest")

for _ in range(700):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()