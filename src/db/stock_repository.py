from sqlalchemy import text
from src.db.connection import engine


def insert_stock_quote(symbol, quote):
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