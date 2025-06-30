from turtle import Turtle, Screen
from Snake_003 import Snake
from Food_003 import Food

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Challenge 1 : Create 3 turtle and position them like so.
# Each turtle should be a white square (default size: 20x20).

# Challenge 2 : Create a class Snake() and paste the code, need to be in that class from here.

# Challenge 3 : Control the snake with the keypress.

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.001)
    snake.move()

    # Challenge 02: Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()

        
screen.exitonclick()