# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_trade_data_163.py
@time    : 2025/12/9 23:24
@desc    : 异步从163获取数据
-----------------------------------------------------------------------
"""

stock_code = "002611"

url = 'http://quotes.money.163.com/service/chddata.html?code=0{}'.format(stock_code)

import pandas as pd


# 沪市前面加0，深市前面加1，比如0000001，是上证指数，1000001是中国平安
def get_daily(code, start='19900101', end=''):
    url_mod = "http://quotes.money.163.com/service/chddata.html?code=%s&start=%s&end=%s"
    url = url_mod % (code, start, end)
    df = pd.read_csv(url, encoding='gb2312')
    return df


df = get_daily('0000001')

if __name__ == '__main__':
    print("get_trade_data_163...")

    print(df.head())
