import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt
import datetime


yf_aapl = yf.download('AAPL', '2000-01-01', '2020-04-01')

aapl_date = yf_aapl.index
aapl_close = yf_aapl['Adj Close']

sma50 = talib.SMA(aapl_close, 50)
sma21 = talib.SMA(aapl_close, 21)

buy_signal = []
sell_signal = []


for i in range(len(yf_aapl)):
    if sma50[i] and sma21[i]:

        date_index = aapl_date[i].date()

        if sma50[i-1] > sma21[i-1] and sma50[i] < sma21[i]:
            buy_signal.append(sma21[i])
            sell_signal.append(np.nan)
            print(date_index, 'Buy')

        elif sma50[i-1] < sma21[i-1] and sma50[i] > sma21[i]:
            buy_signal.append(np.nan)
            sell_signal.append(sma21[i])
            print(date_index, 'Sell')

        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)


plt.plot(aapl_date, buy_signal, 'go')
plt.plot(aapl_date, sell_signal, 'ro')
plt.plot(sma50)
plt.plot(sma21)
plt.plot(aapl_close, 'b')
plt.legend(['Buy', 'Sell', 'SMA50', 'SMA21', 'AAPL'])
plt.show()
