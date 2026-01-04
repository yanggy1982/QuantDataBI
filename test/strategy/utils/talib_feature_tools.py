# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : talib_feature_tools.py
@time    : 2025/12/21 13:45
@desc    : ta-lib技术因子工具库
-----------------------------------------------------------------------
"""

import talib

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


