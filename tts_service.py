def generate_bulletin(articles):
    bulletin = ""
    for article in articles:
        title = article['title']
        summary = article.get('summary', 'No summary available')  # Use .get() method to safely retrieve 'summary' or provide default value
        bulletin += f"{title}: {summary}\n\n"

    # Use TTS, TTV, or STV APIs/libraries to generate output
    print(bulletin)  # For demonstration, replace with actual TTS/TTV/STV generation logic

if __name__ == "__main__":
    articles = [
        {"title": "Example Article 1", "content": "Content of example article 1"},
        {"title": "Example Article 2", "content": "Content of example article 2"},
        # Add more articles as needed
    ]
    generate_bulletin(articles)
