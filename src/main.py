from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote, get_all_stock_quotes, get_stock_quote_by_symbol


def main():
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "DIS", "ERROR"]
    
    stocks = get_all_stock_quotes()
    print("Existing stock quotes in the database:")
    for stock in stocks:
        print(stock)    
        
    return     

if __name__ == "__main__":
    main()