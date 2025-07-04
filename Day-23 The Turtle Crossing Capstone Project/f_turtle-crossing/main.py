# Challenge-01: Move the turtle with keypress (player.py).
# Challenge-02: Create and move the cars (car_manager.py).
# Challenge-03: Detect collision with car (car_manager.py).
# Challenge-04: Detect when turtle reaches the other side (player.py) and increase the speed of the cars after reaching to the other side of the game(car_manager.py).
# Challenge-05: Create Scoreboard (scoreboard.py).



import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successfull crossing
    if player.is_finish_line():
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()