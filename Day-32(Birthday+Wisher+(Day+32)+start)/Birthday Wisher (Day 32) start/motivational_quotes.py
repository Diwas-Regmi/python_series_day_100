import time
import datetime as dt
import smtplib
import random


my_email = "diwas.regmi1110@gmail.com"
password = "uyql mdsr pgwz vjml"

now = dt.datetime.now()
# OPEN THE QUOTES AND SAVE IT INTO A VARIABLE
with open("quotes.txt", "r") as file:
    quotes = file.read()

# convert SAVED VARIABLE into list
listed_quote = list(quotes.split("\n"))

# Generate a Random Quote
random_quotes = random.choice(listed_quote)

with open("already_sent_quote_list.txt", "r") as file:
    already_sent_content = list(file.read().split("\n"))

email_sent = False
while not email_sent:
    if random_quotes in already_sent_content:
        print(random_quotes)
        print("You cannot send this mail")
    else:
        email_sent = True
        with open("already_sent_quote_list.txt", "a") as file:
            file.write(random_quotes + "\n")

        # Checking whether the RANDOM Quote has been sent already or not?
        with smtplib.SMTP('smtp.gmail.com') as connection:
            if now.weekday() == 1:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs="sawid.imger2019@gmail.com",
                                    msg=f"Subject:Quote for Tuesday\n\n\n\n{random_quotes}")
            else:
                print("The Program was only meant to be sent on Tuesday only.")




