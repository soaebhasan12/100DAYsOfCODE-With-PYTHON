# Turtle Event Listeners
# Write down the summary of this lecture, this is very important

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.exitonclick()





# Below code explain the working of above code:

# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# def calculator(n1, n2, func):
#     return func(n1, n2)
#
# result = calculator(5,6, add)
# print(result)















"""
Summary of the Lecture:-

🎯 Event Listeners & Higher-Order Functions in Python
1️⃣ Event Listeners Kya Hote Hain?
Event listeners basically user ke inputs ko sunte hain aur koi action perform karte hain jab ek specific event hota hai. Jaise:

Keyboard event: Jab koi key press hoti hai.

Mouse event: Jab koi button click hota hai.

Example: turtle library me event listener ka use karke keyboard se turtle ko move karna:

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# Event listener set karna
screen.listen()
screen.onkey(move_forward, "space")

screen.exitonclick()


🔍 Breakdown:

1. screen.listen() → Screen ko sunne ke mode me daal diya.

2. screen.onkey(move_forward, "space") → Jab space key dabayi jaye to move_forward function chale.

3. screen.exitonclick() → Click karne par window close ho.



2️⃣ Higher-Order Functions Kya Hote Hain?

Python me functions ko arguments ki tarah pass kar sakte hain, ise higher-order functions kehte hain.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator(n1, n2, func):
    return func(n1, n2)  # Jo function pass hoga, wahi execute hoga

# Function pass karna
print(calculator(5, 3, add))  # Output: 8
print(calculator(5, 3, subtract))  # Output: 2



🔍 Breakdown:

calculator(n1, n2, func) → Ek function as input leta hai.

Jab add pass karenge, addition hoga. Jab subtract pass karenge, subtraction hoga.

Event listeners bhi isi tarah kaam karte hain! Jaise screen.onkey(move_forward, "space") me "space" press hone par move_forward() call hota hai.

🎯 Samajhne Ka Naya Tareeka!
Event listeners = Code jo user ke actions ka wait kare.

Higher-order functions = Function jo dusre functions accept kare.

Turtle + Event Listeners ka use karke interactive games bhi bana sakte hain! 🐢🎮
🔹 Example: Ek calculator jo different functions accept kare:
"""