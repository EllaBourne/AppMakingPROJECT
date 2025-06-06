from flask import Flask, render_template
from api.news_client import NewsClient
from db.memory_db import MemoryDB

# Add these imports
from transformers import pipeline
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Initialize once for simplicity
memory_db = MemoryDB()

# Load environment variables from .env file
load_dotenv()
news_api_key = os.environ.get("NEWS_API_KEY")
news_client = NewsClient(news_api_key)

# Load summarization pipeline once at startup
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")

def generate_summary(articles):
    # Concatenate descriptions for summarization
    text = " ".join([a.get("description") or "" for a in articles[:5]])
    if not text.strip():
        return "No summary available today."
    # Increase max_length for a longer summary
    summary = summarizer(text, max_length=200, min_length=60, do_sample=False)
    return summary[0]['summary_text']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/articles")
def articles():
    articles = news_client.fetch_news("fintech")  # Changed to fintech
    memory_db.articles = []  # Clear previous articles
    for article in articles:
        memory_db.save_article(article)
    stored_articles = memory_db.get_articles()
    summary = generate_summary(stored_articles)
    return render_template("articles.html", articles=stored_articles, summary=summary)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
