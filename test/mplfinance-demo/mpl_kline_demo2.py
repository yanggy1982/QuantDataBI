# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : mpl_kline_demo2.py
@time    : 2025/12/19 04:28
@desc    : mplfinance库绘制K图示例2
-----------------------------------------------------------------------
"""

import akshare as ak
import numpy as np
import talib
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


def get_stock_df(symbol, start_time, end_time, stock_name):
    """
    获取股票的日历史数据
    :param symbol:
    :param start_time:
    :param end_time:
    :param stock_name:
    :return:
    """
    # 利用 AKShare 获取股票的后复权数据，这里只获取前 6 列
    stock_df = ak.stock_zh_a_hist(symbol,period="daily",start_date=start_time,end_date=end_time)

    # 转换日期格式
    stock_df['Data'] = pd.to_datetime(stock_df['日期'])
    stock_df.set_index('Data', inplace=True)

    # 重命名列（英文列名更方便处理）
    stock_hfq_df = stock_df.rename(columns={
        '开盘': 'Open',
        '收盘': 'Close',
        '最高': 'High',
        '最低': 'Low',
        '成交量': 'Volume',
        '成交额': 'amount',
        '振幅': 'amplitude',
        '涨跌幅': 'pct_chg',
        '涨跌额': 'change',
        '换手率': 'turnover'
    })

    df = stock_hfq_df.sort_index()
    return df

def calc_sma(stock_df):
    # 计算各类均线
    stock_df["SMA5"] = talib.SMA(stock_df["Close"], timeperiod=5)
    stock_df["SMA10"] = talib.SMA(stock_df["Close"], timeperiod=10)
    stock_df["SMA20"] = talib.SMA(stock_df["Close"], timeperiod=20)
    stock_df["SMA30"] = talib.SMA(stock_df["Close"], timeperiod=30)
    stock_df["SMA60"] = talib.SMA(stock_df["Close"], timeperiod=60)
    stock_df["SMA120"] = talib.SMA(stock_df["Close"], timeperiod=120)
    stock_df["SMA250"] = talib.SMA(stock_df["Close"], timeperiod=250)

    stock_df['SMA5'] = stock_df['SMA5'].bfill()
    stock_df['SMA10'] = stock_df['SMA10'].bfill()
    stock_df['SMA20'] = stock_df['SMA20'].bfill()
    stock_df['SMA30'] = stock_df['SMA30'].bfill()
    stock_df['SMA60'] = stock_df['SMA60'].bfill()
    stock_df['SMA120'] = stock_df['SMA120'].bfill()
    stock_df['SMA250'] = stock_df['SMA250'].bfill()

    return stock_df

def calc_bbands(stock_df):
    """
    计算布林带
    :param stock_df:
    :return:
    """
    stock_df['upper'], stock_df['mid20'], stock_df['lower'] = talib.BBANDS(stock_df["Close"],
                                                         timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    return stock_df

def calc_kdj(stock_df):
    """
    计算KDJ
    :param stock_df:
    :return:
    """
    stock_df['K'], stock_df['D'] = talib.STOCH(stock_df['High'].values, stock_df['Low'].values, stock_df['Close'].values, fastk_period=9,
                                   slowk_period=3,
                                   slowk_matype=0, slowd_period=3, slowd_matype=0)
    stock_df['K'].bfill()
    stock_df['D'].bfill()
    stock_df['J'] = 3 * stock_df['K'] - 2 * stock_df['D']
    return stock_df

def calc_macd(stock_df):
    """
    计算MACD
    :param stock_df:
    :return:
    """
    dif, dea, bar = talib.MACD(stock_df['Close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    dif[np.isnan(dif)], dea[np.isnan(dea)], bar[np.isnan(bar)] = 0, 0, 0
    red_bar = np.where(bar > 0, bar, 0)
    blue_bar = np.where(bar <= 0, bar, 0)
    return dif, dea,bar, red_bar,blue_bar

if __name__ == '__main__':
    print("mpl_kline_demo2...")

    stock_name = "大众公用"
    symbol = "600635"

    # 1、获取历史数据
    stock_df = get_stock_df(symbol=symbol, start_time="19700101", end_time="20251219", stock_name=stock_name);
    # 2、计算各类均线
    stock_df = calc_sma(stock_df)
    # 3、计算布林线
    stock_df = calc_bbands(stock_df)
    # 4、计算KDJ
    stock_df = calc_kdj(stock_df)
    # 5、计算MACD
    dif, dea, bar, red_bar, blue_bar = calc_macd(stock_df)
    size = 160

    #print(stock_df[['SMA20', 'mid20']].tail(100))
    print(stock_df.tail(size))

    apds = [
        mpf.make_addplot(stock_df['SMA5'].tail(size), panel=0, color='white',width=1,label='SMA5'),
        mpf.make_addplot(stock_df['SMA10'].tail(size), panel=0, color='yellow', width=1,label='SMA10'),
        mpf.make_addplot(stock_df['SMA20'].tail(size), panel=0, color='darkviolet', width=1,label='SMA20'),
        mpf.make_addplot(stock_df['SMA30'].tail(size), panel=0, color='royalblue', width=1,label='SMA30'),
        mpf.make_addplot(stock_df['SMA60'].tail(size), panel=0, color='red', width=1.2,label='SMA60'),
        mpf.make_addplot(stock_df['SMA120'].tail(size), panel=0, color='goldenrod', width=1.3,label='SMA120'),
        mpf.make_addplot(stock_df['SMA250'].tail(size), panel=0, color='lime', width=1.3,label='SMA250'),
        # 显示布林带
        mpf.make_addplot(stock_df['upper'].tail(size), panel=0, color='snow', width=1.3,linestyle='--',label='upper'),
        mpf.make_addplot(stock_df['mid20'].tail(size), panel=0, color='snow', width=1.3, linestyle='--',label='mid20'),
        mpf.make_addplot(stock_df['lower'].tail(size), panel=0, color='snow', width=1.3, linestyle='--',label='lower'),
        # 显示KDJ
        mpf.make_addplot(stock_df['K'].tail(size), panel=2, color='darkviolet', width=1, label='K',ylabel='KDJ'),
        mpf.make_addplot(stock_df['D'].tail(size), panel=2, color='yellow', width=1, label='D'),
        mpf.make_addplot(stock_df['J'].tail(size), panel=2, color='white', width=1, label='J'),

        mpf.make_addplot(dif[-size:], panel=3, color='white', width=1, label='dif', ylabel='MACD'),
        mpf.make_addplot(dea[-size:], panel=3, color='yellow', width=1, label='dea'),
        mpf.make_addplot(bar[-size:], panel=3, color='gray',type="bar"),
        #mpf.make_addplot(blue_bar[-size:], panel=3, color='green', type="bar"),
    ]

    mpf.plot(stock_df.tail(size),
             type='candle',
             style=my_style,
             title=stock_name + "k线图",
             figsize=(22, 14),
             ylabel="价格",
             ylabel_lower="成交量",
             datetime_format='%Y-%m-%d',
             addplot=apds,
             volume=True,
             show_nontrading=False)
