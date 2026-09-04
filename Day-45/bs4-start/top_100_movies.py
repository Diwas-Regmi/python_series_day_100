import requests
from bs4 import BeautifulSoup

# loading the url's html code with requests
url = "https://www.cinemarealm.com/best-of-cinema/empires-500-greatest-movies-of-all-time/"
response = requests.get(url)
movie_page = response.text


# loading the html into beautifulsoup
soup = BeautifulSoup(movie_page, "html.parser")
movies_div = soup.find_all("strong")
top_100_movies = movies_div[1:101]
# print(len(top_100_movies))

# saving top 100 movies inside movielist
movie_list = [top_100_movies[i].getText() for i in range(len(top_100_movies))]


# length_movie_list = len(movie_list)
# print(movie_list[length_movie_list-1])
# reversed_movie_list = movie_list[::-1]
# print(reversed_movie_list)
# for i in range(99,-1,-1):
#     print(f"{i+1} - {movie_list[i]}")

# saving the list in top_100_movies.txt
with open("top_100_movies.txt", "w") as file:
    file.write("Top 100 Greatest Movies of all time. \n\n")
    for i in range(99,-1,-1):
        file.write(f"{i+1} - {movie_list[i]}\n")



