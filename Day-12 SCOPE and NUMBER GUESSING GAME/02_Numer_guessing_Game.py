# My Own Logic :-

import random
from art import logo

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

print("Welcom to the Number Guessing Game")
print("I am thinking of a number between 1 and 40.")
print(logo)

def easy_stage():
    rand_num = random.choice(lst)
    print(rand_num)
    attempts = 10
    for _ in range(0, 10):
        print(f"You have {attempts} remaining  to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == rand_num:
            print(f"You got it! The anshwer was {rand_num}")  
            break
        elif guess < rand_num:
            print("Too Low.")
            print("Guess again")
        elif guess > rand_num:
            print("Too High.")
            print("Guess again")
        attempts -= 1

def hard_stage():
    rand_num = random.choice(lst)
    print(rand_num)
    attempts = 5
    for _ in range(0, 5):
        print(f"You have {attempts} remaining  to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == rand_num:
            print(f"You got it! The anshwer was {rand_num}")  
            break
        elif guess < rand_num:
            print("Too Low.")
            print("Guess again")
        elif guess > rand_num:
            print("Too High.")
            print("Guess again")
        attempts -= 1    

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    easy_stage()
elif level == "hard":
    hard_stage()