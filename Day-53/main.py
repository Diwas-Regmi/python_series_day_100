import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from fill_forms import FillForm

load_dotenv()
ZILLOW_URL = os.environ['ZILLOW_URL']
GOOGLE_FORM = os.environ['GOOGLE_FORM']

# Scrap from Zillow Url
responses =  requests.get(ZILLOW_URL)

doc = BeautifulSoup(responses.text, "html.parser")

lists_of_rentals = doc.find_all(class_ = "ListItem-c11n-8-84-3-StyledListCardWrapper")
price_list = []
links_to_appartment = []
address_lists = []
for items in lists_of_rentals:
    price = items.find(class_ = "PropertyCardWrapper__StyledPriceLine")
    links = items.find(class_ = "property-card-link")
    address = items.find("address")

    price_list.append(price.text)
    links_to_appartment.append(links.get("href"))
    address_lists.append(address.text.strip())

#
# print(price_list)
# print(address_lists)
# print(links_to_appartment)

fill_form = FillForm(GOOGLE_FORM, price_list,address_lists,links_to_appartment)
print("started Filling up forms")
fill_form.form_fill_up()
print(f"Finished filling up a total of : {len(price_list)} forms.")
