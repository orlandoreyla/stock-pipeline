from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote


def main():
    create_tables()

    symbol = "AAPL"
    quote = get_stock_quote(symbol)

    insert_stock_quote(symbol, quote)

    print("Inserted:", symbol)


if __name__ == "__main__":
    main()