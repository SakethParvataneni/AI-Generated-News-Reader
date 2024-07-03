# rss_scraper.py

import requests
from bs4 import BeautifulSoup

# Example function for sitemap/RSS feed scraper
def scrape_sitemap_rss(url):
    # Logic to scrape sitemap or RSS feed
    response = requests.get(url)
    # Parse the response with BeautifulSoup using 'lxml' parser
    soup = BeautifulSoup(response.content, 'lxml')
    links = soup.find_all('link')
    for link in links:
        detail_url = link.get('href')
        if detail_url:
            # Enqueue detail_url for detail page scraping
            scrape_detail_page(detail_url)

def scrape_detail_page(url):
    # Logic to scrape detail page and extract content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')  # Using 'lxml' parser here as well
    # Extract content, metadata, etc.
    title = soup.find('title').get_text()
    content = soup.find('div', class_='content').get_text()
    # Store or process the extracted data as needed

if __name__ == "__main__":
    scrape_sitemap_rss("https://feeds.feedburner.com/ndtvmovies-latest")
