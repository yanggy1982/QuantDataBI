# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : mysql_insert_demo1.py
@time    : 2025/12/7 22:06
@desc    :  MySQL数据库insert示例1
-----------------------------------------------------------------------
"""

import pymysql

if __name__ == '__main__':
    print("mysql_insert_demo1...")

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
    cursor.execute(sql, ("bob", "123"))

    db.commit()  # 提交数据
    cursor.close()
    db.close()
