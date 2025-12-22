# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_trade_date.py
@time    : 2025/12/7 19:13
@desc    : 获取交易日信息
-----------------------------------------------------------------------
"""

import akshare as ak
import datetime
from datetime import date
import pandas as pd
import time

def get_trade_date(N=80):
    """
    获取最近N个交易日的开始日期和结束日期
    :param N: 最近N个交易日，默认80
    :return:
    """
    today = date.today()
    trade_date_df = ak.tool_trade_date_hist_sina()
    #print(trade_date_df.head(20))
    trade_date_list = trade_date_df["trade_date"].astype(str).tolist()
    while str(today) not in trade_date_list:  # 如果当前日期不在交易日期列表内，则当前日期天数减一
        today = today - datetime.timedelta(days=1)

    end_date = str(today)[:4] + str(today)[5:7] + str(today)[8:10]

    start_date_index = trade_date_list.index(str(today)) - N
    start_date = trade_date_list[start_date_index][:4] + trade_date_list[start_date_index][5:7] + trade_date_list[
        start_date_index][8:10]
    print("结束时间", start_date)
    print("开始时间", end_date)
    return trade_date_list[start_date_index:start_date_index + N + 1]

if __name__ == '__main__':
    print("get_trade_date...")
    df = get_trade_date(N=10)
    print(df)
























