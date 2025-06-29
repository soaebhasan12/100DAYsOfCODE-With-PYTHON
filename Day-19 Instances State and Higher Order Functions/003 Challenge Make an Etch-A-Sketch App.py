# Etch-A-Sketch App
# W = Forward
# S = Backward
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

from turtle import Turtle, Screen

timmy = Turtle()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()















"""
Summary of the Lecture:-

Yeh lecture Python ke turtle module ka use karke ek Etch-A-Sketch game banane ka challenge deta hai.
Is game me ek turtle cursor (Tim) hota hai jo keyboard ke keys (W, A, S, D) se move karta hai aur ek sketch board par drawing karta hai.

W se forward (aage)

S se backward (peeche)

A se left (counterclockwise) ghoomna

D se right (clockwise) ghoomna

C se screen clear + turtle ko center par wapas laana

Code Explanation - Term by Term
Chalo, ab har ek term aur concept ko detail me samajhte hain:

1. Turtle Module Import Karna

    import turtle


Yeh Python ka built-in module hai jo ek graphical window open karta hai jisme hum drawing ya shapes bana sakte hain.

2. Turtle Screen Create Karna

    screen = turtle.Screen()


Screen() ek window create karta hai jisme hamara turtle chalega.

Yeh main canvas hai jisme turtle drawings banayega.


3. Turtle Object Banana (Tim)

    tim = turtle.Turtle()


Turtle() se ek cursor (Tim) create hota hai jo draw karega.

Yeh ek chhoti si arrow jaisa dikhai deta hai jo commands follow karta hai.



6. Turn Left (Counterclockwise)

    def turn_left():
        new_heading = tim.heading() + 10
        tim.setheading(new_heading)

heading(): Turtle ki current direction (angle) return karta hai.

+10: Turtle ko left (counterclockwise) 10 degrees ghumata hai.

setheading(new_heading): Turtle ka naya angle set karta hai.

Jab bhi A key press hogi, turtle left ghoomega.



8. Clear Screen & Reset Turtle

    def clear():
        tim.clear()  # Drawing erase karega
        tim.penup()  # Pen uthayega taaki turtle wapas jaye bina line banaye
        tim.home()   # Turtle ko center (0,0) par wapas bhejega
        tim.pendown()  # Pen wapas neeche karega taaki drawing shuru ho sake


clear(): Screen se sab kuch hata dega (jo bhi turtle ne draw kiya).

penup(): Turtle ka pen uthata hai (taaki wapas aane par line na bane).

home(): Turtle ko origin (0,0) par wapas bhejta hai.

pendown(): Turtle ka pen wapas neeche rakhta hai (taaki wapas se draw kar sake).

Jab C key press hogi, sab kuch erase hoke turtle reset ho jayega.




Final Summary
Yeh pura program Turtle graphics + Event listeners ka use karke ek interactive Etch-A-Sketch game banata hai.

W, A, S, D keys turtle ko move karne ke liye hain.

C key screen clear + reset karti hai.

Turtle screen pe draw karta hai, aur user keyboard se drawing bana sakta hai.
"""