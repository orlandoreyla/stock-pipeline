import requests
from config import FINNHUB_API_KEY

def get_stock_quote(symbol):
    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": symbol,
        "token": FINNHUB_API_KEY
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()