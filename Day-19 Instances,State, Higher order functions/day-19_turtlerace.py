from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500, 400) #sets size of scren (x,y)
bet = screen.textinput(title = "Make Bet", prompt = "Enter Color")  #take in user input for the bet


colors = ["red", "blue", "green", "orange", "yellow", "purple"]
starting_y = [-100,-70,-40,-10,20,50]
turtle_list = []


for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y=starting_y[i])
    new_turtle.speed("fastest")
    turtle_list.append(new_turtle)


if bet:
    race_on = True

while race_on:
    

    for i in turtle_list:

        if i.xcor() > 230:
            race_on = False
            print(i.pencolor())
            winning_color = i.pencolor()
            if i.pencolor() == bet:
                print("You win")
            else:
                print(f"You Lost. Winning turtle was {winning_color}")

        random_dist = random.randint(0,10)
        i.forward(random_dist)

screen.exitonclick()