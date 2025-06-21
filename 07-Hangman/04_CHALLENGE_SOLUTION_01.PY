# Step 1

import random

word_list = ["ardvark", "baboom", "camel"]


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable chosen_word.

chosen_word = random.choice(word_list)


# TODO-2 - Ask the user to guess a letter and assign their anshwer to a vaiable called guess. Make guess lowercass

guess = input("Guess any Letter of the Word : ").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else :
        print("Wrong")
        







"""
chosen_word = random.randon(word_list)

guess = input("Guess any Letter of the Word : ")

for i in range(chosen_word):
    if chosen_word[i] == chosen_word:
        print("Right")
else:
    print("Wrong")

"""