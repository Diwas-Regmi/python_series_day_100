from bs4 import BeautifulSoup
with open("website.html") as file:
    content = file.read()

# print(content)
soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.find(id="name"))
# print(soup.a)
# print(soup.li)
# anchor_tag = soup.find_all(name = "h1")
# for tags in anchor_tag:
#     # print(tags.getText())
#     print(tags.get("id"))
heading = soup.find(name = "h1", id = "name")
print(heading.getText())
head_3 = soup.find(name = "h3", class_ = "heading")
print(head_3.getText())

# you can also use soup in css style
unordered_list = soup.select_one("ul")
print(unordered_list.getText())

a_tag = soup.select_one("p a")
print(a_tag)
print(a_tag.getText())

id_name = soup.select_one("#name")
print(id_name)
print(id_name.getText())
