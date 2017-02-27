# encoding: utf-8
import MySQLdb

#打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")
# 使用 cursor()方法获取操作游标
cursor = db.cursor()

'''
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES ('Mac','Mohan', 20, 'M', 2000)"""
'''
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) \
      VALUES ('%s','%s','%d','%c','%d')" %\
      ('Norman','Tian',20,'M',2000)

try:
    #执行sql
    cursor.execute(sql)
    #提交
    db.commit()
except:
    db.rollback()
#关闭数据库连接
db.close()
