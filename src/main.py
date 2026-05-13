from src.api.finnhub_client import get_stock_quote
from src.db.schema import create_tables
from src.db.stock_repository import insert_stock_quote, get_all_stock_quotes, get_stock_quote_by_symbol, get_latest_stock_quotes, get_latest_quotes_df
from src.transformations.quote_transformer import transform_stock_quote
from src.analysis.stock_analysis import calculate_average_price, get_top_gainers
from src.visualization.stock_charts import plot_latest_prices

def main():
    df = get_latest_quotes_df()

    avg_price = calculate_average_price(df)
    top_gainer = get_top_gainers(df)

    print("\nAverage Price:")
    print(avg_price)

    print("\nTop Gainer:")
    print(top_gainer)

    plot_latest_prices(df)

if __name__ == "__main__":
    main()