from tkinter import *

from pandas.core.computation import common

FONT_NAME = "Times New Roman"
import random
import string
import secrets
from tkinter import messagebox
import pyperclip
import json

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
    new_data = {
        website:{
            "email":username,
            "password": password

    }
    }

    if not password or not website:
        messagebox.showwarning(title="Oops!!", message="Please dont leave any field Empty:)")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)



        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_key():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as file:

            dataa = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")


    else:
        if website_name in dataa:
            messagebox.showinfo(title = website_name, message=f"Email:{dataa[website_name]["email"]}\nPassword:{dataa[website_name]["password"]}")

        else:
            messagebox.showinfo(title="Error", message= f"No Details for {website_name} Exist.")







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=80, padx=80)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(column=1, row= 0, columnspan=2, sticky="w")

#Labels
website_text = Label(text = "Website: ")
email_text = Label(text = "Email/Username: ")
password_text = Label(text = "Password: ")

# Grid
website_text.grid(column = 0 , row=1)
email_text.grid(column= 0, row=2)
password_text.grid(column= 0 , row=3)

#inputs
website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="w")
website_input.focus()

email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0, "diwas@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="w")

search_button = Button(text="Search",width=1, command = search_key)
search_button.grid(column=2, row=1, sticky="ew")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=29, command=add_file)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")




window.mainloop()