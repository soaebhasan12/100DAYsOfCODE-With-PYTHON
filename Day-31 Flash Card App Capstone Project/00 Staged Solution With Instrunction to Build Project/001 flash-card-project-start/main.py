from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.minsize(width=800, height=526)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/001 flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image = card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

corss_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/001 flash-card-project-start/images/wrong.png")
unknown_button = Button(image=corss_img, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/31 - Flash Card App Capstone Project/Day - 31 Flash Card App Capstone Project/Resources/00 Staged Solution Code/001 flash-card-project-start/images/right.png")
known_button = Button(image=check_img, highlightthickness=0)
known_button.grid(column=1, row=1)











window.mainloop()