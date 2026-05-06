# from turtle import Turtle, Screen



# timmy = Turtle()
# print(timmy)  #Just says that the object is at a certain memory location
# timmy.shape("turtle")
# timmy.color("green")

# #Challenge: Move forward 100
# timmy.forward(100)

# #Attribute 
# my_screen = Screen()
# print(my_screen.canvheight) #Class attribute obj.atdribute  Also prints the height of this canvass

# #Methods   object.method()
# my_screen.exitonclick() #make it so we exit screen on click


#PrettyTable, gives us ASCII table

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water", "Fire"])


#Note how we are setting the attribute equal to something. Mehtods have ()
table.align = "l"

print(table)                       