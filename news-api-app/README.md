# News API Application

This project is a Python application that retrieves news articles from a news API and stores them in an in-memory database. 

## Project Structure

```
news-api-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── api
│   │   └── news_client.py  # Handles API calls to fetch news
│   ├── db
│   │   └── memory_db.py    # In-memory database for storing articles
│   └── utils
│       └── helpers.py       # Utility functions for data processing
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd news-api-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the application, fetch the latest news articles, and store them in the in-memory database.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.