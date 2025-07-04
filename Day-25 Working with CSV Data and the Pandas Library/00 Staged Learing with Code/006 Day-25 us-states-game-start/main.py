## U.S. States Game Part 2 Challenge with .csv

## Challenge-01: Convert the guess to Title case
## Challenge-02: Check if the guess is among the 50 states
## Challenge-03: Write correct guesses onto the map
## Challenge-04: Use a loop to allow the user to keep guessing
## Challenge-05: Record the correct guesses in a list
## Challenge-06: Keep track of the score

import turtle

screen = turtle.Screen()
screen.title("U.S. States Games")
image = r"005 Day-25 us-states-game-start\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



## Challenge-01: Convert the guess to Title case

# answer_state = screen.textinput(title="Guess the States", prompt="What's another state's name?")



## Challenge-02: Check if the guess is among the 50 states
import pandas

data = pandas.read_csv(r"006 Day-25 us-states-game-start\us-states-game-start\50_states.csv")


# all_states = data.state.to_list()
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # t.goto()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer_state)
    screen.exitonclick()
