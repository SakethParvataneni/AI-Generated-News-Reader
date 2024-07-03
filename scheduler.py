
import time
import pika

def enqueue_urls():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='urls')

    urls = [
        'https://feeds.feedburner.com/ndtvmovies-latest',
        
    ]

    for url in urls:
        channel.basic_publish(exchange='', routing_key='urls', body=url)
        print(f'Enqueued {url}')
    
    connection.close()

if __name__ == '__main__':
    while True:
        enqueue_urls()
        time.sleep(3600)  # Run every hour
