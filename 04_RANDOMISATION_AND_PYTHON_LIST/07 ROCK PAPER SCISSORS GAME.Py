# PROJECT : ROCK PAPER SCISSORS GAME.

import random

rock = '''
    ________
---'    ____)
       (_____)
       (______)                 "ROCK"
       (_____)
----.__(___)
        
'''

paper = '''
    ________
---'    ____)____
        _________)
        __________)             "PAPER"
        ________)
----._____)
        
'''

scissor = '''
    __________
---'     _____)___________
            ______________)
         _________________)     "SCISSORS"
        (_________)
----.___(_________)
        
'''

game_images = [rock, paper, scissor]

user_choices = int(input("What do you choose ? Type 0 for Rock, 1 for Paperor 2 for Scissors."))

print('Your Chose ')

if (user_choices >= 3 or user_choices < 0) :
    print("Ivalid Choice..")
else :
    print(game_images[user_choices])
    computer_choice = random.randint(0, 2)
    print('Computer Chose.')
    print(game_images[computer_choice])

    if ( user_choices == 0 and computer_choice == 2 ):
        print("You Wins")
    elif ( user_choices == 2 and computer_choice == 0 ):
        print("You Lose")
    elif ( computer_choice > user_choices):
        print("You Lose")
    elif ( user_choices > computer_choice ):
        print("You Win")
    elif ( user_choices == computer_choice ):
        print("It's a Draw")
