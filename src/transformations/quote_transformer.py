

def transform_stock_quote(symbol, quote):
    return {
        "symbol": symbol.upper(),
        "current_price": quote.get("c"),
        "change_amount": quote.get("d"),
        "percent_change": quote.get("dp"),
        "high_price": quote.get("h"),
        "low_price": quote.get("l"),
        "open_price": quote.get("o"),
        "previous_close_price": quote.get("pc")   
    }