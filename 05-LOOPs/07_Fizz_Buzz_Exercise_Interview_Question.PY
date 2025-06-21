# EXERCISE : Fizz Buzz Exercise, Interview Question

for num in range (1, 101):
    if (num % 3 == 0 and num % 5 == 0):
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else :
        print(num)