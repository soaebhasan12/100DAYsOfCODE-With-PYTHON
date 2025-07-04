import turtle

screen = turtle.Screen()
screen.title("U.S. States Games")
image = r"005 Day-25 us-states-game-start\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




## Function to get the coordinate of map/screen using function.
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()



anshwer_state = screen.textinput(title="Guess the States", prompt="What's another state's name?")
print(anshwer_state)