TICKERS = ['GLD','SPY','TLT','VNQ']
DATA_RANGE  = ("2005-01-01", "2025-12-31")
INTERVAL = "1mo"
RISK_FREE_RATE = 0.02
INITIAL_INVESTMENT = 1000
CONFIDENCE_LEVEL = 0.95
INTERVAL_MAPPING = {
    "1d" : ("Daily", 252),
    "1wk" : ("Weekly", 52),
    "1mo" : ("Monthly", 12),
}

