class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Soaeb")
user_2 = User("002", "Afjal")


user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)










"""
Lecture Summary: Python Classes and Methods


1️⃣ Attributes and Methods in Classes
Attributes: Properties of an object (e.g., a car has seats).

Methods: Functions inside a class that define object behavior (e.g., changing seat count).


2️⃣ Example: Car Class with a Race Mode Method
A car usually has 5 seats, but in race mode, some seats are removed to reduce weight.

A method enter_race_mode() is created to set seats = 2.

Methods in a class look like normal functions but always take self as the first parameter.


3️⃣ Defining and Using Methods in a Class
Method structure:

def enter_race_mode(self):
    self.seats = 2
    
    
Calling a method using dot notation:

my_car.enter_race_mode()


4️⃣ Example: Instagram User Following System
A User has attributes:

followers = 0

following = 0

A method follow() increases the count when one user follows another.


5️⃣ Implementing the Follow Method

class User:
    def __init__(self):
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        
self.following → Increases for the user who follows.

user.followers → Increases for the user who is being followed.

6️⃣ Calling the Follow Method

user_1 = User()
user_2 = User()

user_1.follow(user_2)

print(user_1.followers, user_1.following)  # Output: 0 1
print(user_2.followers, user_2.following)  # Output: 1 0
user_1 follows user_2.

user_1’s following count becomes 1.

user_2’s followers count becomes 1.


7️⃣ Importance of self in Classes
self represents the instance (object) of the class.

Used inside class methods to modify object attributes.

Not needed when calling methods from an object.


💡 Key Takeaways:
✅ Attributes = Data inside an object.
✅ Methods = Actions an object can perform.
✅ self helps refer to object attributes inside the class.
✅ Use dot notation to call methods (object.method()).
"""