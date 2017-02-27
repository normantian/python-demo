import time
import numpy
t1 = time.time()
print(t1)
nlist=range(0,9000000)
nlist=[float(i)/1000000 for i in nlist]
N=len(nlist)
narray=numpy.array(nlist)
sum1=narray.sum()
narray2=narray*narray
sum2=narray2.sum()
mean=sum1/N
var=sum2/N-mean**2
print("var",var)
print("use time:", time.time() - t1)
