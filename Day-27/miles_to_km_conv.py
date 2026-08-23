from tkinter import *
my_screen = Tk()
my_screen.minsize(height=150, width=300)
to_km = 0


def value():
    miles = miles_box.get()

    if miles:
        km = int(miles) * 1.6
        text_2["text"] = f"{km}"
    else:
        text_2["text"] = "0"

miles_box = Entry()
miles_box.grid(column=2,row=0)

text = Label(text= "Miles")
text.grid(column=4, row=0)



text_2 = Label(text=f"is equal to")
text_2.grid(column=1, row=2)

text_2 = Label(text=f"{to_km}")
text_2.grid(column=2, row=2)
text_2.config(pady=20,padx=70)

text_3 = Label(text = "km")
text_3.grid(column=3, row=2)


calculate = Button(text="Calculate", command= value)
calculate.grid(column=3, row=3)





my_screen.mainloop()