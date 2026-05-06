# import colorgram

# colors = colorgram.extract('hirst.jpg',30)



# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r,g,b)  #tupple for the colors

#     rgb_colors.append(new_color) #append the color tupple to the list

# print(rgb_colors)

#list of colors that we got from the rgb_colors list (removed the white background colors)

from turtle import Turtle, Screen
import turtle

color_list = [(46, 104, 159), (144, 179, 190), (225, 171, 125), (184, 148, 160), (125, 81, 90), (127, 73, 53), (37, 48, 65), (111, 174, 125), (214, 80, 58), (70, 6, 23), (40, 131, 105), (176, 102, 149), (238, 186, 135), (84, 98, 181), (64, 52, 45), (118, 41, 55), (218, 172, 179), (235, 177, 154), (180, 189, 210), (85, 153, 111), (79, 56, 52), (70, 65, 54), (23, 77, 101), (167, 204, 185), (166, 201, 205), (53, 59, 77)]

tim = Turtle()
tim.shape("classic")
tim.speed("fastest")

turtle.colormode(255)

tim.penup()
tim.hideturtle()
# tim.dot(20, (125,81,90))
# tim.forward(50)
# tim.right(90)
# tim.forward(50)
# tim.dot()
# tim.right(90)
# tim.teleport(0,0)

ypos = 0
current_colorIndex = 0
for i in range(10):
    for j in range(10):
        tim.dot(20, color_list[current_colorIndex])
        tim.forward(50)

        if current_colorIndex == len(color_list) - 1:
            current_colorIndex = 0
        else:
            current_colorIndex += 1

    ypos += 50
    tim.teleport(0, ypos)

screen = Screen()
screen.exitonclick()
