from tabulate import tabulate
from data_loader import fetch_data
from plots import (plot_wealth_index, plot_drawdown, plot_dynamic_var_cvar)
from utils import risk_return_summary
from analytics import (
    compute_rets,
    annualized_rets,
    annualized_volatility,
    sharpe_ratio,
    calculate_drawdown,
    var_historic,
    cvar_historic
    )
from config import(
    TICKERS,
    DATA_RANGE,
    INTERVAL,
    RISK_FREE_RATE,
    CONFIDENCE_LEVEL,
    INITIAL_INVESTMENT,
    INTERVAL_MAPPING
)
if INTERVAL not in INTERVAL_MAPPING:
    raise ValueError(f"Interval not supported. Use only from: {list(INTERVAL_MAPPING.keys())}")
PREFIX, PERIODS_PER_YEAR = INTERVAL_MAPPING[INTERVAL]


def main():
    prices = fetch_data(TICKERS, DATA_RANGE, INTERVAL)
    rets = compute_rets(prices)

    cagr = annualized_rets(rets, PERIODS_PER_YEAR)
    vol = annualized_volatility(rets, PERIODS_PER_YEAR)
    sharpe = sharpe_ratio(rets, RISK_FREE_RATE, PERIODS_PER_YEAR)
    dd_data = calculate_drawdown(rets, INITIAL_INVESTMENT)
    max_dd = dd_data["max_drawdown"]
    var = var_historic(rets, 1-CONFIDENCE_LEVEL)
    cvar = cvar_historic(rets, 1-CONFIDENCE_LEVEL)

    risk_return_summary(cagr, vol, sharpe, max_dd, var, cvar, PREFIX)
    plot_wealth_index(dd_data["wealth_index"])
    plot_drawdown(dd_data["drawdown"])
    plot_dynamic_var_cvar(rets, var, cvar) 

if __name__ == "__main__":
    main()
