# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : get_szse_stock_a_list_async.py
@time    : 2025/12/9 22:28
@desc    : 
-----------------------------------------------------------------------
"""

import aiohttp
import asyncio

url = "https://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=1110&TABKEY=tab1&random=0.60175023464362"

szse_stock_list_file = 'szse_stock_a_list.xlsx'

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
    await download_file(url,szse_stock_list_file)

if __name__ == '__main__':
    print("get_szse_stock_a_list_async...")
    asyncio.run(main())