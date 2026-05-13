

def load_stock_symbols(file_path = 'config/stocks.txt'):
    with open(file_path, 'r') as f:
        symbols = [line.strip() for line in f if line.strip()]
        return symbols