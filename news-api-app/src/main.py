import requests
from api.news_client import NewsClient
from db.memory_db import MemoryDB

def main():
    # Initialize the in-memory database
    memory_db = MemoryDB()
    
    # Initialize the news client with your API key
    news_client = NewsClient("d4b6777932da4e32ba9d8972d1aa7984")
    
    # Fetch news articles
    articles = news_client.fetch_news("technology")
    
    # Store articles in the in-memory database
    for article in articles:
        memory_db.save_article(article)
    
    # Retrieve and print stored articles
    stored_articles = memory_db.get_articles()
    for article in stored_articles:
        print(article)

if __name__ == "__main__":
    main()