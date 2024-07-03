import requests
from bs4 import BeautifulSoup
import os
import hashlib  # for generating unique identifiers
import datetime  # for generating timestamps

# Function to scrape and save articles locally
def scrape_and_save(url, save_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('h2', class_='newsHdng')
            for article in articles:
                title = article.text.strip()
                link = article.find('a')['href']
                category = "General"  # Replace with actual category extraction logic
                article_id = hashlib.md5(link.encode()).hexdigest()
                
                # Fetch article content
                article_response = requests.get(link)
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')
                    # Example: extracting article text
                    article_text = article_soup.find('div', class_='content').text.strip()  # Replace with actual content extraction
                    
                    # Example: generating timestamp for filename
                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    
                    # Create directory if it doesn't exist
                    os.makedirs(save_directory, exist_ok=True)
                    
                    # Save article as text file
                    filename = os.path.join(save_directory, f"{timestamp}_{article_id}.txt")
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f"Title: {title}\n\n")
                        file.write(f"Category: {category}\n\n")
                        file.write(f"URL: {link}\n\n")
                        file.write(f"Content:\n\n{article_text}")
                    
                    print(f"Saved: {title}")
                else:
                    print(f"Failed to retrieve article content from {link}. Status code: {article_response.status_code}")
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

if __name__ == '__main__':
    # Example usage
    url = 'https://www.ndtv.com/'
    save_directory = './saved_articles'
    
    scrape_and_save(url, save_directory)
