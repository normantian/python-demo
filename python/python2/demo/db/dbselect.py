# encoding: utf-8
import MySQLdb

#打开数据库连接
db = MySQLdb.connect("localhost","root","root","test")
# 使用 cursor()方法获取操作游标
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

try:
     cursor.execute(sql)
     results = cursor.fetchall()
     for row in results:
         fname = row[0]
         lname = row[1]
         age = row[2]
         sex = row[3]
         income = row[4]
         print "fname={0},lname={1},age={2},sex={3},income={4}".format(fname,lname,age,sex,income)
except:
    print "Error: unable to fetch data"

db.close()
    
