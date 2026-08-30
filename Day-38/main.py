import requests
import os
from dotenv import load_dotenv
import datetime as dt


now = dt.datetime.now()

load_dotenv()
authorization = os.environ["AUTHORIZATION"]
YOUR_APP_ID = os.environ["APP_ID"]
YOUR_NUTRITION_API_KEY = os.environ["api_key"]
PROJECT_ID = os.environ["PROJECT_ID"]
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise = input("So tell me which exercise you did today? : ")
headers = {
    "Content-Type": "application/json",
    "x-app-id": YOUR_APP_ID,
    "x-app-key": YOUR_NUTRITION_API_KEY,
}

data = {
    "query": exercise,
    # "weight_kg": 70,
    # "height_cm": 175,
    #  "age": 30,
    # "gender": "male",
}

response = requests.post(url, headers=headers, json=data)
response.raise_for_status()
result = response.json()
# print(response.text)
exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
today_formatted_date = now.strftime(f"%d/%m/%Y")
current_time = str(now.time().replace(microsecond=0))

# {'tag_id': 63, 'user_input': 'swam for 1 hour', 'nf_calories': 420, ...}
sheety_url = f"https://api.sheety.co/{PROJECT_ID}/myWorkouts/workouts"
body = {
    "workout": {
        "date": today_formatted_date,
        "time": current_time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}
headers = {
    "Authorization": authorization,
}
response = requests.post(url = sheety_url,
                         json=body,
                         headers = headers)
print(response.text)

