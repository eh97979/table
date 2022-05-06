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

date_index = -1
date_sma = []
sma_index = []


for i in range(len(yf_aapl)):
    if sma50[i] and sma21[i]:
        if sma50[i-1] > sma21[i-1] and sma50[i] < sma21[i]:
            date_sma.append(aapl_date[i].date())
            sma_index.append(sma50[i])
            date_index += 1
            print(date_sma[date_index], 'Buy')
        elif sma50[i-1] < sma21[i-1] and sma50[i] > sma21[i]:
            date_sma.append(aapl_date[i].date())
            sma_index.append(sma50[i])
            date_index += 1
            print(date_sma[date_index], 'Sell')


# plt.plot(date_sma, sma_index, 'b')
plt.plot(date_sma[1::2], sma_index[1::2], 'go')
plt.plot(date_sma[0::2], sma_index[0::2], 'ro')

plt.plot(sma50)
plt.plot(sma21)
plt.plot(aapl_close, 'b')
plt.legend(['Buy', 'Sell', 'SMA50', 'SMA21', 'AAPL'])
plt.show()
