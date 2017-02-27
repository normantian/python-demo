# encoding: utf-8
import MySQLdb

#打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")
# 使用 cursor()方法获取操作游标
cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE FIRST_NAME='%s'" % ('Norman')

try:
    #执行sql
    cursor.execute(sql)
    #提交
    db.commit()
except:
    db.rollback()
#关闭数据库连接
db.close()
