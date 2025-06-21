# EXERCISE : ADDING EVEN NUMBERS

max_number = int(input("Enter the Most Biggest Number of your Series : "))
# min_number = input("Enter the Most Smallest Number of your Series : ")

# METHODE 01 :-

total = 0

for number in range (2, max_number+1, 2):
    total = total + number
print(f"Using first methode : {total}")

print()


# METHODE 02 :-

total2 = 0

for number in range(0, max_number+1):
    if number%2 == 0:
        total2 = total2 + number
print(f"By Second methode : {total2}")