# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_szse_stock_list_async.py
@time    : 2025/12/9 23:07
@desc    : 并行异步获取深圳股票列表
-----------------------------------------------------------------------
"""

import aiohttp
import asyncio

# 深圳A股
url_a = "https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1110&TABKEY=tab1&random=0.60175023464362"

# 深圳B股
url_b = "https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1110&TABKEY=tab2&random=0.6942996588777915"

# 暂停上市
url_pause = "https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1793_ssgs&TABKEY=tab1&random=0.5914423178287121"

# 终止上市
url_stop = "https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1793_ssgs&TABKEY=tab2&random=0.3621223816728716"

szse_stock_a_list_file = 'szse_stock_a_list.xlsx'

szse_stock_b_list_file = 'szse_stock_b_list.xlsx'

szse_stock_pause_list_file = 'szse_stock_pause_list.xlsx'

szse_stock_stop_list_file = 'szse_stock_stop_list.xlsx'

async def download_file(url,filename):
    async with aiohttp.ClientSession() as session:
        print(f"Start download file from {url}")
        async with session.get(url) as response:
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
            url_a,
            filename=szse_stock_a_list_file,
        ),
        download_file(
            url_b,
            filename=szse_stock_b_list_file,
        ),
        download_file(
            url_pause,
            filename=szse_stock_pause_list_file,
        ),
        download_file(
            url_stop,
            filename=szse_stock_stop_list_file,
        ),
    )

if __name__ == '__main__':
    print("get_szse_stock_list_async...")
    asyncio.run(main())
