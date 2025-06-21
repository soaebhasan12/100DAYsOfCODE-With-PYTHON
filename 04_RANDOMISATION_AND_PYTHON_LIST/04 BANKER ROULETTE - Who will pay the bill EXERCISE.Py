# EXERCISE : BANKER ROULETTE - Who will pay the bill

# We can solve it by using two methods :

# i) Using str.split(',')

import random

names_string = input("Give me everybody's names, seperated by comma. ")

names = names_string.split(', ')

# get the total number of items
num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
