# -*- coding: utf-8 -*-
#杨辉三角
def yanghui(n=3):
    arr = []
    for i in xrange(n):
        arr.append([])
    for b in xrange(n):
        for c in xrange(b+1):
            if b==c or c==0:
                #arr[b][c] = 1
                arr[b].append(1)
            else:
                arr[b].append( arr[b-1][c-1] + arr[b-1][c])
    #print(arr)
    return arr
#
def yanghui_trangle(n):
    def _yanghui_trangle(n,result):
        if n == 1:
            return [1]
        else:
            #我们在列表2端各补了一个0，然后计算相邻项的和，就可以直接得到结果。
            return [sum(i) for i in zip([0]+result,result+[0])]

    pre_result=[]
    
    for i in xrange(1,n+1):
        pre_result = _yanghui_trangle(i,pre_result)
        yield pre_result

if __name__=='__main__':
    array = yanghui(10)
    for i in xrange(len(array)):
        for j in xrange(len(array[i])):
            print array[i][j],
        print '\n'
    print '-'*30
    for line in yanghui_trangle(10):
        print line
    print '-'*30
