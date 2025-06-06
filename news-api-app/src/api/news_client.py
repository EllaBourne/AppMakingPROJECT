import requests


class NewsClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"

    def fetch_news(self, query, page=1):
        url = f"{self.base_url}/everything?q={query}&page={page}&apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('articles', [])
        else:
            response.raise_for_status()