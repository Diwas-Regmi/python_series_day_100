import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.environ["FLIGHT_API"]

    def check_flight(self, original_city_code, destination_city_code,from_time,to_time):
        params = {
            "engine": "google_flights",
            "departure_id": original_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "api_key": self.api_key,
            # "currency": "GBP",
            # "stops": "1",
        }
        response = requests.get(ENDPOINT, params=params)
        data = response.json()

        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data

tomorrow = datetime.now() + timedelta(days=1)
six_month_later = datetime.now() + timedelta(days=6 * 30)
flight = FlightSearch()

print(flight.check_flight("LHR","CDG",tomorrow,six_month_later))
