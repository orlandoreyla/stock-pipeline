import requests
from src.config import FINNHUB_API_KEY

def get_stock_quote(symbol):
    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": symbol,
        "token": FINNHUB_API_KEY
    }
    ## example format https://finnhub.io/api/v1/quote?symbol=AAPL&token=API_KEY
    response = requests.get(url, params=params, timeout=30)
        
    ## throws a requests.exceptions.HTTPError if the response was unsuccessful
    response.raise_for_status()

    return response.json()