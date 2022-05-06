import yfinance as yf
import talib
import numpy as np
import matplotlib.pyplot as plt


yf_aapl = yf.download('AAPL', '2000-01-01', '2020-04-01')
aapl_close = yf_aapl['Adj Close']
sma50 = talib.SMA(aapl_close, 50)
sma21 = talib.SMA(aapl_close, 21)
sma21_l = []
sma50_l = []
count_index = -1
sell = []
buy = []

for i in sma21:
    sma21_l.append(i)
    if sma50_l == []:
        for i2 in sma50:
            sma50_l.append(i2)


for i3 in sma21_l:
    try:
        count_index += 1
        if sma21_l[count_index] <= sma50_l[count_index]:
            if sma21_l[count_index + 1] >= sma50_l[count_index + 1]:
                buy.append(count_index)
                print('buy')

        elif sma21_l[count_index] >= sma50_l[count_index]:
            if sma21_l[count_index + 1] <= sma50_l[count_index + 1]:
                sell.append(count_index)
                print('sell')
    except IndexError:
        break


sell_l = []
buy_l = []
for i4 in sell:
    sell_l.append(sma21[i4])


for i5 in buy:
    buy_l.append(sma21[i5])


print('sell', sell_l)
print('buy', buy_l)
print(len(aapl_close))
print(len(sma50))
print(len(sma21))

# plt.plot(sma50)
# plt.plot(sma21)
# plt.plot(aapl_close)
# plt.plot(sell_l)
# plt.show()
