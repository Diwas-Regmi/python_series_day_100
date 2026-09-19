import requests

class Post:
    def __init__(self):
        url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(url = url)
        self.all_posts = self.response.json()

    def get_data(self):
        return self.all_posts

# post = Post()
# all_posts = post.get_data()
# print(all_posts)