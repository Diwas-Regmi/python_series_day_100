from tkinter import *

from main import button

window = Tk()
window.minsize(width=500, height=300)
window.title("Working mechanism of place, pack and grid")
window.config(padx=20,pady=20)


text = Label(text="Label Example", font = ("Arial", 24, "bold"))
text.grid(column = 0, row=0)

button_1 = Button(text="button_1")
button_1.grid(column=1, row=1)

button_2 = Button(text="button_2")
button_2.grid(column=2, row=0)

input = Entry(text = "enter something")
input.grid(column = 3, row=2)

window.mainloop()