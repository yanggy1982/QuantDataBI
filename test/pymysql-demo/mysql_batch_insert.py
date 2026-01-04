# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : mysql_batch_insert.py
@time    : 2025/12/7 22:10
@desc    : MySQL数据库批量insert示例
-----------------------------------------------------------------------
"""

import pymysql

if __name__ == '__main__':
    print("mysql_batch_insert...")

    config = {
        "host": "localhost",
        "user": "root",
        "port": 3306,
        "password": "Happy123#",
        "database": "stock_db"
    }
    # 连接数据库
    db = pymysql.connect(**config)

    # 使用cursor()方法创建一个游标对象
    cursor = db.cursor()

    sql = "INSERT INTO td_accout(username,passwd) VALUES(%s,%s)"
    cursor.executemany(sql, [("tom", "123"), ("alex", '321')])

    db.commit()  # 提交数据
    cursor.close()
    db.close()
