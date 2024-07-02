import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
import os
import re 

def get_news():
    url = "https://www.ndtv.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h3')
    news_list = [headline.text for headline in headlines[:10]]
    return news_list

def summarize_text(text):
    try:
        summarizer = pipeline("summarization", model="google/pegasus-xsum")
        summary = summarizer(text, max_length=50, min_length=10, do_sample=False)  # Adjust max_length as needed
        if summary and 'summary_text' in summary[0]:
            summary_text = summary[0]['summary_text'].strip()  # Strip any leading/trailing whitespace
            if len(summary_text) > 0:
                return summary_text
        print("Empty or invalid summary generated.")
        return None  # Return None if summary is empty or invalid
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

def text_to_speech(summary, filename):
    if summary:
        # Remove any non-alphanumeric characters from the news title for the filename
        clean_filename = re.sub(r'\W+', '', filename.split('.')[0]) + '.mp3'
        tts = gTTS(summary, lang='te')
        tts.save(clean_filename)
        print(f"Text saved to {clean_filename}")
    else:
        print("Skipping TTS for empty or invalid summary.")

def main():
    news_list = get_news()

    for news in news_list:
        print(news)
        summary = summarize_text(news)
        if summary:
            print(summary)
            text_to_speech(summary, f"{news[:10]}.mp3")
        else:
            print("Skipping empty or invalid summary...")

if __name__ == "__main__":
    main()
