from turtle import Turtle, Screen
from Snake_004 import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Challenge 1 : Create 3 turtle and position them like so.
# Each turtle should be a white square (default size: 20x20).

# Challenge 2 : Create a class Snake() and paste the code, need to be in that class from here.

snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()












screen.exitonclick()