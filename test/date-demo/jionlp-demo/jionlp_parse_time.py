# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : jionlp_parse_time.py
@time    : 2025/12/8 00:14
@desc    : JioNLP语义时间解析示例
-----------------------------------------------------------------------
"""

import time
import jionlp as jio

if __name__ == '__main__':
    print("jionlp_parse_time...")

    res = jio.parse_time('今年9月', time_base={'year': 2021})
    print(res)
    res = jio.parse_time('零三年元宵节晚上8点半', time_base=time.time())
    print(res)
    res = jio.parse_time('一万个小时')
    print(res)
    res = jio.parse_time('100天之后', time.time())
    print(res)
    res = jio.parse_time('每周五下午4点', time.time())
    print(res)

