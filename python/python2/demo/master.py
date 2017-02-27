# -*- coding: utf-8 -*-
#主元素算法
#先排序再判断中间值的出现次数是否大于L长度的50%
def master(L=None):
    """
    (L) -> element
    >>> master(None)
    None
    >>> master([])
    None
    >>> master([1,1,2,2])
    None
    >>> master([1,1,2])
    1
    >>> master([1,2,1,1])
    1
    """
    if L is None or len(L)==0:
        return None
    ls = sorted(L)
    n = len(L)
    count = 0
    seed = ls[n // 2]
    print 'seed=',seed

    for i in xrange(n):
        if seed == ls[i]:
            count = count +1
    print 'count=',count
    if count > n/2:
        return seed
    else:
        return None

def master_v2(L=None):
    """
    (L) -> element
    >>> master_v2(None)
    None
    >>> master_v2([])
    None
    >>> master_v2([1,1,2,2])
    None
    >>> master_v2([1,1,2])
    1
    >>> master_v2([1,1,2,2,1])
    1
    """
    if L is None or len(L)==0:
        return None
    ls = sorted(L)
    n = len(L)
    #count = 0
    seed = ls[n // 2]
    #print 'seed=',seed

    is_master = (lambda L,x : len([l for l in L if l==x]) > n // 2 )(ls,seed)
    #print 'is_master=',is_master
    if is_master:
        return seed
    else:
        return None
# 解决思路：在元素数组中，删去不同的两个元素，数组的主元素保持不变
def master_v3(L=None):
    """
    (L) -> element
    >>> master_v3(None)
    None
    >>> master_v3([])
    None
    >>> master_v3([1,1,2,2])
    None
    >>> master_v3([1,1,2])
    1
    >>> master_v3([1,1,2,2,1])
    1
    """
    if L is None or len(L)==0:
        return None
    n = len(L)
    seed = 0
    count = 0
    for i in xrange(n):
        if count == 0:
            seed = L[i]
            count = 1
        else:
            if seed == L[i]:
                count = count+1
            else:
                count = count-1
    is_master = (lambda L,x : len([l for l in L if l==x]) > n // 2 )(L,seed)
    #print 'is_master=',is_master
    if is_master:
        return seed
    else:
        return None
