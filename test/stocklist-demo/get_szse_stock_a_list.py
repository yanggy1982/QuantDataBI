# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_szse_stock_a_list.py
@time    : 2025/12/9 21:31
@desc    : 获取深圳A股票列表
-----------------------------------------------------------------------
"""

from urllib import request

url = "https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1110&TABKEY=tab1&random=0.60175023464362"

szse_stock_list_file = 'szse_stock_list.xlsx'


if __name__ == '__main__':
    print("get_szse_stock_a_list...")

    # 1、判断临时文件是否存在，如果存在则删除

    # 2、下载文件
    request.urlretrieve(url, szse_stock_list_file)

    # 3、加载文件入库

