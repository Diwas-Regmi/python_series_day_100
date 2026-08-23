from tkinter import *
FONT_NAME = "Times New Roman"
import random
import string
import secrets
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    length = random.randint(12,20)
    letters = string.ascii_letters
    numbers = string.digits
    symbols =  "!@#$%^&*()-_=+"
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )
    password_input.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_file():

    website = website_input.get()
    username = email_input.get()
    password = password_input.get()
    if not password or not website:
        messagebox.showwarning(title="Oops!!", message="Please dont leave any field Empty:)")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:  \nEmail: {username}\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(column=1, row= 0)

#Labels
website_text = Label(text = "Website: ")
email_text = Label(text = "Email/Username: ")
password_text = Label(text = "Password: ")

# Grid
website_text.grid(column = 0 , row=1)
email_text.grid(column= 0, row=2)
password_text.grid(column= 0 , row=3)

#inputs
website_input = Entry(width = 35)
email_input = Entry(width = 35)
password_input = Entry(width = 21)




# input grids
website_input.grid(column= 1, row=1,columnspan=2)
website_input.focus()
email_input.grid(column= 1 , row=2,columnspan=2)
email_input.insert(0, "diwas@gmail.com")
password_input.grid(column= 1, row=3)

#Buttons
generate_password_button = Button(text = "Generate Password", command=generate_password)
add_button = Button(text= "Add", width=29, command=add_file)

# Buttons Grids
generate_password_button.grid(column=2, row=3)
add_button.grid(column = 1, row=4,columnspan=2)

print(website_input.get())


window.mainloop()