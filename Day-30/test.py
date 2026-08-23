facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    try:
        total_likes = 0
        for post in posts:
            print(post)
            total_likes = total_likes + post['Likes']

    except KeyError as error:
        print(f"The {error} doesnot exist")

    return total_likes


count_likes(facebook_posts)

