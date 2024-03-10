from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200523081845/https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

title_list = []
titles = soup.find_all(name="div", class_="article-title-description__text")

with open("movies.txt", "a", encoding="utf-8") as file:
    for title in reversed(titles):
        file.write(f"{title.h3.get_text()}\n")