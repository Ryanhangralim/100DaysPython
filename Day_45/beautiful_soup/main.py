from bs4 import BeautifulSoup
import lxml

with open("index.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
print(soup.find_all(name="p"))

print(soup.find(name="h1", id="name").string)

company_url = soup.select_one(selector="p a")
print(company_url)
print(soup.a)