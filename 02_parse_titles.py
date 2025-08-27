import requests

from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")


infos = soup.select("h3 a")
print("Book informatiuns: ")

for info in infos:
    print("Titles:-", info.get("title"))
    print("Link:-", info.get("href"))