
from tkinter import *
import sys
import os
import winsound
from plyer import notification

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None   #we need to be able to access the timer vaiable outside of the count_down function, so we declare it as a global variable with
               #value of None so that we define its value in the count_down function but can access it in the reset_timer function


#----For EXE-----#

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



#-----FOR NOTIFICATION-----#
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # notification disappears after 10 seconds
    )


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, timer


    window.after_cancel(timer)   #we are canceling the timer variable in the countdwon function
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text=f"25:00")
    checkmark.config(text="")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():


    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, timer
    
    
    count_min = int(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    




    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000,count_down, count - 1)   #wait for 1000ms, then calls function countdown and passes in count-1, THIS IS GLOBAL
    else:
        reps += 1
        
        winsound.MessageBeep()  #plays a sound when the timer is done
        if reps % 2 == 0:
            show_notification("Pomodoro", "Work session done! Time for a break 🍅")
        else:
            show_notification("Pomodoro", "Break is over! Time to work 🍅")

        marks = ""
        work_sessions = int(reps/2)
        for x in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)
        start_timer()
        



# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg = YELLOW) 



#Image 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("tomato.png")) #Turns our image into a PhotoImage class
canvas.create_image(100,112, image = tomato_img) #must pass a image of type PhotoImage into the image variable
timer_text = canvas.create_text(100,130, text="25:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#Title Text
title_label = Label(text="Timer")
title_label.config(fg=GREEN,bg=YELLOW, font=(FONT_NAME,45,"bold"))
title_label.grid(column=1,row=0)

#start and reset
start = Button(text="Start", command=start_timer)
start.config(highlightthickness=0)
start.grid(column=0,row=2)

reset = Button(text="Reset", command=reset_timer)
reset.config(highlightthickness=0)
reset.grid(column=2, row=2)

#Checkmark
checkmark = Label()
checkmark.config(fg=GREEN, bg=YELLOW, font=(15))
checkmark.grid(column=1,row=3)


window.mainloop()   #since we have mainloop we cant always do another loop or else it may not reachy the main loop. so we work around using the .after method which allows us to call a function after a certain amount of time. This is how we implement the countdown timer.