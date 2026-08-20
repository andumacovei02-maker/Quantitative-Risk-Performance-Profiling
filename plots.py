import matplotlib.pyplot as plt
import pandas as pd
import math

def plot_wealth_index(wealth_index) -> None:
    wealth_index.index = wealth_index.index.to_timestamp()
    plt.figure(figsize=(12, 6))
    for col in wealth_index.columns:
        plt.plot(
            wealth_index.index,
            wealth_index[col],
            label=col,
            linewidth=1.8
        )
    plt.title(
        "Historical wealth index growth ( 1,000 Initial Investment)",
        fontsize = 14,
        fontweight = "bold"
    )
    plt.xlabel("Date", fontsize = 11)
    plt.ylabel("Portfolio Value (USD)", fontsize = 11)
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend(title = "Asset", frameon= True)
    plt.tight_layout()
    plt.show()

def plot_drawdown(drawdown)-> None:
    drawdown.index = drawdown.index.to_timestamp()

    plt.figure(figsize=(12, 6))
    for col in drawdown.columns:
        plt.plot(
            drawdown.index,
            drawdown[col] * 100,
            label = col,
            linewidth = 1.5,
        )
    plt.title(
        "Historical drawdowns (Underwater Plot)",
        fontsize = 14, fontweight ="bold" 
    )
    plt.xlabel("Date", fontsize = 11)
    plt.ylabel("Drawdown (%)", fontsize = 11)
    plt.axhline(0, color = "black", linestyle = "--", linewidth = 1, alpha = 0.7)
    plt.grid(True, linestyle = "--", alpha = 0.5)
    plt.legend(title = "Asset", frameon = True)
    plt.tight_layout()
    plt.show()

def plot_dynamic_var_cvar(rets: pd.DataFrame , var_series: pd.Series, cvar_series: pd.Series) -> None:
    num_assets = len(rets.columns)
    cols = 2 
    rows = math.ceil(num_assets/cols)
    fig, axes = plt.subplots(rows, cols, figsize=(14, 5*rows), squeeze = False)
    axes = axes.flatten()
    for i, ticker in enumerate(rets.columns):
        ax = axes[i]

        asset_rets = rets[ticker].dropna()
        var_threshold = -var_series[ticker]
        cvar_value = -cvar_series[ticker]

        counts, bins, patches = ax.hist(asset_rets, bins = 50, density = True, alpha = 0.7, color = 'steelblue', edgecolor = 'black')
        ax.axvline(x = var_threshold, color = 'red', linestyle = '--', linewidth = 2, label = f'VaR: {var_threshold:.2%}')
        ax.axvline(x = cvar_value, color = 'darkred', linestyle = '-', linewidth = 2, label = f'CVaR: {cvar_value:.2%}')

        for b, p in zip(bins, patches):
            if b < var_threshold:
                p.set_facecolor('lightcoral')

        ax.set_title(f'Retruns Distribution : {ticker}', fontsize = 12, fontweight = 'bold')
        ax.set_xlabel('Monthly Return', fontsize = 10)
        ax.set_ylabel('Frequency (Density)', fontsize = 10)
        ax.legend(loc = 'upper left', frameon = True)

    for j in range(num_assets, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    



