# Debug Fizz Buzz Exercise.

# Instruction:
    # 1.Read the Below Code.
    # 2.Spot the problem.
    # 3.Modify the code to fix the problem.
    # 4.No-Shortcuts - don't copy/paste to replace the code entirely with a solution.


############# CODE to DEBUG #############

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fuzz")
    if number % 5 == 0:
        print("Bizz")
    else:
        print([number])



































############# DEBUGGED CODE #############

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fuzz")
#     if number % 5 == 0:
#         print("Bizz")
#     else:
#         print([number])