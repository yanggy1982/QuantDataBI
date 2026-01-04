# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : time_parse.py
@time    : 2025/12/8 00:04
@desc    : 使用Time-NLPY库语义时间解析
-----------------------------------------------------------------------
"""

from TimeNormalizer import TimeNormalizer

if __name__ == '__main__':
    print("time_parse...")

    tn = TimeNormalizer()

    res = tn.parse(target='下周三下午两点30分五秒')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target='2013年二月二十八日下午四点三十分二十九秒',
                   timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target='我需要大概33天2分钟', timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target='1月末')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target='明天')
    print(res)
