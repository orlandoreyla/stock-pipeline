def calculate_average_price(df):
    return df['current_price'].mean()

def get_top_gainers(df, top_n=5):
    return df.loc[df['percent_change'].idxmax()]