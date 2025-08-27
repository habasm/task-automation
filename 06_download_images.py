import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
site_root = "https://books.toscrape.com/"

# Create folder for images
os.makedirs("book_images", exist_ok=True)

for page in range(1, 3):  # First 2 pages for demo
    print(f"\n--- Downloading Page {page} ---")
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(".product_pod")
    for b in books:
        title = b.h3.a.get("title")
        img_tag = b.select_one("img")

        if img_tag:
            img_url = urljoin(site_root, img_tag["src"])  # ✅ Properly join URL
            # Clean filename (remove slashes/illegal chars)
            safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "_", "-")).rstrip()
            filename = f"book_images/{safe_title}.jpg"

            # Download image
            img_data = requests.get(img_url).content
            with open(filename, "wb") as f:
                f.write(img_data)

            print(f"✅ Saved {filename}")
