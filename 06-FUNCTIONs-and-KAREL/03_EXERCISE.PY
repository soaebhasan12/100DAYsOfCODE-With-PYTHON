# SOLUTION

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def master_move():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#master_move()
#master_move()
#master_move()
#master_move()
#master_move()
#master_move()

for step in range(0,6):
    master_move()