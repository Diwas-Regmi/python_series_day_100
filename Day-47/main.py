import requests
from bs4 import BeautifulSoup
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()
my_email = os.environ["MY_EMAIL"]
password = os.environ["PASSWORD"]
receiver = os.environ["RECEIVING_EMAIL"]
app_password = os.environ["APP_PASSWORD"]

url = "https://appbrewery.github.io/instant_pot/"

# headers
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)",
}

response = requests.get(url,headers = header)

soup = BeautifulSoup(response.text, "html.parser")
whole = soup.find_all("span", class_ = "a-price-whole")
fraction = soup.find_all("span", class_ = "a-price-fraction")
price = float((whole[0].getText()) + (fraction[0].getText()))
title = soup.find_all("span", id = "productTitle", class_="a-size-large product-title-word-break")
title_list = title[0].string.split()
title_ricecooker = "".join(title_list)
print(title_ricecooker)
print(price)

message = EmailMessage()
message["Subject"] = "AMAZON PRICE ALERT!!!!!"
message["From"] = my_email
message["To"] = receiver

# 2. Set message body (UTF-8 encoding is handled automatically)
message.set_content(f"{title_ricecooker} is now ${price}")


#
# smtp
with smtplib.SMTP('smtp.gmail.com',587) as smtp_server:
    smtp_server.starttls()
    smtp_server.login(my_email,app_password)
    if price < 100:
        smtp_server.send_message(msg = message)
