# Debug Leap Year Exercise...

# Instructions:-
    # 1.Read the Below Code.
    # 2.Spot the problem.
    # 3.Modify the code to fix the problem.
    # 4.No-Shortcuts - don't copy/paste to replace the code entirely with a solution.


############# CODE to DEBUG #############

year = input("Which year do you want to check?")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")





























############# DEBUGGED CODE #############

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else:
#             print("Not Leap Year.")
#     else:
#         print("Leap Year.")
# else:
#     print("Not Leap Year.")