import numpy as np
import pandas as pd
from data_loader import fetch_data
from analytics import (
    compute_rets,
    annualized_rets,
    annualized_volatility,
    sharpe_ratio,
    calculate_drawdown) 

def main():
    tickers= ['SPY', 'GLD', 'TLT', 'VNQ']
    prices = fetch_data(tickers)
    rets = compute_rets(prices)

    cagr = annualized_rets(rets, periods_per_year=12)
    vol = annualized_volatility(rets, periods_per_year=12)
    sharpe = sharpe_ratio(rets, risk_free_rate=0.02, periods_per_year=12)

    dd_data = calculate_drawdown(rets)
    max_dd = dd_data["max_drawdown"]

    summary = pd.DataFrame({
        "CAGR" : cagr,
        "Annualized Volatility" : vol,
        "Sharpe Ratio (Rf=2%)" : sharpe,
        "Max Drawdown" : max_dd
    })

    summary_formatted = pd.DataFrame({
        "CAGR" : summary["CAGR"].apply(lambda x: f"{x:.2%}"),
        "Annualized Volatility" : summary["Annualized Volatility"].apply(lambda x: f"{x:.2%}"),
        "Sharpe Ratio (Rf=2%)" : summary["Sharpe Ratio (Rf=2%)"].round(2),
        "Max Drawdown" : summary["Max Drawdown"].apply(lambda x: f"{x:.2%}")
    })

    print("=" * 74)
    print("       MULTI-ASSET RISK-RETURN SUMMARY (2005 - 2025)")
    print("=" * 74)
    print(summary_formatted)
    print("="*74 + "\n")

if __name__ == "__main__":
    main()
