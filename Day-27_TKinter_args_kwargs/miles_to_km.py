from tkinter import *

window = Tk()
window.title("Miles to KM")
window.config(padx=20,pady=20)

## Entry Box
def calculate():
    mile = float(input.get())
    km = mile * 1.609
    value.config(text=f"{km}")


input = Entry(width=10)
input.grid(column=1, row=0)


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0,row=1)

value = Label(text="0")
value.grid(column=1, row=1)

unit_km = Label(text="km")
unit_km.grid(column=2, row=1)

calc = Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)





window.mainloop()