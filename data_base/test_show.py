# -*- coding: UTF-8 -*-
import MySQLdb as mdb
import sys
#连接mysql，获取连接的对象
con = mdb.connect('10.10.111.229', 'root', 'root', 'wincenter');
with con:
    #仍然是，第一步要获取连接的cursor对象，用于执行查询
    cur = con.cursor()
    #类似于其他语言的query函数，execute是python中的执行查询函数
    #cur.execute("SELECT * FROM SYS_USER ")

    #"INSERT INTO DATA_CENTER(DATA_CENTER_ID, DATA_CENTER_NAME, WCE_ADDRESS, WCE_PORT, WCE_ACCOUNT,WCE_PASSWORD,) VALUES(1, '姚明', 25);"
    cur.execute("SELECT * FROM DATA_CENTER ")

    #使用fetchall函数，将结果集（多维元组）存入rows里面
    rows = cur.fetchall()
    #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
    for row in rows:
        print row