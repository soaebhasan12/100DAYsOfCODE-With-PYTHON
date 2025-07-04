from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/002 flash-card-project\data/french_words.csv")

to_learn = data.to_dict(orient="records")

print(to_learn)


def next_card():
    curent_card = random.choice(to_learn)
    
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=curent_card["French"])



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.minsize(width=800, height=526)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/001 flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

corss_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/001 flash-card-project-start/images/wrong.png")
unknown_button = Button(image=corss_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/001 flash-card-project-start/images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)


next_card()








window.mainloop()