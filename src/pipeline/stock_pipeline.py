from src.api.finnhub_client import get_stock_quote
from src.db.stock_repository import get_latest_quotes_df, insert_stock_quote
from src.transformations.quote_transformer import transform_stock_quote
from src.utils.logger import logger

## Ingest stock quotes for a list of symbols through the API, transform them, and store in the database
def ingest_stock_quotes(symbols):
    for symbol in symbols:
        ## bad API called/error
        try:
            raw_quote = get_stock_quote(symbol)
            quote_data = transform_stock_quote(symbol, raw_quote)
            inserted = insert_stock_quote(quote_data)
            
            ## good quote inserted into the database
            if inserted:
                logger.info(f"Ingested quote for {symbol}")
            else: ## bad quote/symbol that failed validation
                logger.warning(f"Quote for {symbol} was not inserted due to validation failure.")   
            
        except Exception as e:
            logger.error(f"Failed to process {symbol}: {e}")