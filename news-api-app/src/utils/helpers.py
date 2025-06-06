def format_article(article):
    return {
        "title": article.get("title"),
        "description": article.get("description"),
        "url": article.get("url"),
        "published_at": article.get("publishedAt"),
    }

def validate_article(article):
    required_fields = ["title", "description", "url", "publishedAt"]
    return all(field in article for field in required_fields)