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

#½¨Òé¸ñÊ½»¯×Ö·û´®
out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)


#±ÜÃâ
out = "<html>" + head + prologue + query + tail + "</html>"

#Èç¹ûÐèÒª½»»»Á½¸ö±äÁ¿µÄÖµÊ¹ÓÃ a,b=b,a ¶ø²»ÊÇ½èÖúÖÐ¼ä±äÁ¿ t=a;a=b;b=t£»
