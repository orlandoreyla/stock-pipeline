from sqlalchemy import text
from src.db.connection import engine


def create_tables():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS stock_quotes (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR(10) NOT NULL,
                current_price NUMERIC,
                change_amount NUMERIC,
                percent_change NUMERIC,
                high_price NUMERIC,
                low_price NUMERIC,
                open_price NUMERIC,
                previous_close_price NUMERIC,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """))
        conn.commit()