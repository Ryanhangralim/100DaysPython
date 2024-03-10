import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []
article_votes = []

titles = soup.find_all(name="span", class_="titleline")

for title in titles:
    tag = title.a.text
    link = title.a.get("href")
    article_texts.append(tag)
    article_links.append(link)

subclass = soup.find_all(name="span", class_="score")
for article in subclass:
    upvotes = article.text.replace(" points", "")
    article_votes.append(int(upvotes))

print(article_texts)
print(article_links)
print(article_votes)
max_index = article_votes.index(max(article_votes))
print(f"Title = {article_texts[max_index]}\nLink = {article_links[max_index]}\nVotes = {article_votes[max_index]}")


# titles = soup.select(selector="td .title")
# print(titles)
# for title in titles:
#     print(title.text)