import datetime as dt
import requests
import smtplib
import time
import os

my_email = os.getenv(my_email)
password = os.getenv(password)

MY_LAT = 27.687228
MY_LONG = 83.180471
def is_overhead():

    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # check your position is within +5 or -5 of the degree of the iss position
    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5<= iss_longitude<= MY_LONG+5):
        return True
    else:
        return False


def is_night_time():
    parameter = {"lat":MY_LAT,
                 "lng": MY_LONG,
                 "formatted": 0,
                 }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now()
    hour_now = int(time_now.strftime("%H"))
    if hour_now >= sunset or hour_now<= sunrise:
        return True
    else:
        return False


is_email_sent = False
while not is_email_sent:


    if is_overhead() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg = "Subject : Look at the start Look how they shine for you.\n\n\n"
                                      "The satellite is over your head check it out")
            is_email_sent = True
    time.sleep(60)
time_now = dt.datetime.now()