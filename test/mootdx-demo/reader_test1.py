# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : reader_test1.py
@time    : 2025/12/22 00:27
@desc    : 
-----------------------------------------------------------------------
"""

from mootdx.quotes import Quotes

if __name__ == '__main__':
    print("reader_test1...")

    # 创建行情客户端
    client = Quotes.factory(market='std')

    # 获取K线数据
    kline_data = client.bars(symbol='002611', frequency=9)

    print(kline_data)
