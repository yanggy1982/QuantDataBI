# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : stock_daily_ma.py
@time    : 2025/12/3 01:21
@desc    : 包含均线的日线数据
-----------------------------------------------------------------------
"""

import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

if __name__ == '__main__':
    print("stock_daily_ma...")

    # 获取股票数据
    stock_code = "002611"
    start_date = "19700101"
    end_date = "20500101"
    df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start_date, end_date=end_date)

    # 数据预览
    print(df.head())

    # 转换日期格式
    df['date'] = pd.to_datetime(df['日期'])
    df.set_index('date', inplace=True)

    # 计算5日和20日移动平均线
    df['MA5'] = df['收盘'].rolling(window=5).mean()
    df['MA20'] = df['收盘'].rolling(window=20).mean()

    # 策略：当MA5上穿MA20时买入，下穿时卖出
    df['Signal'] = 0
    df.loc[df['MA5'] > df['MA20'], 'Signal'] = 1
    df.loc[df['MA5'] < df['MA20'], 'Signal'] = -1

    # 绘制策略信号图
    plt.figure(figsize=(12, 6))
    plt.plot(df['收盘'], label='收盘价')
    plt.plot(df['MA5'], label='MA5')
    plt.plot(df['MA20'], label='MA20')
    plt.grid(True)
    plt.title('东方精工(002611)-MACD交易策略')
    plt.xlabel('日期')
    plt.ylabel('收盘价')
    plt.legend()
    plt.show()



