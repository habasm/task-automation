import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 4):  # First 3 pages
    print(f"\n--- Page {page} ---")
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(".product_pod")
    for b in books:
        title = b.h3.a.get("title")
        price = b.select_one(".price_color").get_text()
        print(f"{title} — {price}")
