# 008 - Challege 2 - Search fo a Website in the Password Manager.





from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Challenge-1 (008) :
#               1). Modify the code to handle the FileNotFoundError.
#               2). Create a new data.json file if it does not exist.
#               3). If the file already exists, then simply add the new entry.

# Challenge-2 (009) : 
#               1). Add "Search" button next to the website entry field.

#               2). Adjust the layout and the other widgets as needed to get the desired look.

#               3). Create a function called find_password() that gets triggered 
#                   when the "Search" button is pressed. 

#               4). Check if the user's text entry matches an item in the data.json. 

#               5). If yes, show a messagebox with the website's name and password. 

#               6). Catch an exception that might occur trying to access the data.json showing 
#                   a messagebox with the text "Nod Data File Found".

#               7). If the user's website does not exist inside the data.json, show a messagebox
#                   that reads "No details for the website exists".

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                # data = json.load(data_file)
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    data = {}

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()                            
window.title("Passoword Manager")        
window.config(padx=50, pady=50)          

canvas = Canvas(width=200, height=200)        
logo_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/29 - Building a Password Manager GUI App with Tkinter/Coding Exercise/Python-Projects/Tkinter GUI Application of Password Manager/logo.png")           

# canvas.create_image(image=logo_img)                
canvas.create_image(100, 100, image=logo_img)        
canvas.grid(column=1, row=0)


# Labels:
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entry
website_entry = Entry(width=27)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "soaebhasan04@gmail.com")
password_entry = Entry(width=27)
password_entry.grid(column=1, row=3, columnspan=1)



# Button
search_password_button = Button(text="Search", width=13, command=find_password)
search_password_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()                                    