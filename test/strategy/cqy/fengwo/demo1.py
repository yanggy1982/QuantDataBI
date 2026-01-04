# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : demo1.py
@time    : 2026/1/5 01:05
@desc    : 
-----------------------------------------------------------------------
"""

import fengwo as fw
fw.showMsg(False)
from strategy.utils.ak_data_tools import get_daily_df

if __name__ == '__main__':
    print("demo1...")

    stock_name = "大众公用"
    symbol = "600635"
    start_time = "19700101"
    end_time = "20260106"

    # 1、获取股票的日线数据
    stock_daily_df = get_daily_df(symbol, start_time, end_time)
    print(stock_daily_df.head())

    # 计算90%获利盘的价格
    print(fw.COST(stock_daily_df['High'], stock_daily_df['Low'], stock_daily_df['Volume'], stock_daily_df['turnover'] / 100, 90))
    # 计算每日平均成本：
    print(fw.COST(stock_daily_df['High'], stock_daily_df['Low'], stock_daily_df['Volume'], stock_daily_df['turnover'] / 100, 50))

    # 计算收盘价的获利比例
    print(fw.RD(fw.WINNER(stock_daily_df['High'], stock_daily_df['Low'], stock_daily_df['Volume'], stock_daily_df['turnover'] / 100, stock_daily_df['Close']), 2))

