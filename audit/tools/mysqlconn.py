#!/usr/bin/env python
import mysql.connector

def mysql_conn(cmd):
        conn=mysql.connector.connect(host='10.4.16.227',user='zabbix',passwd='zabbixadmin',db='audit',port=3306,charset='utf8')
        cur=conn.cursor()
        count=cur.execute(cmd)
        result=cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result
