# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : donchian_channel.py
@time    : 2025/12/21 13:47
@desc    :
唐奇安通道
1、主要思想：
寻找一定时间内(如20日)出现的最高价和最低价，将最高价和最低价分布作为通道的上下轨道，规则如下：
（1）当价格突破上轨道时，说明股价运动较强势，释放出买入信号；
（2）当价格线向下突破下轨道的时候，空方市场较为强势，市场下跌趋势较为明显，则释放出卖出信号

2、组成
唐奇安通道由三条轨道线构成：
通道上界 = 过去20日内的最高价
通道下界 = 过去20日内的最低价
         通 道 上 界 + 通 道 下 界
中轨道 =  -----------------------
                 2
通道上界+通道下界
-----------------------------------------------------------------------
"""
import numpy as np

from strategy.utils.ak_data_tools import get_daily_df
from strategy.utils.talib_feature_tools import calc_sma
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

my_colr = mpf.make_marketcolors(up='red',
                                down='green',
                                edge='inherit',
                                wick='inherit',
                                volume='inherit')

my_style = mpf.make_mpf_style(
    base_mpf_style='nightclouds',
    marketcolors=my_colr,
    gridaxis='horizontal',
    y_on_right = True,
    rc={'font.family': 'SimHei'})

def upbreak(tsLine, tsRefLine):
    """
    向上突破
    :param tsLine: 收盘价序列 
    :param tsRefLine: 唐奇安上通道
    :return: 
    """
    n = min(len(tsLine), len(tsRefLine))
    tsLine = tsLine[-n:]
    tsRefLine = tsRefLine[-n:]
    signal = pd.Series(np.nan, index=tsLine.index)
    for i in range(1, len(tsLine)):
        if all([tsLine.iloc[i]>tsRefLine.iloc[i], tsLine.iloc[i-1]<tsRefLine.iloc[i-1]]):
            signal.iloc[i] = tsLine.iloc[i]+0.2
    return(signal)

def downbreak(tsLine, tsRefLine):
    """
    向下突破
    :param tsLine:
    :param tsRefLine:
    :return:
    """
    n = min(len(tsLine), len(tsRefLine))
    tsLine = tsLine[-n:]
    tsRefLine = tsRefLine[-n:]
    signal = pd.Series(np.nan, index=tsLine.index)
    for i in range(1, len(tsLine)):
        if all([tsLine.iloc[i] < tsRefLine.iloc[i], tsLine.iloc[i-1] > tsRefLine.iloc[i-1]]):
            signal.iloc[i] = -1
    return(signal)


if __name__ == '__main__':
    print("donchian_channel...")

    stock_name = "大众公用"
    symbol = "600635"
    start_time="19700101"
    end_time="20251219"
    size = 160
    n = 20 # 时间跨度

    # 1、获取股票的日线数据
    stock_daily_df = get_daily_df(symbol, start_time, end_time)

    # 2、计算均线数据
    stock_daily_df = calc_sma(stock_daily_df)
    print(stock_daily_df)

    # 3、提取收盘价、最高价、最低价
    Close = stock_daily_df["Close"]
    High = stock_daily_df["High"]
    Low = stock_daily_df["Low"]

    # 4、设定上、下、中通道线初始值
    upDc = pd.Series(0.0,index=Close.index)
    downDc = pd.Series(0.0, index=Close.index)
    midDc = pd.Series(0.1, index=Close.index)

    # 5、求唐奇安上、中、下通道
    for i in range(20,len(Close)):
        upDc.iloc[i] = max(High[(i-20):i])
        downDc.iloc[i] = min(Low[(i - 20):i])
        midDc.iloc[i] = 0.5*(upDc.iloc[i]+downDc.iloc[i])

    # 6、计算买卖信号
    UpBreak = upbreak(Close[upDc.index[0]:], upDc)
    DownBreak = downbreak(Close[downDc.index[0]:], downDc)

    apds = [
        mpf.make_addplot(stock_daily_df['SMA5'].tail(size), panel=0, color='white', width=1, label='SMA5'),
        mpf.make_addplot(stock_daily_df['SMA10'].tail(size), panel=0, color='yellow', width=1, label='SMA10'),
        mpf.make_addplot(stock_daily_df['SMA20'].tail(size), panel=0, color='darkviolet', width=1, label='SMA20'),
        mpf.make_addplot(stock_daily_df['SMA30'].tail(size), panel=0, color='royalblue', width=1, label='SMA30'),
        mpf.make_addplot(stock_daily_df['SMA60'].tail(size), panel=0, color='red', width=1.2, label='SMA60'),
        mpf.make_addplot(stock_daily_df['SMA120'].tail(size), panel=0, color='goldenrod', width=1.3, label='SMA120'),
        mpf.make_addplot(stock_daily_df['SMA250'].tail(size), panel=0, color='lime', width=1.3, label='SMA250'),
        # 显示唐奇安通道
        mpf.make_addplot(upDc.tail(size), panel=0, color='snow', width=1.3, linestyle='--', label='upper'),
        mpf.make_addplot(midDc.tail(size), panel=0, color='snow', width=1.3, linestyle='--', label='mid20'),
        mpf.make_addplot(downDc.tail(size), panel=0, color='snow', width=1.3, linestyle='--', label='lower'),
        # 显示唐奇安通道的买卖信号
        mpf.make_addplot(UpBreak.tail(size), type='scatter', markersize=100, marker='^', color='red', panel=0),
        mpf.make_addplot(DownBreak.tail(size), type='scatter', markersize=100, marker='v', color='green', panel=0),
    ]

    mpf.plot(stock_daily_df.tail(size),
             type='candle',
             style=my_style,
             title=stock_name + " - 唐奇安通道",
             figsize=(22, 14),
             ylabel="价格",
             ylabel_lower="成交量",
             datetime_format='%Y-%m-%d',
             addplot=apds,
             volume=True,
             show_nontrading=False)