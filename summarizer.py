import schedule
import time
import pika

def enqueue_ndtv_urls():
    # Replace with logic to enqueue NDTV URLs for scraping
    urls_to_scrape = [
        "https://www.ndtv.com/rss/news",
        "https://www.ndtv.com/rss/movies",
        # Add more URLs for different categories as needed
    ]

    # Connect to RabbitMQ and enqueue URLs
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detail_urls')

    for url in urls_to_scrape:
        channel.basic_publish(exchange='', routing_key='detail_urls', body=url)
        print(f"Enqueued {url} for scraping...")

    connection.close()

# Schedule the job to run every hour
schedule.every().hour.do(enqueue_ndtv_urls)

while True:
    schedule.run_pending()
   # time.sleep(1)
