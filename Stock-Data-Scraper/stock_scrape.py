import requests
from bs4 import BeautifulSoup
from datetime import datetime

FINVIZ_BASE_URL = "https://finviz.com/quote.ashx?t="
HEADERS = {'User-Agent': 'Mozilla'}
