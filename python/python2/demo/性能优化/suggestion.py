from collections import defaultdict
from datetime import datetime
from datetime import date
context = defaultdict(list)
#setdefault 一次只能设置一个值，但是好处是可以使用链式语法，但是defaultdict更快

context = {}
context.setdefault('name_list',[]).append('Fiona')

print context

name_list = ['kevin','robin']
context = {}.fromkeys(name_list,9)

print context

context = dict.fromkeys([1,2],True)

print context

#列表去重复快速方法
list1 = [1,2,3,12,3,4,2,3,4]
print {}.fromkeys(list1).keys()

# 列表深拷贝
a = [1,2,3]
b = a[:]

#字典深拷贝
a ={'male':0,'female':1}
b = a.copy()

#取今天的年月日时间,下面两种代码效果相同
n_date = datetime.now().date()
n2_date= datetime.today().date()

print '%s,%s' %(n_date,n2_date)

#date -> datetime
b = datetime.combine(n_date,datetime.min.time())
print b

#计算日期差
d0 = date(2016,3,21)
d1 = date(2016,2,14)
delta = d0-d1
print delta.days

#map作为iterator
m1 = map(None,xrange(3),xrange(10,12))
print m1

print zip(xrange(3),xrange(10,12))

#判断奇数偶数
a = 1
if a&1:
    print '%s is even' %a




