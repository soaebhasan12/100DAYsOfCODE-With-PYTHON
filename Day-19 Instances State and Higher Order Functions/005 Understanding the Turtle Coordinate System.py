from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x = -230 , y = y_position[turtle_index])



screen.exitonclick()















"""
1. Python set() Function Explanation:-
2. Definition
🔹 The set() function in Python is used to create a set, which is an unordered collection of unique elements.

🔹 It automatically removes duplicate values and stores only distinct items.

3. Key Features
✅ Unordered: Elements are not stored in a specific sequence.

✅ Unique Elements: Duplicate values are automatically removed.

✅ Mutable (Changeable): You can add or remove elements.

✅ Supports Mathematical Operations: Like union, intersection, and difference.

✅ Fast Lookups: Checking if an element exists is faster compared to lists.

4. Common Use Cases
🔸 Removing duplicate values from a list.

🔸 Performing set operations like union, intersection, and difference.

🔸 Checking membership (element in set).

🔸 Optimizing searches due to its fast lookup time.

5. Important Notes
⚠️ Elements inside a set must be immutable (unchangeable), meaning you can store numbers, strings, and tuples, but not lists or dictionaries.

⚠️ Since sets are unordered, you cannot access elements using an index like lists.

In short, set() is useful when you need a collection of unique values and want to perform fast membership checks or mathematical set operations. 🚀





1️⃣ textinput() Function in Python:-
1️⃣ Overview
🔹 textinput() ek method hai jo Turtle module me use hoti hai user se text input lene ke liye.
🔹 Yeh ek simple pop-up dialog box show karta hai jisme user text likh sakta hai.

2️⃣ Syntax
🔹 Iska basic structure hota hai:

turtle.textinput(title, prompt)

🔹 title: Dialog box ka title set karta hai.
🔹 prompt: User ko jo message dikhana hai.

3️⃣ Return Value
🔹 User jo bhi text input karega, yeh function string (str) format me return karega.
🔹 Agar user Cancel button dabata hai, toh yeh None return karega.

4️⃣ Use Cases
🔹 Interactive Turtle Graphics me user input lene ke liye.
🔹 User se naam ya koi aur detail lene ke liye.
🔹 Simple GUI-based Python applications me user se data lene ke liye.










1️⃣ goto() Function (Turtle Module)
1️⃣ Overview
🟢 goto() Turtle module ka function hai jo turtle ko kisi bhi specified (x, y) coordinates par move karne ke liye use hota hai.

2️⃣ Syntax
🟢 turtle.goto(x, y)
🔹 x → X-axis ka coordinate
🔹 y → Y-axis ka coordinate

3️⃣ Functionality
🟢 Turtle directly move karti hai bina pen uthaye
🟢 Agar pen down hai, toh turtle line draw karegi
🟢 Agar pen up hai, toh sirf position change hogi

4️⃣ Use Cases
✅ Specific position par shape ya pattern draw karne ke liye
✅ Turtle ka movement control karne ke liye










"""