 import pandas as pd
import numpy as np

def compute_rets(prices: pd.DataFrame) -> pd.DataFrame:
    return prices.pct_change().dropna()

def annualized_rets(rets: pd.DataFrame, periods_per_year: int = 12) -> pd.Series:
    n_periods = rets.shape[0]
    compound_growth = (rets+1).prod()
    return compound_growth**(periods_per_year/n_periods) - 1

def annualized_volatility(rets: pd.DataFrame, periods_per_year: int = 12) -> pd.Series:
    return rets.std()*(np.sqrt(periods_per_year))

def sharpe_ratio(rets: pd.DataFrame, risk_free_rate : float = 0.0, periods_per_year : int = 12) -> pd.Series:
    cagr = annualized_rets(rets, periods_per_year)
    vol = annualized_volatility(rets, periods_per_year)
    return (cagr-risk_free_rate)/vol

def calculate_drawdown(rets: pd.DataFrame) -> dict:
    wealth_index = 1000 * (1 + rets).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdown = (wealth_index - previous_peaks) / previous_peaks
    max_drawdown = drawdown.min()
    return {
        "wealth_index" : wealth_index,
        "peaks" : previous_peaks,
        "drawdown" : drawdown,
        "max_drawdown" : max_drawdown 
    }