from bs4 import BeautifulSoup
import requests
url = "https://www.newegg.com/gigabyte-gv-n507tgaming-oc-16gd-geforce-rtx-5070-ti-16gb-graphics-card-triple-fans/p/N82E16814932768"

response = requests.get(url)
# print(response.text)
doc = BeautifulSoup(response.text, "html.parser")
# print(doc.prettify())
price = doc.find_all(text = "$")
parent = price[0].parent
parent_2 = price[1].parent
parent_3 = price[2].parent
parent_4 = price[3].parent
strong = parent.find("strong")
print(strong.string)
print(strong)
print(price)
print(parent)
print(parent_2)
print(parent_3)
print(parent_4)

# with open("website.html") as file:
#     doc = BeautifulSoup(file,"html.parser")
#
# tag = doc.title
# tag.string = "changing the title with tag.string"
# para_1 = doc.find_all("li")
