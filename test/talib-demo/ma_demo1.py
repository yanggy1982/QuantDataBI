# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : ma_demo1.py
@time    : 2025/12/18 23:23
@desc    : 
-----------------------------------------------------------------------
"""

import akshare as ak
import talib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':
    print("ma_demo1...")

    symbol = "600635"
    start_time = "20250901"
    end_time = "20251218"
    stock_name = "大众公用"

    stock_df = ak.stock_zh_a_hist(symbol, period="daily", start_date=start_time, end_date=end_time)

    stock_df['date'] = pd.to_datetime(stock_df['日期'])
    stock_df.set_index('date', inplace=True)

    stock_df['MA5'] = talib.MA(stock_df['收盘'], timeperiod=5)

    print(stock_df.head())

    plt.figure(figsize=(12, 6))
    plt.plot(stock_df['收盘'], label='Close Price')
    plt.plot(stock_df['MA5'], label='MA5')
    plt.grid(True)
    plt.title('MACD交易策略')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
