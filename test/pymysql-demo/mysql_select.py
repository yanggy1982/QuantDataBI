# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : mysql_select.py
@time    : 2025/12/7 20:12
@desc    : MySQL数据库select示例
-----------------------------------------------------------------------
"""

import pymysql

if __name__ == '__main__':
    print("mysql_select...")

    # 连接数据库
    db = pymysql.connect(host="localhost",port=3306, user="root", password="Happy123#", database="stock_db")

    # 使用cursor()方法创建一个游标对象
    cursor = db.cursor()

    # 使用execute()方法执行SQL语句
    cursor.execute("SELECT * FROM td_trade_date")

    # 使用fetall()获取全部数据
    data = cursor.fetchall()

    # 打印获取到的数据
    print(data)

    # 关闭游标和数据库的连接
    cursor.close()
    db.close()

