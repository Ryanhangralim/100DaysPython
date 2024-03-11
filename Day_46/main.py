import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

with open("secret.txt", "r") as file:
    data = file.readlines()

CLIENT_ID = data[0].strip()
CLIENT_SECRET = data[1].strip()

user_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{user_year}"

response = requests.get(billboard_endpoint).text

soup = BeautifulSoup(response, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.text.strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager= SpotifyOAuth(
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        redirect_uri= "https://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
spotify_userid = sp.current_user()["id"]

# result = sp.search(q="Life will Change", type="track", limit=1)
# print(result["tracks"]["items"][0]["external_urls"]["spotify"])
song_links = [sp.search(q=song, type="track", limit=1)["tracks"]["items"][0]["external_urls"]["spotify"] for song in song_list]

playlist_id = sp.user_playlist_create(user=spotify_userid, name=f"{user_year} Billboard 100", public=False, collaborative=False, description=f"Top songs from {user_year}")
sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_links)