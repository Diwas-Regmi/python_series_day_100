from pydoc import text
from tkinter import Tk, Label,Button, Entry,Spinbox,Checkbutton,Radiobutton,Scale,Listbox,END
window = Tk()
window.minsize(height=300, width=500)
window.title("My First GUI Program")


# Label
my_label = Label(text = "I am groot", font = ("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    new_input = input.get()
    my_label.config(text=f"I am {new_input}")


#Button
button =  Button(
                text="Click Me",
                command=button_clicked)
button.pack()

#Entry
input = Entry(width=54)
input.pack()
input.insert(END, "Enter the text to replace the entered string in place of GROOT")


#spinbox
spin_num = Spinbox(from_=0, to=10, increment=1)
spin_num.pack(pady=20)

check_box = Checkbutton(text="Is on?")
check_box.pack()

rb1 = Radiobutton(text="Option A", value=1)
rb2 = Radiobutton(text="Option B", value=2)

# rb1.pack(anchor="w", padx=20, pady=5)
rb1.pack()
rb2.pack()

#Scale
slider = Scale(from_=0, to=10, orient="vertical")
slider.pack()
# slider.pack(pady=40, fill="x", padx=20)



#Listbox
listbox = Listbox()
listbox.pack(pady=20, padx=20, fill="both", expand=True)

listbox.insert(END, "Python")
listbox.insert(END,"JavaScript")
listbox.insert(END, "C++")
listbox.insert(1, "GAY")



my_label.mainloop()


