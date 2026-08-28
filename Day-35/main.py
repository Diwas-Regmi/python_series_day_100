import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

import requests
api_key = os.getenv("API_KEY")
url_link="https://api.openweathermap.org/data/2.5/forecast"


parameter = {
    "lat":27.687225,
    "lon":83.180471,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url=url_link, params=parameter)

# print(response.status_code)
# print(response.text)
response.raise_for_status()

data = response.json()


will_rain = False
for lists in data["list"]:
    # print(lists)
    id = lists["weather"][0]["id"]
    if int(id)< 700:
        will_rain = True


if will_rain:
    # import twilio_sms
    import whatsapp_sms