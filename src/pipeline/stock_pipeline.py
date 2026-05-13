from src.api.finnhub_client import get_stock_quote
from src.db.stock_repository import get_latest_quotes_df, insert_stock_quote
from src.transformations.quote_transformer import transform_stock_quote


## Ingest stock quotes for a list of symbols through the API, transform them, and store in the database
def ingest_stock_quotes(symbols):
    for symbol in symbols:
        raw_quote = get_stock_quote(symbol)
        quote_data = transform_stock_quote(symbol, raw_quote)
        insert_stock_quote(quote_data)
        print(f"Inserted quote for {symbol}")