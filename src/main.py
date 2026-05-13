from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote, get_all_stock_quotes, get_stock_quote_by_symbol, get_latest_stock_quotes, get_latest_quotes_df
from src.transformations.quote_transformer import transform_stock_quote
from src.analysis.stock_analysis import calculate_average_price, get_top_gainers
from src.visualization.stock_charts import plot_latest_prices
from src.pipeline.stock_pipeline import ingest_stock_quotes
from src.utils.stock_loader import load_stock_symbols

def main():
    create_tables()
    
    symbols = load_stock_symbols()
    ingest_stock_quotes(symbols)

    df = get_latest_quotes_df()
    
    print("\nAverage Price: ")
    print(calculate_average_price(df))
    
    print("\nTop Gainers: ")
    print(get_top_gainers(df))
    
    plot_latest_prices(df)

if __name__ == "__main__":
    main()