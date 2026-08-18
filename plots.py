import matplotlib.pyplot as plt
import pandas as pd

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



