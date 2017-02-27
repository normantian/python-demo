import time
t1 = time.time()
print(t1)
nlist=range(0,9000000)
nlist=[float(i)/1000000 for i in nlist]
N=len(nlist)
sum1=0.0
sum2=0.0
for i in range(N):
    sum1+=nlist[i]
    sum2+=nlist[i]**2
mean=sum1/N
var=sum2/N-mean**2
print("var",var)
print("use time:", time.time() - t1)
