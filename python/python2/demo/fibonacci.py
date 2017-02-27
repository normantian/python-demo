# -*- coding: utf-8 -*-
def fib(N):
    a,b = 0,1
    # a=0 b=1
    for i in xrange(N):
        yield a
        a,b = b,a+b
##    while a < N:
##        yield a
##        a, b = b, a+b
        #a=b b=a+b

if __name__=='__main__':
    for i in fib(10):
        print i,',',
