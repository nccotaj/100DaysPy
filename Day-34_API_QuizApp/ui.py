from tkinter import *

THEME_COLOR = "#375362"
FONT = "Arial"

class QuizInterface:

    def __init__(self):  #reminder: initi function is called everytime we create an opject of this class
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)

        #Score label
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)



        #Canvas/card
        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(150,125,text="Question Text",font=(FONT,20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        #True button
        true_icon = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_icon, command=self.placeholder, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        #False Button
        false_picture = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_picture, command=self.placeholder, highlightthickness=0)
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()

    def placeholder(self):
        print("button press")

quiz = QuizInterface()