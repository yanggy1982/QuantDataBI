# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_stock_cyq_em.py
@time    : 2026/1/5 00:02
@desc    : 获取股票的筹码帆布
-----------------------------------------------------------------------
"""

import akshare as ak

if __name__ == '__main__':
    print("get_stock_cyq_em...")

    # stock_cyq_em
    # 1、说明：从东方财富网获取筹码分布
    # 2、输入参数
    # symbol	str	symbol="000001"; 股票代码
    # adjust	str	adjust=""; choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
    # 3、输出参数
    # 日期	object	-
    # 获利比例	float64	-
    # 平均成本	float64	-
    # 90成本-低	float64	-
    # 90成本-高	float64	-
    # 90集中度	float64	-
    # 70成本-低	float64	-
    # 70成本-高	float64	-
    # 70集中度	float64	-
    stock_cyq_em_df = ak.stock_cyq_em(symbol="600635", adjust="")
    print(stock_cyq_em_df)
