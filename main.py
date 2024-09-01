from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def reset ():

   window.after_cancel(timer)
   canva.itemconfig(timer_text,text="00:00")
   title_label.config(text="Timer")
   check_marks.config(text="")
   global  reps
   reps = 0


def start_timer ():
    global reps
    reps +=1
    work_sec =WORK_MIN*60
    short_break_sec =SHORT_BREAK_MIN *60
    longbreak_sec =LONG_BREAK_MIN *60

    if reps% 8 == 0:
        count_down(longbreak_sec)
        title_label.config(text="chill",fg= GREEN,bg =YELLOW,font=(FONT_NAME,50))
    elif reps % 2== 0:
        count_down(short_break_sec)
        title_label.config(text="break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
    else:
        count_down(work_sec)
        title_label.config(text="work", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))





def count_down(count):
    count_min =math.floor(count/60)
    count_sec = count %60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count >0 :
        global timer
        timer = window.after(1000,count_down,count-1)

    else :
          start_timer()
          mark =""
          work_sessions =math.floor(reps/2)
          for _ in range(math.floor(reps/2)):
              mark +="✓"
    check_marks.config(text = "marks")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pom")
window.config(padx= 100,pady=50,bg =YELLOW,highlightthickness=0)




title_label =Label(text="Timer",fg= GREEN,bg =YELLOW,font=(FONT_NAME,50))
title_label.grid(column = 1,row = 0)
canva  =Canvas(width = 200 ,height= 224,bg=YELLOW)

img  =PhotoImage(file ="tomato.png")
canva.create_image(103,112,image =img )
timer_text= canva.create_text(103,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canva.grid(column =1 ,row =1 )

start_button =Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column =0 ,row = 2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column =2 ,row =2)

check_marks = Label(fg=GREEN,bg = YELLOW)
check_marks.grid(column =1 ,row =3)






window.mainloop()