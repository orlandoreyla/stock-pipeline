import os 
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FINNHUB_API_KEY")
if not API_KEY:
    raise SystemExit("Missing FINNHUB_API_KEY in .env")

symbol = "AAPL"
url = "https://finnhub.io/api/v1/quote"
params = {"symbol": symbol, "token": API_KEY}

r = requests.get(url, params=params, timeout=30)
print("Status:", r.status_code)
print(r.json())

