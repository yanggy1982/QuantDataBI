# -*- coding:utf-8 -*-

"""
***********************************************************************

@author  : yanggy
@file    : mysql_delete.py
@time    : 2025/12/7 22:10
@desc    : MySQL数据库delete示例
-----------------------------------------------------------------------
"""

import pymysql

if __name__ == '__main__':
    print("mysql_delete...")

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

    sql = "delete from td_accout where id=3"
    cursor.execute(sql)

    db.commit()  # 提交数据
    cursor.close()
    db.close()
