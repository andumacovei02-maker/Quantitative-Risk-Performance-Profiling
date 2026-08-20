import pandas as pd
from tabulate import tabulate
from config import RISK_FREE_RATE, CONFIDENCE_LEVEL, DATA_RANGE

def risk_return_summary(cagr: pd.Series, vol: pd.Series, sharpe: pd.Series, max_dd: dict, var: pd.Series, cvar: pd.Series, PREFIX: str) -> None:
    sharpe_col = f'Sharpe Ratio (Rf={RISK_FREE_RATE*100:.0f}%)'
    var_col = f'{PREFIX} VaR ({CONFIDENCE_LEVEL*100:.0f}%)'
    cvar_col = f'{PREFIX} CVaR ({CONFIDENCE_LEVEL*100:.0f}%)'
    summary = pd.DataFrame({
        "CAGR" : cagr,
        "Annualized Volatility" : vol,
        sharpe_col : sharpe,
        "Max Drawdown" : max_dd,
        var_col : var,
        cvar_col : cvar,
    })
    
    summary_formatted = summary.copy()
    pct_cols = [
        "CAGR",
        "Annualized Volatility",
        "Max Drawdown",
        var_col,
        cvar_col,
        ]

    for col in pct_cols:
        summary_formatted[col] = summary_formatted[col].apply(lambda x: f"{x:.2%}")
    summary_formatted[sharpe_col] = summary_formatted[sharpe_col].round(2)

    print(f" # MULTI-ASSET RISK-RETURN SUMMARY ({DATA_RANGE[0][:4]} - {DATA_RANGE[1][:4]}) #")
    print(
        tabulate(
            summary_formatted,
            headers = "keys",
            tablefmt = "fancy_grid",
            showindex = True
        )
    )