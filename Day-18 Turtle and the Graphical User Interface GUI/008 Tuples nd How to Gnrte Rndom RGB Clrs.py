# 008 Python Tuples and How to Generate Random RGB Colours


# Tuple:-
# Note: tuple is immutable, while list is mutable.
# Note: We can't change the item of tuple, it is like as a "Patthar ki lakeer".
# If we want to modify the tuple, we have to firstly change tuple into a list then modify the item then convert to the tuple.

import turtle as t
import random
from turtle import Screen

timmy = t.Turtle()
t.colormode(255)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]

timmy.pensize(15)

timmy.speed("fastest")

for _ in range(700):
    timmy.color(random_colors())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()










# What is setheading ?
"""
1. setheading() in Turtle Module
setheading() ek method hai jo Python ke Turtle module me use hoti hai. Ye method turtle ka direction (heading) set karne ke kaam aati hai.

2. Usage:-
Agar aap turtle ka mukammal direction ek fixed angle pe set karna chahte hain, to setheading(angle) ka use kar sakte hain.

Syntax:
turtle.setheading(angle)

📌 Yahan angle ek numerical value hoti hai jo degrees me di jati hai.


3. Direction Guide (Konse Angle Pe Kya Hoga?)

Angle (Degree)	    Direction (Turtle ka Rukh)
    0	                East (Right)
    90	                North (Up)
    180	                West (Left)
    270	                South (Down)
    
Example:-

    import turtle
    
    t = turtle.Turtle()
    
    t.forward(100)  # 100 steps forward
    t.setheading(90)  # Turtle ka rukh 90 degrees (North) pe set
    t.forward(100)  # Ab turtle upar jayega
    
    t.setheading(180)  # Turtle ka rukh 180 degrees (West) pe set
    t.forward(100)  # Ab turtle left jayega
    
    turtle.done()
    
    
📝 Output Explanation:
Pehle turtle right (east) move karega.
Phir setheading(90) se wo upar (north) move karega.
Phir setheading(180) se wo left (west) move karega.


4. Difference Between setheading() & left()/right()

    Method	                    Kaam
setheading(90)	            Direct 90-degree north set karega.
left(90)	                Current direction se 90-degree left move karega.
right(90)                   Current direction se 90-degree right move karega.

Agar exact direction set karni ho, to setheading() best hai. Agar bas rotate karna ho, to left() ya right() ka use karein.

5. Conclusion:-
🔹 setheading(angle) turtle ka bilkul exact direction set karta hai, bina current direction ka asar liye.
🔹 Ye robotics, simulation, aur graphics programming me kaafi useful hota hai.
🔹 left() aur right() sirf current position ke mutabiq angle change karte hain, jabke setheading() direct ek fixed angle pe set karta hai.
"""