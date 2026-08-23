import tkinter
from pickle import GLOBAL
from tkinter import *
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
timer_countdown = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    start.config(state="normal")

    global marks
    window.after_cancel(timer_countdown)
    canvas.itemconfig(timer_text,text= "00:00")
    tick_mark.config(text = "")
    timer.config(text = "Timer")
    marks = ""
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_on():
    start.config(state="disabled")

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        if reps % 8 == 0:
            timer.config(text = "Break", fg = RED)
            count_down(long_break_sec)
        timer.config(text = "Break", fg = PINK)
        count_down(short_break_sec)
    else:
        timer.config(text = "Work", fg = GREEN)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text,text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        global timer_countdown

        timer_countdown = window.after(1000, count_down, count-1)

    else:
        global marks
        timer_on()
        marks = ""
        for _ in range(reps //2):
            marks += "✔"
        tick_mark.config(text= marks)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg = YELLOW)
canvas = Canvas(width=200, height=224,bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer = Label(text="Timer", font= (FONT_NAME, 40, "bold"), bg = YELLOW,fg = GREEN,highlightthickness=0)
timer.grid(column=1, row=0)

tick_mark = Label(text = "", font= (FONT_NAME, 15, "bold"), bg = YELLOW,fg = GREEN,highlightthickness=0)
tick_mark.grid(column=1, row=3)

start = Button(text="Start",command = timer_on)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=timer_reset)
reset.grid(column=3, row=2)


window.mainloop()
