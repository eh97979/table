import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt


a1 = yf.download('AAPL', '2000-01-01', '2020-04-01')
a3 = a1['Adj Close']
sma50 = talib.SMA(a1['Adj Close'], 50)
sma21 = talib.SMA(a1['Adj Close'], 21)


b = 0


for i in sma50:

    b += 1
    try:
        if i >= sma21[b-1]:
            if i <= sma21[b]:
                date_b = str(sma21[b:b+1])
                print('покупаю', date_b[5:15:])

        elif i <= sma21[b - 1]:
            if i >= sma21[b]:
                date_s = str(sma21[b:b + 1])
                print('продаю', date_s[5:15:])
    except IndexError:
        break


plt.plot(sma50, label='SMA50')
plt.plot(sma21, label='SMA21')
plt.plot(a3)
plt.show()