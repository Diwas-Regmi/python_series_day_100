import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()
# AUTHORIZATION = os.environ["AUTHORIZATION"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
SHEETY_API = os.environ["SHEETY_API"]
SHEETY_ENDPOINT = "https://api.sheety.co"
AUTHORIZATION = HTTPBasicAuth(username=USERNAME, password= PASSWORD)
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_url = f"{SHEETY_ENDPOINT}/{SHEETY_API}/flightDeals/prices"
        # self.headers = {
        #     "Authorization": AUTHORIZATION,
        # }
        self.response = requests.get(url=self.sheety_url, auth=AUTHORIZATION)
        self.response.raise_for_status()
        self.data = self.response.json()

    def flight_price(self):
        return self.data["prices"]

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_ENDPOINT}/{row_id}",
            json=new_data,
            auth=AUTHORIZATION,
        )