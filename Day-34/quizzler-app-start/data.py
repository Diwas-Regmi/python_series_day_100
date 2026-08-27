import requests
URL = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
response = requests.get(url = URL)
response.raise_for_status()
data =response.json()
question_data = data["results"]
