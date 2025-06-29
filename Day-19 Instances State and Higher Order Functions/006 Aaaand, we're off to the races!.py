import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230 , y = y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! the {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! the {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
























"""
🧠 1. Module Imports

import turtle
from turtle import Turtle, Screen
import random

🔸 turtle module ek built-in Python library hai jo graphics draw karne ke liye use hoti hai, usually educational purpose ke liye.

🔸 from turtle import Turtle, Screen:
Humne specifically Turtle class (jo ek turtle ka object banata hai) aur Screen class (jo screen window handle karti hai) ko import kiya hai.

🔸 random module ka use hum yahan karenge turtle ki movement ko unpredictable banane ke liye (jaise real race hoti hai!).

🖼️ 2. Screen Setup and User Input

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

🔹 is_race_on = False:
Yeh ek flag hai jo batata hai race shuru hui hai ya nahi.

🔹 screen = Screen():
Yeh ek turtle screen window create karta hai, jisme sab kuch display hoga.

🔹 screen.setup(...):
500x400 pixels ka ek window banata hai — width = 500px, height = 400px.

user_bet = screen.textinput(
    title="Make your bet", 
    prompt="Which turtle will win the race? Enter a color: "
)

🔸 screen.textinput(...):
Yeh ek pop-up input box open karta hai jahan user se poocha jata hai ki kaunsa turtle color jeetega.

▶️ Return type: string (user ka diya hua color).

🎨 3. Turtle Setup (Colors and Positions)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

🔹 colors:
6 alag-alag colors define kiye gaye hain — yehi turtle ke rang honge.

🔹 y_position:
Har turtle ka vertical position (y-axis) different hoga taaki wo ek hi line me na ho.

🔹 all_turtle:
Yeh ek empty list hai jisme sabhi turtle objects store honge.


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230 , y = y_position[turtle_index])
    all_turtle.append(new_turtle)
    
🔸 Loop 6 turtles banata hai (index 0 se 5 tak):
1️⃣ Turtle(shape="turtle"):
Ek turtle object create karta hai aur uska shape actual turtle jaisa dikhata hai.

2️⃣ .color(...):
Turtle ka rang set karta hai list me se.

3️⃣ .penup():
Turtle ka pen utha leta hai taaki move karne se koi line draw na ho.

4️⃣ .goto(x=-230, y=...):
Sabhi turtles ko left edge par set karta hai x = -230 (starting point), aur y_position ke hisaab se vertical jagah alag hoti hai.

5️⃣ all_turtle.append(...):
Turtle ko list me add karta hai taaki aage race ke waqt sab ke upar loop chal sake.

🏁 4. Start the Race

if user_bet:
    is_race_on = True
    
👉 Agar user ne koi input diya hai (empty nahi chhoda), tab race ko True mark kar ke start kiya jata hai.

🐢 5. Race Simulation Loop

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
🔹 while is_race_on:
Jab tak race on hai, sab turtles ko randomly aage badhaya jayega.

🔹 turtle.xcor()
Yeh method current turtle ka horizontal position (x-coordinate) batata hai.
Agar koi turtle > 230 pahuch gaya, matlab wo race ki finish line tak pahuch gaya.

🔹 winning_color = turtle.pencolor()
Jeetne wale turtle ka color store kar lete hain — pencolor() uska current color deta hai.

🏆 6. Result Declaration

if winning_color == user_bet:
    print(f"You have won! the {winning_color} turtle is the winner!")
else:
    print(f"You have lost! the {winning_color} turtle is the winner!")
    
🔹 User ka guess agar sahi nikla to jeet gaye! Warna haar gaye.
Comparison dono strings ka hota hai (color name).

🏃 7. Turtle Moves Randomly

random_distance = random.randint(0, 10)
turtle.forward(random_distance)

🔹 random.randint(0, 10):
Har iteration me turtle ko 0 to 10 pixels randomly aage badhaya jata hai.

🔹 turtle.forward(...):
Actual movement turtle ka screen pe hota hai.

➡️ Ye randomness hi game ko exciting aur unpredictable banata hai.

👋 8. Exit on Click

screen.exitonclick()

🔹 Screen window tab tak open rahegi jab tak user uspe click nahi karta.
Isse window immediately close nahi hoti — user dekh sakta hai result.

"""