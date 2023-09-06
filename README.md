Stock Data Scraper

This Python script is a simple web scraper that retrieves stock data from Finviz for a given stock symbol. It uses the requests library to make HTTP requests and BeautifulSoup for HTML parsing. The scraped data includes the stock symbol, stock name, and various stock details.

Features
Scrapes stock data from Finviz based on the provided stock symbol.
Extracts and presents relevant stock details in a dictionary format.
Provides a simple command-line interface for user interaction.

Clone this repository to your local machine.
Install the required libraries using pip install -r requirements.txt.
Run the script by executing python stock_scraper.py.
Enter the stock symbol when prompted.

The script will fetch and display the stock data, including the stock symbol, stock name, and other details, such as market cap, P/E ratio, EPS, etc.

Feel free to use and modify this script to suit your needs. If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

Dependencies
requests: HTTP library for making requests.
BeautifulSoup: HTML parsing library for web scraping.
