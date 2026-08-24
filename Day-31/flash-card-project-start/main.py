# import pandas as pd
# from tkinter import *
# import random
#
# BACKGROUND_COLOR = "#B1DDC6"
# TITLE_FONT = ("Ariel", 40, "italic")
# WORD_FONT = ("Ariel", 60, "bold")
#
# directory = "./data/french_words.csv"
# df = pd.read_csv(directory)
# index_rand = 0
#
#
# def unknown_next_card():
#     global index_rand
#
#     index_rand = random.choice(range(len(df)))
#     canvas.itemconfig(flipper,  image = card_front)
#     canvas.itemconfig(title_text, text = df.columns[0])
#     canvas.itemconfig(word_text, text = df["French"][index_rand])
#     window.after(3000, flip_card)
#
#
# def known_next_card():
#     global index_rand
#     global df
#     df = df.drop(index_rand)
#     df.to_csv("words_to_learn.csv", index = False)
#
#     index_rand = random.choice(range(len(df)))
#     canvas.itemconfig(flipper,  image = card_front)
#     canvas.itemconfig(title_text, text = df.columns[0])
#     canvas.itemconfig(word_text, text = df["French"][index_rand])
#     window.after(3000, flip_card)
#
#
# def flip_card():
#     global index_rand
#     canvas.itemconfig(title_text, text = df.columns[1])
#     canvas.itemconfig(word_text, text = df["English"][index_rand])
#     canvas.itemconfig(flipper, image = card_back)
#
#
#
# #Setting up the screen
# window = Tk()
# window.title("Flashy")
# window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)
#
# # images and logos
# card_front = PhotoImage(file="./images/card_front.png")
# card_back = PhotoImage(file="./images/card_back.png")
# right = PhotoImage(file="./images/right.png")
# wrong = PhotoImage(file="./images/wrong.png")
#
# #Setting our Canvas
# canvas = Canvas(width=800, height=526, highlightthickness=0, bg = BACKGROUND_COLOR)
# # canvas.create_image(400,270, image = card_back)
# flipper = canvas.create_image(400,263, image = card_front)
# title_text = canvas.create_text(400,150, text="", font=TITLE_FONT)
# word_text = canvas.create_text(400,263, text="", font=WORD_FONT)
# canvas.grid(column = 0, row = 0, columnspan=2)
#
# #Making Right or Wrong Buttons
# unknown_button = Button(image= wrong, highlightthickness=0, command=unknown_next_card)
# unknown_button.grid(column=0, row=1)
# known_button = Button(image= right, highlightthickness=0, command=known_next_card)
# known_button.grid(column=1, row=1)
# unknown_next_card()
# window.mainloop()

import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# ---------------------------- DATA ------------------------------- #

try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")

index_rand = 0


# ---------------------------- FLASHCARDS ------------------------------- #

def unknown_next_card():
    global index_rand

    index_rand = random.choice(range(len(df)))

    canvas.itemconfig(flipper, image=card_front)
    canvas.itemconfig(title_text, text=df.columns[0])
    canvas.itemconfig(word_text, text=df.iloc[index_rand]["French"])

    window.after(3000, flip_card)


def known_next_card():
    global index_rand
    global df

    # Remove the current word
    df = df.drop(df.index[index_rand])

    # Save remaining words
    df.to_csv("words_to_learn.csv", index=False)

    # Check if there are no words left
    if len(df) == 0:
        canvas.itemconfig(title_text, text="Finished!")
        canvas.itemconfig(word_text, text="No more words!")
        return

    # Show next card
    index_rand = random.choice(range(len(df)))

    canvas.itemconfig(flipper, image=card_front)
    canvas.itemconfig(title_text, text=df.columns[0])
    canvas.itemconfig(word_text, text=df.iloc[index_rand]["French"])

    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text=df.columns[1])
    canvas.itemconfig(word_text, text=df.iloc[index_rand]["English"])
    canvas.itemconfig(flipper, image=card_back)


# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

canvas = Canvas(
    width=800,
    height=526,
    highlightthickness=0,
    bg=BACKGROUND_COLOR
)

flipper = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

canvas.grid(column=0, row=0, columnspan=2)

unknown_button = Button(
    image=wrong,
    highlightthickness=0,
    command=unknown_next_card
)
unknown_button.grid(column=0, row=1)

known_button = Button(
    image=right,
    highlightthickness=0,
    command=known_next_card
)
known_button.grid(column=1, row=1)

unknown_next_card()

window.mainloop()