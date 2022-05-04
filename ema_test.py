import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt

a1 = yf.download('AAPL', '2000-01-01', '2020-04-01')
a2 = np.array([1, 2, 3])

a3 = a1['Adj Close']
sma50 = talib.SMA(a1['Adj Close'], 50)
sma21 = talib.SMA(a1['Adj Close'], 21)


plt.plot(sma50, label='SMA50')
plt.plot(sma21, label='SMA21')
plt.plot(a3)
plt.show()


