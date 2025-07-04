from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution With Instrunction to Build Project/003 flash-card-project/data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_backgorund, image=card_front_img)
    window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_backgorund, image=card_back_img)




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution With Instrunction to Build Project/003 flash-card-project/images/card_front.png")
card_back_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution With Instrunction to Build Project/003 flash-card-project/images/card_back.png")

# canvas.create_image(400, 263, image = card_front_img)
card_backgorund = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

corss_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution With Instrunction to Build Project/003 flash-card-project/images/wrong.png")
unknown_button = Button(image=corss_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution With Instrunction to Build Project/003 flash-card-project/images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)


next_card()








window.mainloop()