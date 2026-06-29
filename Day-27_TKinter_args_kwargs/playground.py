import tkinter

window = tkinter.Tk()
window.title("Gui Program")
window.minsize(width=500, height=300)


#Lables

my_label = tkinter.Label(text="I Label", font=("Arial", 24, "italic"))
my_label.pack(side="bottom")      #pack automatically centers the component into the window

#different ways of changing the properties of a component
my_label["text"] = "New Text" #Like a dictionary
my_label.config(text="New New Text")


## BUTTONS
def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=button_clicked) #command calls name of funciton
button.pack()


## ENTRY component

input = tkinter.Entry(width=10)
input.pack()

#to retrieve the value of the input we need to use the .get method


window.mainloop() #keeps the window running, must be at end of program