# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : mpl_kline_demo1.py
@time    : 2025/12/8 00:28
@desc    : mplfinance库绘制K图示例
-----------------------------------------------------------------------
"""


import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def kline(symbol, start_time, end_time, stock_name):
    # 利用 AKShare 获取股票的后复权数据，这里只获取前 6 列
    stock_hfq_df = ak.stock_zh_a_hist(symbol,period="daily",start_date=start_time,end_date=end_time)

    #print(stock_hfq_df)

    # 转换日期格式
    stock_hfq_df['Data'] = pd.to_datetime(stock_hfq_df['日期'])
    stock_hfq_df.set_index('Data', inplace=True)

    # 重命名列（英文列名更方便处理）
    stock_hfq_df = stock_hfq_df.rename(columns={
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
    print(df)

    # 创建一个marketcolors对象,并设置颜色参数
    marketcolors = mpf.make_marketcolors(up='red', down='green', volume='inherit')

    style = mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=marketcolors, edgecolor='k', rc={'font.family': 'SimHei'})

    mpf.plot(df,type='candle',style=style,title=stock_name+"k线图",
             ylabel="价格",
             ylabel_lower="成交量",
             datetime_format='%Y-%m-%d',
             mav=(5, 10, 20), volume=True, show_nontrading=False)



if __name__ == '__main__':
    print("mpl_kline_demo1...")
    kline("600635", "20250901", "20260105", "大众公用");
