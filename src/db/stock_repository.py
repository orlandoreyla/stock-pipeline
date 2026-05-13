from sqlalchemy import text
import pandas as pd
from src.db.connection import engine

## check for valid stock quote before insertion into the database
def is_valid_stock_quote(quote_data):
    return quote_data.get("current_price") is not None and quote_data.get("current_price") != 0

## Insertion for the stock quote data into the database
def insert_stock_quote(quote_data):
    if not is_valid_stock_quote(quote_data):
        print(f"Invalid stock quote for {quote_data.get('symbol')}, skipping insertion.")
        return
    
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO stock_quotes (
                symbol,
                current_price,
                change_amount,
                percent_change,
                high_price,
                low_price,
                open_price,
                previous_close_price
            )
            VALUES (
                :symbol,
                :current_price,
                :change_amount,
                :percent_change,
                :high_price,
                :low_price,
                :open_price,
                :previous_close_price
            );
        """), quote_data)
        conn.commit()
        
## fetch all of the stock quotes from the database
def get_all_stock_quotes():
    with engine.connect() as conn:
        result = conn.execute(text("""
                               SELECT * FROM stock_quotes
                               Order by created_at DESC;
                                   """))
        return result.fetchall()
    
## fetch stock quote by symbol from the database    
def get_stock_quote_by_symbol(symbol):
    with engine.connect() as conn:
        result = conn.execute(text("""
                                   SELECT * FROM stock_quotes
                                   where symbol = :symbol
                                Order by created_at DESC;
                                   """), {"symbol": symbol})
        return result.fetchall()
    
def get_latest_stock_quotes(limit=10):
    with engine.connect() as conn:
        result = conn.execute(text(
            """
            SELECT * FROM stock_quotes
            ORDER BY created_at DESC
            LIMIT :limit;
            """
        ),{"limit": limit})
        return result.fetchall()
    
    
def get_latest_quotes_df(limit=10):
    with engine.connect() as conn:
        df = pd.read_sql(text("""
            SELECT symbol, current_price, percent_change, created_at
            FROM stock_quotes
            ORDER BY created_at DESC
            LIMIT :limit;
        """), conn, params={"limit": limit})

        return df
    
                            