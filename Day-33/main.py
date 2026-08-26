import requests
import datetime as dt
import time
# import pandas
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# print(response.status_code)
# df = response.json()
#
# # print(df)
# print(df["iss_position"]["latitude"],"\t", df["iss_position"]["longitude"])
MY_LAT =27.687250
MY_LONG = 83.180598
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json",params= parameters)
response.raise_for_status()

df = response.json()
# print(df)
sunrise = df["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = df["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
now = dt.datetime.now()
time_now = now.strftime("%H:%M:%S %p")
print(df)
print(type(time_now))