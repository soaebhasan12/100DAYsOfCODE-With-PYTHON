from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Challenge 1 : Create 3 turtle and position them like so.
# Each turtle should be a white square (default size: 20x20).

# # Solution 01 :-

# x_position = [0, -20, -40]
#
# for turtle_index in range(0, 2):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.pen()
#     new_turtle.goto(x = x_position[turtle_index], y = 0)



# # Solution 02 :-

# segment_1 = Turtle(shape="square")
# segment_1.color("white")
# segment_1.goto(x = 0, y = 0)
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(x = -20, y = 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(x = -40, y = 0)



# # Solution 03 :-

starting_position = [(0,0), (-20,0), (-40,0)]

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)












screen.exitonclick()