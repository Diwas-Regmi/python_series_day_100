import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"
API_KEY  = os.environ["FLIGHT_API_KEY"]
APP_ID = os.environ["FLIGHT_APP_ID"]


class FlightSearch:
    def __init__(self, origin_place_id, arrival_place_id, departure_time, to_time,is_direct):
        self.params = {
            "engine": "google_flights",
            "departure_id": origin_place_id,
            "arrival_id": arrival_place_id,
            "outbound_date": departure_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "stops": "1",
            "api_key": API_KEY,
        }
        self.is_direct = is_direct

    def get_flight_data(self):
        # Only include stops parameter if is_direct is True
        if self.is_direct:
            self.params["stops"] = "1"

        response = requests.get(url=ENDPOINT, params=self.params)
        data = response.json()
        return data

tomorrow         = datetime.now() + timedelta(days=1)
six_month_later  = datetime.now() + timedelta(days=6 * 30)


# Searching For flight available from places and times included
flight_class = FlightSearch("LHR","CDG",tomorrow,six_month_later,True)
print(flight_class.get_flight_data())