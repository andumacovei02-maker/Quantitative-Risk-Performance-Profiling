import numpy as np
import pandas as pd
import yfinance as yf

# Download monthly total return data (2005-2025) across diverse asset classes:
# Equities (SPY), Gold (GLD), Long-term Treasuries (TLT), Real Estate (VNQ)
def fetch_data(tickers):
    data = yf.download(tickers=tickers,
                     start ="2005-01-01", 
                     end ="2025-12-31",
                     interval="1mo",
                     auto_adjust=True) 
     # Extract automatically adjusted prices for dividens and splits (Total Return)
    prices = data['Close'].copy() 
    prices.index = prices.index.to_period('M') 
    return prices.dropna()


