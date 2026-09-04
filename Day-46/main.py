import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

# date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
# url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
url = f"https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"
# print(url)
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
song_list = [songs.getText() for songs in soup.find_all("h3")]
print(song_list)


ytmusic = YTMusic("browser.json")
playlists = ytmusic.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

# if the playlist already exist
# playlistId = "PLPd22gTbMXUA" # id taken from my ytmusic playlist which is the id of Project_playlist playlist
# song_list = ["Drop It Like It's Hot", "Stronger", "G.O.M.D","Runaway "]

playlistId = ytmusic.create_playlist("Project_playlist", "Created as part of my backend web development project. A curated collection of tracks generated and managed via the YouTube Music API.")
for songs in song_list:
    search_results = ytmusic.search(songs, filter="songs")

    if search_results:
        video_id = search_results[0]['videoId']
        ytmusic.add_playlist_items(playlistId, [video_id])
        print(f"{songs} added successfully!")
    else:
        print(F"{songs} not Found.")
