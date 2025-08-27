import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.select(".product_pod")

print("List of available nooks with the prices: ")

for b in books:
    title = b.h3.a.get("title")
    price = b.select_one(".price_color").getText()
    print(f"{title}-{price}")


