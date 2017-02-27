# encoding: utf-8
import MySQLdb

#打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")
# 使用 cursor()方法获取操作游标
cursor = db.cursor()
#使用execute方法执行SQL
cursor.execute("SELECT VERSION()")
#使用fetch获取一条数据
data = cursor.fetchone()

print "Database version : %s" %data
#关闭数据库
db.close()
