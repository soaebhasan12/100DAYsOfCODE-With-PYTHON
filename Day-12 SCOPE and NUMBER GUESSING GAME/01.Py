####### Scope ########

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")






####### Local Scope ########

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # This will give an error because potion_strength is a local variable and it is not accessible outside the function.







####### global Scope ########

player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health) # This will work because player_health is a global variable and it is accessible outside the function.






####### Namespace ########

# a namespace is a system that organizes and stores names for objects like variables, functions, and classes. Namespaces help to avoid naming conflicts and make it easier to differentiate between different entities in a program. 

# There are four types of namespaces in Python:

# Built-in namespace: Contains built-in functions and built-in exception names.
# Global namespace: Contains names from various imported modules that are used in the program.
# Enclosing namespace: Contains names of the local scope of any enclosing functions.
# Local namespace: Contains local names inside a function.
# Namespaces are created at different moments and have different lifetimes. The built-in namespace is created when the Python interpreter starts and is never deleted. The global namespace is created when the module is imported and lasts until the interpreter quits. The local namespace is created when the function is called and is deleted when the function returns.

# The order in which Python searches for a name is as follows:

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

drink_potion() # This will give an error because drink_potion is not defined in the global scope.
game() # This will work because drink_potion is defined in the local scope of the game function.
print(player_health) # This will work because player_health is defined in the global scope.







####### Does Python have BlockSpace ########

# Python does not have block-level scope. In other words, variables defined inside a block (such as an if statement or a loop) are still accessible outside that block. This is because Python uses indentation to define blocks of code, rather than curly braces or other block delimiters. As a result, variables defined inside a block are still part of the surrounding namespace.

game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy) # This will work because new_enemy is defined inside the if block, but it is still accessible outside the block.







game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy) # This will work because new_enemy is defined inside the if block, but it is still accessible outside the block.

print(new_enemy) # This will give an error because new_enemy is defined inside the create_enemy function and is not accessible outside the function.












####### How to Modify Variable with global Variable ########

# If you want to modify a global variable inside a function, you can use the global keyword to declare the variable as global. This allows you to modify the global variable from within the function.

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



# Best Practice: Avoid using global variables whenever possible, as they can make code harder to understand and maintain. Instead, pass variables as arguments to functions and return values from functions to update variables.

enemies = 2

def increase_enemies(enemies):
    return enemies + 1

enemies = increase_enemies(enemies)

print(enemies)















####### Python Constants and GLobal Scope ########

# pi = 3.14159

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@python"


# Overview: Constants are variables whose values should not be changed during the execution of a program. In Python, there is no strict way to define constants, as the language does not have a built-in constant type. However, it is a common convention to use uppercase variable names to indicate that a variable should be treated as a constant and not changed during the program's execution