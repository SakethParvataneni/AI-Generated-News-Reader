# schedule_tasks.py

import time
import sched

# Example function to enqueue URLs based on schedule
def enqueue_scraping(url, category, scheduler):
    print(f"Enqueuing {url} for category {category}...")
    # Logic to enqueue URL for scraping goes here

# Example scheduler
def main_scheduler():
    s = sched.scheduler(time.time, time.sleep)
    interval = 3600  # Example interval: every 1 hour

    # Example URLs and categories
    urls = [
        ("https://feeds.feedburner.com/ndtvmovies-latest", "movies"),
        # Add more URLs and categories as needed
    ]

    for url, category in urls:
        enqueue_scraping(url, category, s)
        s.enter(interval, 1, enqueue_scraping, (url, category, s))
    
    s.run()

if __name__ == "__main__":
    main_scheduler()
