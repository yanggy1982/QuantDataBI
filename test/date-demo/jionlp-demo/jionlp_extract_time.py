# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : jionlp_extract_time.py
@time    : 2025/12/8 00:17
@desc    : JioNLP语义时间解析时间提取
-----------------------------------------------------------------------
"""

import time
import jionlp as jio

if __name__ == '__main__':
    print("jionlp_extract_time...")

    text = '【新华社报2021-9-9】南方都市报今天发布了2021年8月份全国CPI（居民消费价格指数）和PPI（工业生产者出厂价格指数）数据。'
    res = jio.ner.extract_time(text, time_base={'year': 2021})
    print(res)
