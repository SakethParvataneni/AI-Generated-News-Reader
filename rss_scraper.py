import feedparser
import pika

def scrape_rss(feed_url):
    feed = feedparser.parse(feed_url)
    urls = [entry.link for entry in feed.entries]

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detail_urls')

    for url in urls:
        channel.basic_publish(exchange='', routing_key='detail_urls', body=url)
        print(f'Enqueued detail URL: {url}')
    
    connection.close()

def callback(ch, method, properties, body):
    feed_url = body.decode()
    scrape_rss(feed_url)

def consume_rss_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='urls')

    channel.basic_consume(queue='urls', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages...')
    channel.start_consuming()

if __name__ == '__main__':
    consume_rss_queue()
