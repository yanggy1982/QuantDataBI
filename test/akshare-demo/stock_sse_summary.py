# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : stock_sse_summary.py
@time    : 2025/12/3 00:33
@desc    : 
-----------------------------------------------------------------------
"""

import akshare as ak
from akshare import stock_sse_summary

if __name__ == '__main__':
    print("stock_sse_summary...")

    stock_sse_summary = ak.stock_sse_summary()
    print(stock_sse_summary)