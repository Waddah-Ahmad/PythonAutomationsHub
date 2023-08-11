
# Project: Automated News Headline Scraper
"""
Description: This project automates the process of scraping news headlines from a news website and categorizing them based on keywords.
It utilizes web scraping libraries to extract news headlines and processes the data to provide a summary of recent news in different categories.
"""


import requests
from bs4 import BeautifulSoup
import nltk
from collections import defaultdict

def get_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [headline.text.strip() for headline in soup.find_all('h3') if headline.text.strip()]
    return headlines

def categorize_news(headlines, categories):
    categorized_news = defaultdict(list)

    for headline in headlines:
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in headline.lower():
                    categorized_news[category].append(headline)
                    break

    return categorized_news

if __name__ == "__main__":
    nltk.download('punkt')  # Download required NLTK data

    bbc_url = "https://www.bbc.com/news"
    news_headlines = get_news_headlines(bbc_url)

    # Define categories and keywords for categorization
    categories = {
        'Politics': ['politics', 'government', 'election'],
        'Technology': ['technology', 'innovation', 'digital'],
        'Health': ['health', 'wellness', 'medicine'],
        'Environment': ['environment', 'climate', 'ecology']
    }

    categorized_news = categorize_news(news_headlines, categories)

    for category, headlines in categorized_news.items():
        print(f"{category} News:")
        for headline in headlines:
            print("- " + headline)
        print("\n")