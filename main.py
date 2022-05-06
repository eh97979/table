import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt
import datetime


yf_aapl = yf.download('AAPL', '2000-01-01', '2020-04-01')
aapl_close = yf_aapl['Adj Close']
sma50 = talib.SMA(aapl_close, 50)
sma21 = talib.SMA(aapl_close, 21)
date_buy_sell = []
value_buy_sell = []


for i in range(len(sma50)):
    if i+1 < 5094:
        if sma21[i] >= sma50[i]:
            if sma21[i+1] < sma50[i+1]:
                value_buy_sell.append(sma21[i])
                date_buy_sell.append(str(sma21[i:i + 1:])[5:15:])
        elif sma21[i] <= sma50[i]:
            if sma21[i+1] > sma50[i+1]:
                value_buy_sell.append(sma21[i])
                date_buy_sell.append(str(sma21[i:i + 1:])[5:15:])


print(date_buy_sell)
print(value_buy_sell)


# plt.plot(date_buy_sell[1::2], value_buy_sell[1::2], 'ro')
# plt.plot(date_buy_sell[0::2], value_buy_sell[0::2], 'ro')
# plt.plot(sma50)
# plt.plot(sma21)
# plt.plot(aapl_close)
plt.show()
