import numpy as np
import pandas as pd
import yfinance as yf

def fetch_data(tickers):
    data = yf.download(tickers=tickers,
                     start ="2005-01-01", 
                     end ="2025-12-31",
                     interval="1mo",
                     auto_adjust=True) 

    prices = data['Close'].copy() 
    prices.index = prices.index.to_period('M') 
    return prices.dropna()


