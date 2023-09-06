import requests
from bs4 import BeautifulSoup
from datetime import datetime

FINVIZ_BASE_URL = "https://finviz.com/quote.ashx?t="
HEADERS = {'User-Agent': 'Mozilla'}


def scrape_stock_data(stock_name: str) -> dict:
    """
    Scrapes stock data from Finviz and returns a dictionary of stock details.
    
    Args:
        stock_name (str): The stock symbol.
        
    Returns:
        dict: A dictionary containing stock details.
    """

    url = f"{FINVIZ_BASE_URL}{stock_name}"
    response = requests.get(url, headers=HEADERS)