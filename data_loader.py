import pandas as pd
import yfinance as yf

def fetch_data(tickers: list, data_range: tuple, interval: str = "1mo") -> pd.DataFrame:
    start_date, end_date = data_range
    data = yf.download(tickers=tickers,
                     start =start_date, 
                     end =end_date,
                     interval=interval,
                     auto_adjust=True) 

    prices = data['Close'].copy() 
    prices.index = prices.index.to_period('M') 
    return prices.dropna()


