# How to Open, Read, and Write to Files using the "with" Keyword


## Reading from file(2 methode):

## Methode-01: 

# file = open("003_my_file.txt")
# content = file.read()
# print(content)

# file.close()


## Methode-02 (using "with" keyword): 

with open("003_my_file.txt") as file:
    content = file.read()
    print(content)





## Writing in a file:

## Methode-01("write" mode):

# with open("003_my_file.txt", mode="w") as file:
#     file.write("New Text.")


## Methode-01("append" mode):

# with open("003_my_file.txt", mode="a") as file:
#     file.write("\nNew Text.")

with open("003_my_new_file.txt", mode="a") as file:
    file.write("\nNew Text.")