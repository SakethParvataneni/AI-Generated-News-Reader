import requests
from bs4 import BeautifulSoup
import sqlite3
import pika

def create_db():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (url TEXT PRIMARY KEY, title TEXT, content TEXT, metadata TEXT)''')
    conn.commit()
    conn.close()

def save_article(url, title, content, metadata):
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO articles (url, title, content, metadata) VALUES (?, ?, ?, ?)",
              (url, title, content, metadata))
    conn.commit()
    conn.close()

def scrape_detail_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No Title'
    content = ' '.join(p.get_text() for p in soup.find_all('p'))
    metadata = ''  # Add code to extract metadata if needed

    save_article(url, title, content, metadata)
    print(f'Scraped and saved article: {url}')

def callback(ch, method, properties, body):
    url = body.decode()
    scrape_detail_page(url)

def consume_detail_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detail_urls')

    channel.basic_consume(queue='detail_urls', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages...')
    channel.start_consuming()

if __name__ == '__main__':
    create_db()
    consume_detail_queue()
