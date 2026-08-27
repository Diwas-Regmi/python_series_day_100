import tkinter
from tkinter import *
import random
import time
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 12, "italic")
FONT_SCORE = ("Arial", 9)
TRUE_BUTTON_FILE = "./images/true.png"
FALSE_BUTTON_FILE = "./images/false.png"


class Ui:
    def __init__(self,quiz:QuizBrain):
        self.ques = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, pady=20, padx=20)
        true_image = PhotoImage(file=TRUE_BUTTON_FILE)
        false_image = PhotoImage(file=FALSE_BUTTON_FILE)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            text="Welcome to Quizzler",
            font=FONT,
            fill=THEME_COLOR,
            width=250
        )
        self.canvas.grid(row=1, column = 0, columnspan= 2,pady=50)
        self.score = Label(text = f"Score: 0", font=FONT_SCORE,bg = THEME_COLOR, fg = "white")
        self.score.grid(row=0,column= 1)

        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0,command = self.true_button_click)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0,command = self.false_button_click)
        self.false_button.grid(column=1, row=2)
        self.get_next_ques()

        self.window.mainloop()
    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.ques.still_has_questions():
            self.score.config(text=f"Score: {self.ques.score}")
            q_text = self.ques.next_question()
            self.canvas.itemconfig(self.question,text = q_text)
        else:
            self.score.config(text=f"Score: {self.ques.score}")
            self.canvas.itemconfig(self.question, text = f"Thank You For Playing the Game.\nYour Total score is {self.ques.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_button_click(self):
        score = self.ques.check_answer("True")
        self.change_background(score)

    def false_button_click(self):
        score = self.ques.check_answer("False")
        self.change_background(score)

    def change_background(self, is_correct):
        score_tracker = 0
        if is_correct:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_ques)

    # def false_button_click(self):
