import turtle
import pandas

from turtle import Turtle

screen = turtle.Screen()

screen.title("US State Quiz")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

correct_states = []

def place_state(name,xcor,ycor):
    state = Turtle()
    state.hideturtle()
    state.penup()
    state.goto(xcor,ycor)
    state.write(f"{name}", False, align="center")
    

    

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()



while len(correct_states) < 50:
    if correct_states == 0:
        answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    else:
        answer = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?")

    
    
    if answer is None or answer.lower() == "exit":
        missed_states = list(set(state_list) ^ set(correct_states))
        states_to_Learn = pandas.DataFrame(missed_states)
        states_to_Learn.to_csv("states_to_learn.csv")
        break

    answer = answer.title()

    selection = data[data.state == answer]
    if not selection.empty:
        place_state(selection.state.item(), selection.x.item(), selection.y.item())
        correct_states.append(answer)
    else:
        print("Selection not found")




turtle.mainloop()