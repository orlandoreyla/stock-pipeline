import matplotlib.pyplot as plt
import os

def plot_latest_prices(df):
    os.makedirs('outputs/charts', exist_ok=True)
    
    plt.figure()
    plt.bar(df['symbol'], df['current_price'], color='blue')
    plt.xlabel('Stock Symbol')
    plt.ylabel('Current Price')
    plt.title('Latest Stock Prices')
    ## plt.show() use this line if you want to display the plot in an interactive environment
    plt.savefig('outputs/charts/latest_stock_prices.png')
    plt.close()
    print("Latest stock prices chart saved as 'latest_stock_prices.png'")