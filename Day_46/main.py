import requests
from bs4 import BeautifulSoup

# user_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
user_year = "2018-02-04"
billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{user_year}"

response = requests.get(billboard_endpoint).text

soup = BeautifulSoup(response, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.text.strip() for song in songs]
print(song_list)
