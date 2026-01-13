# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yangguangyuan
@file    : duckdb_demo1.py
@time    : 2026/1/7 10:04
@desc    : 从pandas dataframe转成polars dataframe
-----------------------------------------------------------------------
"""

import akshare as ak
import pandas as pd
import polars as pl
import duckdb
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # Mac系统
plt.rcParams['axes.unicode_minus'] = False


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

if __name__ == '__main__':
    print("duckdb_demo1...")

    stock_name = "大众公用"
    symbol = "600635"
    start_time = "19700101"
    end_time = "20260107"

    pd_df = get_stock_df(symbol=symbol, start_time=start_time, end_time=end_time, stock_name=stock_name)
    print(pd_df.tail())

    # 将 Pandas DataFrame 转换为 Polars DataFrame，并添加股票代码列
    pl_df = pl.from_pandas(pd_df.reset_index()).with_columns(
        pl.lit(stock_name).alias("symbol")  # 为每一行添加股票代码标识
    )

    print(pl_df.tail())  # 查看前几行数据

    # 连接到本地数据库文件，如果不存在会自动创建
    con = duckdb.connect("stocks.db")

    # 将 Polars DataFrame 直接加载为数据库表
    con.execute("""
        CREATE TABLE IF NOT EXISTS stocks AS SELECT * FROM pl_df
    """)

    # 验证数据是否成功导入
    row_count = con.execute("SELECT COUNT(*) FROM stocks").fetchone()
    print(f"表中的数据行数：{row_count[0]}")

    # 按股票代码分组，计算平均收盘价
    avg_close = con.execute(f"""
                            SELECT symbol, ROUND(AVG(Close), 2) AS avg_close
                            FROM stocks
                            where symbol = '{stock_name}'
                            GROUP BY symbol
                            """).fetchdf()

    print(f"平均收盘价: {avg_close}")

    # 找出成交量最大的5天，通常对应重大新闻或财报发布
    high_vol = con.execute(f"""
                           SELECT symbol, 日期, Volume,Close 
                           FROM stocks
                           where symbol = '{stock_name}'
                           ORDER BY Volume,symbol DESC LIMIT 5
                           """).fetchdf()

    print(f"找出成交量最大的5天: {high_vol}")

    # 计算20日滚动成交量加权平均价格（VWAP）
    vwap_query = """
        WITH daily_vwap AS (SELECT 日期,symbol,
                 SUM(Volume * Close) / SUM(Volume) AS vwap
             FROM stocks
             where symbol = '{stock_name}'
             GROUP BY 日期,symbol
        ),
        rolling_vwap AS (SELECT 日期,symbol,
                AVG(vwap) OVER (
                PARTITION BY symbol
                ORDER BY 日期
                ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
            ) AS rolling_20d_vwap
            FROM daily_vwap
        )
        SELECT * FROM rolling_vwap
        ORDER BY symbol, 日期
    """
    # 执行查询并转换为 Polars DataFrame
    vwap_df = pl.DataFrame(con.execute(vwap_query).fetchdf())
    vwap_df = vwap_df.rename({"日期": "Date"})

    # 绘制 20 日滚动 VWAP 趋势图
    vwap_df.to_pandas().plot(x="Date", y="rolling_20d_vwap", title="20日滚动VWAP")
    plt.show()