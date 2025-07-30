class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user_1 = User("001", "Soaeb")
user_2 = User("002", "Afjal")






"""
1. Object Attributes
Attributes object ke andar stored values hoti hain jo uske properties ko define karti hain.
Hum dot notation (.) ka use karke attributes ko assign kar sakte hain:

class User:
    pass  # Empty class

user_1 = User()
user_1.id = "001"
user_1.username = "Ali"
print(user_1.username)  # Output: Ali

Yahaan user_1 object hai aur humne manually id aur username set kiye.


2. Problem with Manual Attributes
Har naye object ke liye alag-alag manually attributes set karna error-prone aur time-consuming hota hai.

Example:

user_2 = User()
user_2.id = "002"
user_2.username = "Jack"

Agar naam galat likh diya user_2.usernmae to error aayega!


3. Constructor (__init__ method)
Constructor ek special function hota hai jo automatically chalta hai jab koi naya object create hota hai.

Python me constructor ko __init__ method ke naam se likhte hain:

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user_1 = User("001", "Ali")
user_2 = User("002", "Jack")

print(user_1.username)  # Output: Ali
print(user_2.username)  # Output: Jack

Yahaan har user ka attribute initialization automatic ho gaya!

self ka matlab hota hai current object.


4. Constructor ka Fayda (Benefit)
Har object ek hi tareeke se initialize hota hai.

Error chance kam ho jata hai (wrong spelling ya missing attributes nahi rahte).

Code short aur clean lagta hai.


5. Real-Life Example
Agar ek Car class banaani ho jisme har gaadi ki seats aur color ho:

class Car:
    def __init__(self, seats, color):
        self.seats = seats
        self.color = color

car_1 = Car(5, "Red")
car_2 = Car(7, "Black")

print(car_1.color)  # Output: Red
print(car_2.seats)  # Output: 7

Ab har car ke liye automatically seats aur color set ho raha hai! 🎉


Conclusion
__init__ constructor object initialization ko easy aur error-free banata hai.

Har object apne unique values ke saath ban sakta hai bina manual attributes likhne ke.

Ye OOP ka ek fundamental concept hai jo aage bohot kaam aayega! 🚀
"""