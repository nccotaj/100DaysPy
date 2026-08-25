from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  #reminder: initi function is called everytime we create an opject of this class, Variable quiz_brain, must be of datatype QuizBrain (type hints)

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)

        #Score label
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)



        #Canvas/card
        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="Question Text",font=(FONT,15,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        #True button
        true_icon = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_icon, command=self.check_answer_true, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        #False Button
        false_picture = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_picture, command=self.check_answer_false, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def check_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

        

    def check_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

        

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.next_question)


    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)  #changes the text to the next question
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

