import smtplib
import time
my_email = "diwas.regmi1110@gmail.com"
password="ifkj ajnf rcas ####"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user = my_email,password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="sawid.imger2019@gmail.com",
#     msg = "Subject:Hello This message is Sent using SMTP (A Simple Module Using Python)\n\n\n"
#           "So i am at my day-32 of 100 Days Python Challenge. Everything's going on perfect till now"
#           "i am gonna be the best")
# connection.close()

# # You can also use with with this one
# with smtplib.SMTP("smtp.gmail.com") as connection:
#
#     connection.starttls()
#     connection.login(user = my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#         to_addrs="kriti.regmi218@gmail.com ",
#                         msg="""Subject: Important: Please Review and Confirm
#
#         Dear Sister,
#
#         I hope this email finds you well.
#
#         This message is being sent regarding an important matter that requires a small amount of your attention and cooperation.
#
#         Please take a moment to carefully read the following information before responding.
#
#         There is currently a requirement to verify whether the recipient of this email is able to identify certain details contained within the message.
#
#         For confirmation, please carefully consider the following questions:
#
#         1. Did this email arrive successfully in your inbox?
#
#         2. Did you read the complete message?
#
#         3. Did you notice anything unusual about the wording of this email?
#
#         4. Were you expecting to receive an email like this?
#
#         5. How much time did you spend reading this?
#
#         6. Did you consider replying before reaching this section?
#
#         If the answer to the above questions is yes, congratulations. The communication test has been completed successfully.
#
#         There is, however, one final and extremely important piece of information.
#
#         This entire email was created and sent as part of a Python project using the smtplib module. The purpose was to practice sending emails programmatically through an SMTP server.
#
#         So basically...
#
#         You have officially participated in my Python experiment.
#
#         Thank you for your valuable time and cooperation.
#
#         Best regards,
#         Your extremely serious and definitely professional brother
#
#         P.S. Yes, you really did read the whole thing.
#         """)
# Doing the same with yahoo on myself
# my_email_2 = "sawid.imger2019@gmail.com"
# password_2="###########"
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls() # to make secure
#     connection.sendmail(from_addr=my_email_2, to_addrs="diwas.regmi1110@gmail.com", msg="Subject: Sending from Yahoo Just to know it works from Both sides\n\n\n"
#                                                    "Really Feeling like i am learning something practical. I am very happy:)")

import datetime as dt
# while True:

now = dt.datetime.now()
time_full = now.time()
year = now.year
time_min = now.time().replace(microsecond=0)
# c_time = now.ctime().replace(month = None)
# print(c_time)
print(f"Year: {year}, Time = {time_min}")
dob = dt.datetime(year = 2003, day=22, month=2)
print(now.weekday())
print(dob)
time.sleep(1)
