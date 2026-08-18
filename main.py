import numpy as np
import pandas as pd
from data_loader import fetch_data
from plots import (plot_wealth_index, plot_drawdown)
from analytics import (
    compute_rets,
    annualized_rets,
    annualized_volatility,
    sharpe_ratio,
    calculate_drawdown,
    var_historic,
    cvar_historic
    ) 

pd.set_option("display.max.columns", None)

TICKERS = ['SPY', 'GLD', 'TLT', 'VNQ']
DATA_RANGE  = ("2005-01-01", "2025-12-31")
INTERVAL = "1mo"
PERIODS_PER_YEAR = 12
RISK_FREE_RATE = 0.02
INITIAL_INVESTMENT = 1000
CONFIDENCE_LEVEL = 0.95

def main():
   
    prices = fetch_data(TICKERS, DATA_RANGE, INTERVAL)
    rets = compute_rets(prices)

    cagr = annualized_rets(rets, PERIODS_PER_YEAR)
    vol = annualized_volatility(rets, PERIODS_PER_YEAR)
    sharpe = sharpe_ratio(rets, RISK_FREE_RATE, PERIODS_PER_YEAR)

    dd_data = calculate_drawdown(rets, INITIAL_INVESTMENT)
    max_dd = dd_data["max_drawdown"]

    var_95 = var_historic(rets, 1-CONFIDENCE_LEVEL)
    cvar_95 = cvar_historic(rets, 1-CONFIDENCE_LEVEL)

    summary = pd.DataFrame({
        "CAGR" : cagr,
        "Annualized Volatility" : vol,
        "Sharpe Ratio (Rf=2%)" : sharpe,
        "Max Drawdown" : max_dd,
        "Monthly VaR (95%)" : var_95,
        "Monthly CVaR (95%)" : cvar_95
    })

    summary_formatted = summary.copy()
    pct_cols = [
        "CAGR",
        "Annualized Volatility",
        "Max Drawdown",
        "Monthly VaR (95%)",
        "Monthly CVaR (95%)",
        ]

    for col in pct_cols:
        summary_formatted[col] = summary_formatted[col].apply(lambda x: f"{x:.2%}")
    summary_formatted["Sharpe Ratio (Rf=2%)"] = summary_formatted["Sharpe Ratio (Rf=2%)"].round(2)

    print("=" * 60)
    print("       MULTI-ASSET RISK-RETURN SUMMARY (2005 - 2025)")
    print("=" * 60)
    print(summary_formatted)
    print("="*60 + "\n")

    plot_wealth_index(dd_data["wealth_index"])
    plot_drawdown(dd_data["drawdown"])

if __name__ == "__main__":
    main()
