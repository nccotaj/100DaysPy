from turtle import Turtle, Screen

tim = Turtle() #create turtle object from Turtle() class
screen = Screen() #create screen object form Screen() class

#function to move forward
def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen() #listens for user input 
screen.onkey(key="w", fun=move_forward) #event listener, needs a key and function with no argumetn  (example of passing a function into another fucntion). We used keyword arguments here
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

#Higher order functions take another function in as a an input
