import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
article_texts = []
article_links = []
soup = BeautifulSoup(yc_web_page, "html.parser")
web_links = soup.find_all("span", class_= "titleline")
for web in web_links:
    parent = web.parent
    text = parent.find("a").string
    link = parent.find("a").get("href")
    article_links.append(link)
    article_texts.append(text)

# print(article_links)
# print(web_links)
upvotes = soup.find_all("span", class_ = "score")
# print(upvotes.getText())
upvotes_numbers = [upvote.getText() for upvote in upvotes]
print(len(upvotes_numbers))
print(upvotes_numbers)
print(len(article_texts))
print(article_texts)


for i in range(len(article_links)-1):
    print(f"article {i+1} - {article_texts[i]}. link - {article_links[i]} with an upvotes {upvotes_numbers[i].split(" ")[0]}")

# # print(first_web[0].get("class"))
# print(first_web)
# parent = first_web[0].parent
# find_a = parent.find("a")
# print(find_a)
# text_find_a = find_a.getText()
# print(find_a.get("href"))
# # print(parent.find(href))
# upvote = soup.find_all("span", class_ = "score", id = "score_49554643")
# print(upvote[0].string)
# # print(upvote.parent)
# print(text_find_a)
