# -*- coding: utf-8 -*-
from collections import OrderedDict

d = {1:'z',2:'y',3:'z'}
print sorted(d.items(),key=lambda x : x[1])

sorted_d = OrderedDict(sorted(d.items(),key=lambda x : x[1]))

print sorted_d


'''
    小写字母在大写字母之前
    所有字母在数字之前
    所有奇数在偶数之前
'''

s = "Sorting1234"

s1 = "".join(sorted(s,key=lambda x : (x.isdigit(),x.isdigit() and int(x)  % 2 == 0, x.isupper(),x.islower(),x)))

print s1

def reverseBits(n):
    bit_str = '{0:032b}'.format(n)
    reverse_str = bit_str[::-1]
    return int(reverse_str,2)

print reverseBits(0)
print '{0:032b}'.format(100)
