'''
字符串优化
使用join 不要使用+=

from time import time

t = time()

s = ""
list = ['a','b','b','d','e','f','g','h','i','j','k','l','m'  ,'n']
for i in range (10000):
   for substr in list:
       s += substr
print "total run time:"
print time()-t
'''
'''
优化后
'''
from time import time
t = time()

s = ""
list = ['a','b','b','d','e','f','g','h','i','j','k','l','m'  ,'n']
for i in range (10000):
    s.join(list)
print "total run time:"
print time()-t

#建议格式化字符串
out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)


#避免
out = "<html>" + head + prologue + query + tail + "</html>"

#如果需要交换两个变量的值使用 a,b=b,a 而不是借助中间变量 t=a;a=b;b=t；
