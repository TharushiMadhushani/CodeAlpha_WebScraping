# CodeAlpha Web Scraping Project

## Project Overview
This project was completed as part of the CodeAlpha Data Analytics Internship. It uses Python web scraping techniques to collect book information from the practice website [Books to Scrape](https://books.toscrape.com/).

## Objectives
- Extract book information from web pages.
- Understand HTML parsing using BeautifulSoup.
- Collect and organize data into a structured CSV file.
- Practice handling multiple pages of website data.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- CSV

## Data Collected
The scraper collects the following fields:
- Book title
- Price
- Star rating
- Availability
- Page number

## Project Files
- `scraper.py` — Python web scraping script.
- `books.csv` — Collected book dataset.
- `requirements.txt` — Required Python libraries.

## How to Run
Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the scraper:

```bash
python scraper.py
```

The collected data will be saved to `books.csv`.

## Results
The scraper successfully collected 60 book records from three catalogue pages during the test run.

## Learning Outcomes
This project provided practical experience in retrieving web pages, parsing HTML, extracting structured information, and exporting data to CSV.

## Author
CodeAlpha Data Analytics Intern
