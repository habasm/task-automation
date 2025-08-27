import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
all_books = []

for page in range(1, 4):  # First 3 pages
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(".product_pod")
    for b in books:
        title = b.h3.a.get("title")
        price = b.select_one(".price_color").get_text()
        all_books.append([title, price])

# Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    writer.writerows(all_books)

print("✅ Saved data to books.csv")
