# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : ak_data_tools.py
@time    : 2025/12/21 13:36
@desc    : 使用akshare获取数据工具函数
-----------------------------------------------------------------------
"""

import akshare as ak
import pandas as pd

def get_daily_df(symbol, start_time, end_time):
    """
    利用 AKShare 获取股票的后复权数据
    :param symbol:
    :param start_time:
    :param end_time:
    :return:
    """
    stock_df = ak.stock_zh_a_hist(symbol, period="daily", start_date=start_time, end_date=end_time)

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
