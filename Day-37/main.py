import requests
import datetime
import datetime as dt
import os
from dotenv import load_dotenv

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = os.environ["GRAPH_ID"]

#Create pixela username
pixela_endpoint = "https://pixe.la/v1/users"
# today's date in required format
now = datetime.datetime.now()
time_str = str(now.date())
date_today = time_str.split("-")
date_today_str = "".join(date_today)

# today = datetime.datetime(year = 2026, month = 8, day = 27)
# date_today_str = today.strftime("%Y%m%d")

# step 1 creating username inside pixela
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)

2. adding graphs and giving it id name and units
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

# step 3 adding pixel inside the graph to track the activities
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json = graph_config,headers = headers)
# print(response.text)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_today_str}"
pixel_data = {
    # "date": date_today_str,
    "quantity": "10.8",

}
response = requests.put(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
