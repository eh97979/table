import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt


yf_aapl = yf.download('AAPL', '2000-01-01', '2020-04-01')
aapl_close = yf_aapl['Adj Close']
sma50 = talib.SMA(aapl_close, 50)
sma21 = talib.SMA(aapl_close, 21)

sell_buy = {}

for i in range(len(sma50)):
    if i+1 < 5094:
        if sma21[i] >= sma50[i]:
            if sma21[i+1] < sma50[i+1]:
                sell_buy[sma50[i]] = 'buy'
        elif sma21[i] <= sma50[i]:
            if sma21[i+1] > sma50[i+1]:
                sell_buy[sma50[i]] = 'sell'






print(sell_buy)
print(len(sma50))


# plt.plot(sma50)
# plt.plot(sma21)
# plt.plot(aapl_close)
# plt.show()
