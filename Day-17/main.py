# class User:
#     pass
# user_1 = User()
# user_1.id = 2003
# user_1.name = "Diwas_2003"
# print(user_1.name)
#
# user_2 = User()
# user_2.id = "990"
# user_2.name = "sawid"
# print(user_2.id)
# print(user_2.name)
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        self.following += 1
        user.followers +=1

user_1 = User("999", "Lilly")
print(user_1.id)
print(user_1.username)
user_2 = User("111", "Diwas")
print(f"Welcome {user_2.username}. You have logged in as username {user_2.id}")
user_2.follow(user_1)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)