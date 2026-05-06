from turtle import Turtle, Screen
import turtle
import random

#import these classes 


tim = Turtle()
tim.shape("classic")
tim.color("red")
# tim.pensize(5)
tim.speed("fastest")

#Draw a square

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

#or

# for item in range(4):
#     tim.forward(100)
#     tim.right(90)


#Draw a dashed line
# for item in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

#Challenge: Different Shapes


colors = ("blue","red","green","pink","purple","brown","black","grey","deep pink") #Tuple is Similar to a list. It is Immutable unlike a list tho, they also use parentheses

# def draw_shape(num_sides):
#      angle = 360/num_sides
#      for item in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for sides in range(3,11): #range from 3 to 10
#     tim.color(random.choice(colors))
#     draw_shape(sides)

#Challenge: Random Walk
directions = [0,90,180,270]


turtle.colormode(255)

def random_color(): #returns a touple with rgb val
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r,g,b)
    return random_color

# for i in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())



#Challenge: Spirograph

def draw_spirograph(size_gap):

    for i in range(int(360/size_gap)):
        tim.setheading(tim.heading() + size_gap)
        tim.circle(100)
        tim.color(random_color())

draw_spirograph(40)

screen = Screen()















screen.exitonclick()