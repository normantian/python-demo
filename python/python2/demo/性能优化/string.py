'''
�ַ����Ż�
ʹ��join ��Ҫʹ��+=

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
�Ż���
'''
from time import time
t = time()

s = ""
list = ['a','b','b','d','e','f','g','h','i','j','k','l','m'  ,'n']
for i in range (10000):
    s.join(list)
print "total run time:"
print time()-t

#�����ʽ���ַ���
out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)


#����
out = "<html>" + head + prologue + query + tail + "</html>"

#�����Ҫ��������������ֵʹ�� a,b=b,a �����ǽ����м���� t=a;a=b;b=t��
