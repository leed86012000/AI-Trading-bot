import pandas as pd
import numpy as np

# Generate fake stock price data
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=100)
prices = 100 + np.random.randn(100).cumsum()
data = pd.DataFrame({"Date": dates, "Close": prices})
data.set_index("Date", inplace=True)

# Moving averages
data["SMA_5"] = data["Close"].rolling(window=5).mean()
data["SMA_20"] = data["Close"].rolling(window=20).mean()

# Trading signals
data["Signal"] = 0
data.loc[data["SMA_5"] > data["SMA_20"], "Signal"] = 1   # Buy
data.loc[data["SMA_5"] < data["SMA_20"], "Signal"] = -1  # Sell

# Simple strategy performance
data["Returns"] = data["Close"].pct_change()
data["Strategy"] = data["Signal"].shift(1) * data["Returns"]

print("Total Strategy Return:", data["Strategy"].cumsum().iloc[-1])
print(data.tail(10))
