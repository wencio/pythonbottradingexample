import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the historical data into a DataFrame
df = pd.read_csv("data.csv")

# Calculate the simple moving average of the closing prices
df['SMA50'] = df['Close'].rolling(window=50).mean()
df['SMA200'] = df['Close'].rolling(window=200).mean()

# Buy when SMA50 crosses above SMA200, sell when SMA50 crosses below SMA200
df['Order'] = np.where(df['SMA50'] > df['SMA200'], 1, -1)

# Plot the moving averages and the buy/sell signals
plt.plot(df['Close'])
plt.plot(df['SMA50'])
plt.plot(df['SMA200'])
plt.scatter(df.index, df['Close'], c=df['Order'], cmap='viridis')
plt.show()
