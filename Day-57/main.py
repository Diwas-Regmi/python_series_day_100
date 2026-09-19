import requests

blog_url = "https://api.npoint.io/fa378257259b7d695a4d"
response = requests.get(blog_url)
all_posts = response.json()
print(all_posts)