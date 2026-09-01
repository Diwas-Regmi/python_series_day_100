#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from dotenv import load_dotenv
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import FlightData
from flight_data import search_cheapest_flight
from notification_manager import NotificationManager
import os

from retry import data_manager

# time
tomorrow         = datetime.now() + timedelta(days=1)
six_month_later  = datetime.now() + timedelta(days=6 * 30)

#Loading Sheets Data
data_class = DataManager()
data = data_class.get_data()

# Searching For flight available from places and times included
flight_Class = FlightSearch("LHR","CDG",tomorrow,six_month_later)
flight_class_data = flight_Class.get_flight_data()

#Flight Data
# data_flight_data = FlightData(flight_class_data)
cheapest_flight = search_cheapest_flight(flight_class_data, six_month_later.strftime("%Y-%m-%d"))
print(f"{data["prices"][0]['city']}: GBP {cheapest_flight.price}")
if cheapest_flight.price != "N/A" and cheapest_flight.price < data["prices"][0]["lowestPrice"]:
    print(f"Lower price found to {data["prices"][0]["city"]}")
    data_class.update_lowest_price(data["prices"][0]["id"], cheapest_flight.price)
notification = NotificationManager()
sms = f"The lowest price for place {data["prices"][0]['city']} from date {tomorrow.strftime("%Y-%m-%d")}{six_month_later.strftime("%Y-%m-%d")} is {cheapest_flight.price}. Contact us to confirm now"
notification.send_message(sms)
