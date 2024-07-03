# summarizer.py
import sqlite3

def generate_summary(content):
    return content[:200] + '...'  # Placeholder summary

def summarize_articles():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute("SELECT url, content FROM articles")
    articles = c.fetchall()

    for url, content in articles:
        summary = generate_summary(content)
        c.execute("UPDATE articles SET metadata=? WHERE url=?", (summary, url))
        print(f'Summarized article: {url}')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    summarize_articles()
