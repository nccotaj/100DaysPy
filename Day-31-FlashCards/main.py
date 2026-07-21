from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
FONT_SIZE = 60
random_word = {}
flip_timer = NONE



#------------DATA HANDLE---------------#
try:
    word__data = pandas.read_csv("Data/words_to_learn.csv", usecols=["Spanish", "English"])

except FileNotFoundError:
    word__data = pandas.read_csv("Data/SpanishFrequency.csv", usecols=["Spanish", "English"])
finally:
    to_learn = word__data.to_dict(orient="records")  # gives us list of dictionaries


def known_word():
    to_learn.remove(random_word)

    word__data = pandas.DataFrame(to_learn)
    word__data.to_csv("Data/words_to_learn.csv")

    known_dict = {
        "English":[random_word["English"]],
        "Spanish":[random_word["Spanish"]]
    }

    known_df = pandas.DataFrame(known_dict)
    known_df.to_csv("Data/known_words.csv",mode='a',index=False)

    new_word()



#----------New Word-----------#

def new_word():
    global random_word, flip_timer

    window.after_cancel(flip_timer) #cancels the old flip_timer so that it restarts if we go to a newcard before the last timer completes


    random_word = random.choice(to_learn)

    spanish_word = random_word["Spanish"]
    
    canvas.itemconfig(canvas_image,image = card_front)
    canvas.itemconfig(word_text, text = spanish_word, fill = "black")
    canvas.itemconfig(title_text, text = "Spanish", fill= "black")

    flip_timer = window.after(3000,flip_card)

   

#------------Flip Card------------------#    
def flip_card():
    english_word = random_word["English"]
    canvas.itemconfig(canvas_image,image = card_back)
    canvas.itemconfig(title_text,text="English", fill="white")
    canvas.itemconfig(word_text, text = english_word, fill="white")





#--------------UI SETUP-----------------#
#Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

#Front Card
canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400,263, image = card_front)
title_text = canvas.create_text(400,150,text="", font=(FONT,40,"italic"))
word_text = canvas.create_text(400, 263,text="",font=(FONT,60,"bold"))


canvas.grid(column=0,row=0,columnspan=2)

#known button
known = PhotoImage(file="images/right.png")
known_buttonm = Button(image=known, command=known_word,highlightthickness=0)
known_buttonm.grid(row=1, column=1)

#unknown Button
unknown = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown, command= new_word,highlightthickness=0)
unknown_button.grid(row=1, column=0)



#Creates card_back image
card_back = PhotoImage(file="images/card_back.png")
new_word()














window.mainloop()