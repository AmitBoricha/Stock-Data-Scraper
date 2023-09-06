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

    if response.status_code == 200:
        res = {}
        soup = BeautifulSoup(response.text, 'html.parser')

        stock_symbol = soup.find('h1').find('a', class_='tab-link').text
        stock_name = soup.select_one('a.tab-link b').get_text(strip=True)

        table = soup.find('table', {'class': 'snapshot-table2'})
        
        res['stock_symbol'] = stock_symbol
        res['stock_name'] = stock_name
        res['scrape_timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        stock_details = {}

        for row in table.find_all('tr'):
            cell_iterator = iter(row.find_all('td'))
            for current, next_value in zip(cell_iterator, cell_iterator):
                current_text = current.get_text(strip=True)
                next_text = next_value.get_text(strip=True)

                if current_text and next_text:
                    stock_details[current_text] = next_text
        res['stock_details'] = stock_details
        return res