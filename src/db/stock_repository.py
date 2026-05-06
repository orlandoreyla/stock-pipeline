from sqlalchemy import text
from src.db.connection import engine

## check for valid stock quote before insertion into the database
def is_valid_stock_quote(quote):
    return quote.get("c") is not None and quote.get("c") != 0

## Insertion for the stock quote data into the database
def insert_stock_quote(symbol, quote):
    if not is_valid_stock_quote(quote):
        print(f"Invalid stock quote for {symbol}, skipping insertion.")
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
        """), {
            "symbol": symbol,
            "current_price": quote.get("c"),
            "change_amount": quote.get("d"),
            "percent_change": quote.get("dp"),
            "high_price": quote.get("h"),
            "low_price": quote.get("l"),
            "open_price": quote.get("o"),
            "previous_close_price": quote.get("pc")
        })
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
            LIMIT : limit;
            """
        ),{"limit": limit})
        return result.fetchall()
    
                            