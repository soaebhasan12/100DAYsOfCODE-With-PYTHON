from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Challenge 1 : Create 3 turtle and position them like so.
# Each turtle should be a white square (default size: 20x20).

starting_position = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)










screen.exitonclick()