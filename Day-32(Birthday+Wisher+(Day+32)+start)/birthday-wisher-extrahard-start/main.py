import pandas as pd
import random
import smtplib
import datetime as dt

email_id = "diwas.regmi1110@gmail.com"
password = "uyql mdsr ###z vjml"

##################### Extra Hard Starting Project ######################
with open("./letter_templates/letter_1.txt","r") as file:
    letter_1 = file.read()
with open("./letter_templates/letter_2.txt","r") as file:
    letter_2 = file.read()
with open("./letter_templates/letter_3.txt","r") as file:
    letter_3 = file.read()

# letter_list = [letter_3,letter_2,letter_1]
rand_lett = random.choice((letter_1,letter_2,letter_3))




# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birthday_month = int(now.strftime("%m"))
birthday_day = int(now.strftime("%d"))


for i in range(len(df)):
    if (df["month"][i] == birthday_month) and (df["day"][i] == birthday_day):
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email_id, password=password)
            connection.sendmail(from_addr=email_id,
                                to_addrs="sawid.imger2019@gmail.com",
                                msg=f"Subject: Happy BirthDay To You:))))\n\n"
                                    f"{rand_lett.replace("[NAME]", df["name"][i])}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#




