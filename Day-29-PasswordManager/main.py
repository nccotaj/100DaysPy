from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers




    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_fields():
    web_entry.delete(0,END)  #clears from 0 index to end
    password_entry.delete(0,END) 

def save():
    website = web_entry.get()
    username = user_entry.get()
    password = password_entry.get()
    line = f"{website} | {username} | {password}\n "

    if len(website) != 0 and len(username) != 0 and len(password) != 0:


        is_ok = messagebox.askokcancel(title=website, message=f"Save? \nWebsite: {website} \nUsername: {username} \nPassword: {password}")

        if is_ok:
            with open("passwords.txt", mode="a") as file:
                file.write(line)
                clear_fields()
    else:
        messagebox.showwarning(title="Empty Fields", message="One or more fields is empty")

    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Mangaer")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo) #first two args are for x,y position
canvas.grid(row=0,column=1)

##### Website label/Entry box
web_label = Label(text="Website")
web_label.grid(row=1, column=0, sticky="e")

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2, sticky="ew")




####### Email/Username
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0, sticky="e")

user_entry = Entry(width=35)
user_entry.insert(0, "nccotaj@gmail.com")  #0 inserts the cursor at the beginning of text box
user_entry.grid(row=2, column=1, columnspan=2, sticky="ew")



###### Password/Generate Passowrd
password_label = Label(text="Password")
password_label.grid(row=3, column=0, sticky="e")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=3,column=2, sticky="ew")


###### Add
add = Button(text="Add", width=36, command=save)
add.grid(row=4,column=1, columnspan=2, sticky="ew")

window.mainloop()