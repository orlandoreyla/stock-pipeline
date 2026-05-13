from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote, get_all_stock_quotes, get_stock_quote_by_symbol, get_latest_stock_quotes, get_latest_quotes_df
from src.transformations.quote_transformer import transform_stock_quote


def main():
    df = get_latest_quotes_df()
    print(df)
    result = get_latest_stock_quotes()
    for row in result:
        print(row)
    
        
if __name__ == "__main__":
    main()