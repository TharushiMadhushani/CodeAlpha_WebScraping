
import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

START_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"

HEADERS = {
    "User-Agent": "CodeAlpha-WebScraping-Student/1.0"
}

all_books = []
url = START_URL
page_number = 0
max_pages = 3

while url and page_number < max_pages:
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )
        response.raise_for_status()

        soup = BeautifulSoup(
            response.content,
            "html.parser"
        )

        books = soup.select("article.product_pod")

        if not books:
            print("No book records found. Stopping.")
            break

        for book in books:
            title_element = book.select_one("h3 a")
            price_element = book.select_one(".price_color")
            rating_element = book.select_one(".star-rating")
            stock_element = book.select_one(
                ".availability"
            )

            all_books.append({
                "title": (
                    title_element.get("title", "").strip()
                    if title_element else ""
                ),
                "price": (
                    price_element.get_text(strip=True)
                    if price_element else ""
                ),
                "rating": (
                    rating_element.get("class", ["", ""])[1]
                    if rating_element
                    and len(rating_element.get("class", [])) > 1
                    else ""
                ),
                "availability": (
                    " ".join(stock_element.stripped_strings)
                    if stock_element else ""
                ),
                "page": page_number + 1
            })

        page_number += 1
        print(
            f"Page {page_number} completed: "
            f"{len(books)} books found."
        )

        next_link = soup.select_one("li.next a")

        if next_link and page_number < max_pages:
            url = urljoin(url, next_link.get("href", ""))
            time.sleep(1)
        else:
            url = None

    except requests.RequestException as error:
        print(f"Request failed: {error}")
        break

if all_books:
    fieldnames = [
        "title",
        "price",
        "rating",
        "availability",
        "page"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(all_books)

    print(f"\nTotal books collected: {len(all_books)}")
    print(f"Data saved to {OUTPUT_FILE}")
else:
    print("No data collected. Please check the website.")
