#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.100.166", "root", "root", "wincenter_zhengyi_sec", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
#cursor.execute("SELECT VERSION()")

#清除指定数据库表
cursor.execute("SELECT concat('DROP TABLE IF EXISTS ', table_name, ';') FROM information_schema.tables WHERE table_schema = 'wincenter_zhengyi_sec'");
rows = cursor.fetchall()
#依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
for row in rows:
    exeStr = str(row).split("'")[1]
    print exeStr
    cursor = db.cursor()
    cursor.execute(exeStr)
    #
    data = cursor.fetchone()
    print data
#
#cursor.execute("SHOW TABLES");

# 使用 fetchone() 方法获取一条数据
#data = cursor.fetchone()

# 关闭数据库连接
db.close()