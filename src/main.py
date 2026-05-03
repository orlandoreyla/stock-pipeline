from src.finnhub_client import get_stock_quote

def main():
    symbol = "AAPL"
    data = get_stock_quote(symbol)

    print(f"Stock: {symbol}")
    print(data)

if __name__ == "__main__":
    main()