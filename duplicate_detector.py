import sqlite3
import hashlib

def get_article_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

def detect_duplicates():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute("SELECT url, content FROM articles")
    articles = c.fetchall()

    hashes = {}
    duplicates = []

    for url, content in articles:
        article_hash = get_article_hash(content)
        if article_hash in hashes:
            duplicates.append(url)
        else:
            hashes[article_hash] = url

    for url in duplicates:
        c.execute("DELETE FROM articles WHERE url=?", (url,))
        print(f'Removed duplicate article: {url}')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    detect_duplicates()
