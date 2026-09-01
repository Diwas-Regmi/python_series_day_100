from wsgiref import headers

import requests
import os
from dotenv import load_dotenv
from urllib3.util import url

load_dotenv()
TOKEN = os.environ["SHEETY_TOKEN"]
AUTHORIZATION_KEY= os.environ["SHEETY_AUTHORIZATION"]
USERNAME = os.environ["SHEETY_USERNAME"]
PASSWORD = os.environ["SHEETY_PASSWORD"]
AUTHORIZATION = (USERNAME,PASSWORD)
HEADERS = {
    "Authorization": AUTHORIZATION_KEY
}
class DataManager:
    def __init__(self):
        self.url = f"https://api.sheety.co/{TOKEN}/flightDeals/prices"


    def get_data(self):
        # response = requests.get(url=self.url, auth=AUTHORIZATION)
        response = requests.get(url=self.url, headers=HEADERS)
        data = response.json()
        return data

    def update_lowest_price(self,id, price):
        new_data = {
            "price":{

            # "id": id,
            "lowestPrice": price,}
        }
        response = requests.put(url= f"{self.url}/{id}", auth = AUTHORIZATION,json=new_data)
        pass
# data = DataManager()
# dataa = data.get_data()
# print(dataa)
# # print(dataa[0]["city"])

