from turtle import Turtle, Screen
import pandas
# Image setup
image = "./giphy.gif"


# Setup Turtle and Screen
screen = Screen()
screen.setup(width=500, height=490)
screen.title("US States Finder")
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
title = screen.textinput(title="Guess the state", prompt="What state can you guess?")

#Setup Pandas
data = pandas.read_csv("states.csv")
states = data.state.to_list()


#do
if title in states:
    new_turtle = Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    state_data = data[data.state == title]
    new_turtle.goto(int(state_data.x), int(state_data.y))
    new_turtle.write(state_data.state.item())



#while loop 





# Keep the screen open
screen.mainloop()
