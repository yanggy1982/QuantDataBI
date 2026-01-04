# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_sse_stock_list_async.py
@time    : 2025/12/9 22:14
@desc    : 并行异步获取上证股票列表
-----------------------------------------------------------------------
"""

import aiohttp
import asyncio

# 主板A
url_main_board_a = "https://query.sse.com.cn/sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_GP_L&type=inParams&CSRC_CODE=&STOCK_CODE=&REG_PROVINCE=&STOCK_TYPE=1&COMPANY_STATUS=2,4,5,7,8"

# 主板B
url_main_board_b = "https://query.sse.com.cn/sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_GP_L&type=inParams&CSRC_CODE=&STOCK_CODE=&REG_PROVINCE=350000&STOCK_TYPE=2&COMPANY_STATUS=2,4,5,7,8"

# 科创板
url_star_market = "https://query.sse.com.cn/sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_GP_L&type=inParams&CSRC_CODE=&STOCK_CODE=&REG_PROVINCE=350000&STOCK_TYPE=8&COMPANY_STATUS=2,4,5,7,8"

# 暂停上市
url_pause = "https://query.sse.com.cn//sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_ZTGP_L&type=inParams&STOCK_CODE=&REG_PROVINCE=&STOCK_TYPE=1,2&COMPANY_STATUS=5"

# 终止上市
url_stop = "https://query.sse.com.cn//sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_ZZGP_L&type=inParams&STOCK_CODE=&REG_PROVINCE=&STOCK_TYPE=1,2&COMPANY_STATUS=3"

request_headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer':'http://www.sse.com.cn/assortment/stock/list/share/'
}

async def download_file(url,filename):
    async with aiohttp.ClientSession() as session:
        print(f"Start download file from {url}")
        async with session.get(url,headers=request_headers) as response:
            assert response.status == 200
            with open(filename, "wb") as f:
                while True:
                    chunk = await response.content.readany()
                    if not chunk:
                        break
                    f.write(chunk)
            print(f"Downloaded {filename} from {url}")

async def main():
    await asyncio.gather(
        download_file(
            url_main_board_a,
            "sse_stock_a_list.xlsx",
        ),
        download_file(
            url_main_board_b,
            "sse_stock_b_list.xlsx",
        ),
        download_file(
            url_star_market,
            "sse_stock_sm_list.xlsx",
        ),
        download_file(
            url_pause,
            "sse_stock_pause_list.xlsx",
        ),
        download_file(
            url_stop,
            "sse_stock_stop_list.xlsx",
        ),
    )

if __name__ == '__main__':
    print("get_sse_stock_list_async...")
    asyncio.run(main())
