from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote, get_all_stock_quotes, get_stock_quote_by_symbol, get_latest_stock_quotes, get_latest_quotes_df
from src.transformations.quote_transformer import transform_stock_quote
from src.analysis.stock_analysis import calculate_average_price, get_top_gainers

def main():
    avg_price = calculate_average_price(get_latest_quotes_df())
    top_gainer = get_top_gainers(get_latest_quotes_df())
    
    print("\nAverage Price:")
    print(avg_price)

    print("\nTop Gainer:")
    print(top_gainer)

if __name__ == "__main__":
    main()