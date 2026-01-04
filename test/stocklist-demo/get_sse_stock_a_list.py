# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_sse_stock_a_list.py
@time    : 2025/12/9 20:32
@desc    : 获取上证股票列表
-----------------------------------------------------------------------
"""
import requests

url = "https://query.sse.com.cn/sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_GP_L&type=inParams&CSRC_CODE=&STOCK_CODE=&REG_PROVINCE=&STOCK_TYPE=1&COMPANY_STATUS=2,4,5,7,8"

request_headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer':'http://www.sse.com.cn/assortment/stock/list/share/'
}

if __name__ == '__main__':
    print("get_sse_stock_a_list...")

    try:
        # 1、判断临时文件是否存在，如果存在则删除

        # 2、下载文件
        response = requests.get(url, headers=request_headers)
        with open("sse_stock_a_list.xlsx", "wb") as f:
            f.write(response.content)

        # 3、加载文件入库


    except requests.exceptions.HTTPError as errh:
        raise SystemExit(errh)
