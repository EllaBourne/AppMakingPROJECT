class MemoryDB:
    def __init__(self):
        self.articles = []

    def save_article(self, article):
        self.articles.append(article)

    def get_articles(self):
        return self.articles[:]  # Return a copy of the articles list to prevent modification