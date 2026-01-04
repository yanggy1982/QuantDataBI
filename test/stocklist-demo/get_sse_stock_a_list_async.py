# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_sse_stock_a_list_async.py
@time    : 2025/12/9 21:47
@desc    : 异步方式获取上证股票列表
-----------------------------------------------------------------------
"""
url = "https://query.sse.com.cn/sseQuery/commonExcelDd.do?sqlId=COMMON_SSE_CP_GPJCTPZ_GPLB_GP_L&type=inParams&CSRC_CODE=&STOCK_CODE=&REG_PROVINCE=&STOCK_TYPE=1&COMPANY_STATUS=2,4,5,7,8"

request_headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer':'http://www.sse.com.cn/assortment/stock/list/share/'
}

import aiohttp
import asyncio

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
    await download_file(url,"sse_stock_a_list.xlsx")

if __name__ == '__main__':
    print("get_sse_stock_a_list_async...")
    asyncio.run(main())
