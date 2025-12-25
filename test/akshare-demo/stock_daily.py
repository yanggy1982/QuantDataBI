# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : stock_daily.py
@time    : 2025/12/3 00:42
@desc    : 各股日线数据
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
    print("stock_daily...")

    # 获取股票数据
    stock_code = "002611"
    start_date = "19700101"
    end_date = "20500101"
    df = ak.stock_zh_a_hist(symbol = stock_code,period = "daily",start_date = start_date,end_date = end_date)

    # 数据预览
    print(df.head())

    # 转换日期格式
    df['date'] = pd.to_datetime(df['日期'])
    df.set_index('date', inplace=True)

    # 绘制收盘价趋势图
    plt.figure(figsize=(12, 6))
    plt.plot(df['收盘'], label='收盘')
    plt.grid(True)
    plt.title('东方精工(002611)')
    plt.xlabel('日期')
    plt.ylabel('收盘')
    plt.legend()
    plt.show()
