from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote, get_all_stock_quotes, get_stock_quote_by_symbol, get_latest_stock_quotes
from src.transformations.quote_transformer import transform_stock_quote


def main():
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "DIS", "ERROR"]
    
    for symbol in symbols:
        raw_quote = get_stock_quote(symbol)
        quote_data = transform_stock_quote(symbol, raw_quote)
        insert_stock_quote(quote_data)
        print(f"Inserted quote for {symbol}")

    stocks =get_latest_stock_quotes(5)
    for stock in stocks:
        print(f"latest inserted stocks: {stock.symbol}")
    return
        
if __name__ == "__main__":
    main()