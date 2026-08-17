# Quantitative Risk & Performance Profiling

A python module for historical financial data analysis, risk metrics computation, and performance evaluation across multi-asset portfolios.

### Features
1. Automated data fetching using `yfinance`
2. Monthly compound return computation 
3. Compounded Annual Growth Rate -CAGR- using geometric compounding
4. Annualized Volatility calculation scaled by the square root of periods
5. Sharpe Ratio computation relative to a customizable Risk-Free Rate
6. Cumulative Peak tracking and Maximum Drawdown analysis
7. Monthly VaR and CVaR measurement at 95% confidence level 

### Analysed Assets (2005-2025)
1. SPY - US Equities (S&P500)
2. GLD - Gold Trust
3. TLT - 20+ Year Treasury Bonds
4. VNQ - Real Estate 

### Project Structure
1. `data_loader.py` - Fetches adjusted monthly closing prices
2. `analytics.py` - Vectorized financial formulas
3. `main.py` - Pipeline execution and results summary

### How to Run
```bash
pip install pandas numpy yfinance
python main.py 
```