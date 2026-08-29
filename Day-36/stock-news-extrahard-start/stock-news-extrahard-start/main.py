import os
import requests
import random
from dotenv import load_dotenv
import datetime as dt
import os
from twilio.rest import Client
from dotenv import load_dotenv
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv()
now = dt.datetime.now()
today_date = str(now.date())

# print(today_date)
load_dotenv()

#Api key
news_api = os.environ["NEWS_API"]
stock_api = os.environ["STOCK_API"]

#
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_url = 'https://www.alphavantage.co/query'
# https://www.alphavantage.co/query?function=&symbol=IBM&apikey=demo
parameter_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    # "interval":"5min",
    "apikey":stock_api,


}
response = requests.get(url= stock_url, params = parameter_stock)
response.raise_for_status()
data = response.json()
yesterday_stock = data["Time Series (Daily)"]["2026-08-28"]
yesterday_opening_stock = float(yesterday_stock["1. open"])
yesterday_closing_stock = float(yesterday_stock["4. close"])
day_before_yesterday_closing_stock = data["Time Series (Daily)"]["2026-08-27"]["4. close"]
difference =float(yesterday_closing_stock)- float(day_before_yesterday_closing_stock)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_per = round((difference/float(yesterday_closing_stock))*100)
if abs(diff_per)>5:
    print("get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = "https://newsapi.org/v2/everything"
parameter_news = {
    "q": "Tesla Inc",
    "from": f"{now.date()}&",
    # "sortBy":"popularity",
    "apiKey":news_api,
    "language":"en",
    # "sources":10,
    # "totalResults":2,
    # "pageSize":6,
    # "page":1,
}

response = requests.get(url = news_url, params=parameter_news)
response.raise_for_status()
# print(response.json())
data = response.json()
# print(data)
print(data["articles"])
articles = data["articles"][0:3]
random_article = random.choice(articles)
sms = f"TSLA:{up_down}{diff_per}\nHeadline: {random_article["title"]}\nBrief: {random_article["description"]}"


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# Download the helper library from https://www.twilio.com/docs/python/install
# loading data from environment
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
my_number = os.environ["MY_WHATSAPP"]
sender_number = os.environ["sender_whatsapp"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=my_number,
    from_=sender_number,
    body = sms,
    content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
)

print(message.status)















#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

