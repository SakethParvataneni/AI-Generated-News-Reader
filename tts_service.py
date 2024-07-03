import sqlite3 

def generate_tts(summary):
    return f'TTS for: {summary}'  # Placeholder TTS

def create_tts():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute("SELECT url, metadata FROM articles")
    articles = c.fetchall()

    for url, summary in articles:
        tts = generate_tts(summary)
        print(f'Generated TTS for article: {url}')

if __name__ == '__main__':
    create_tts()
