import os
from dotenv import load_dotenv

load_dotenv()

# Finnhub
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

# Database
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Validation
if not FINNHUB_API_KEY:
    raise SystemExit("Missing FINNHUB_API_KEY in .env")

if not all([DB_USER, DB_HOST, DB_PORT, DB_NAME]):
    raise SystemExit("Missing DB config in .env")