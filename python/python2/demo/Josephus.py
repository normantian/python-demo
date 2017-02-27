# -*- coding: utf-8 -*-
def Josephus_1(n,k):
    '''(number,number) -> NoneType
        return Josephus cycle kill sequence
        Josephus_1(5,3)
        kill: 3
        kill: 1
        kill: 5
        kill: 2
        survivor: 4
    '''
	#n个人的列表
    link = range(1,n+1)
    ind = 0
    for i in range(n-1):
        ind = (ind+k-1) % len(link)
        #ind -= 1
        #if ind==-1:
        #   ind = len(link)-1
        print 'kill:',link[ind]
        del link[ind]
        #if ind==-1:
        #    ind=0
    print 'survivor:',link[0]

def Josephus(n,k):
    '''(number,number) -> NoneType
        return Josephus cycle kill sequence
        Josephus(5,3)
        kill: 3
        kill: 1
        kill: 5
        kill: 2
        survivor: 4
    '''
	#n个人的列表
    link = range(1,n+1)
    ind = 0 #开始的index
    for i in range(n-1):
        ind = (ind+k-1) % len(link)
        #ind -= 1
        #if ind==-1:
        #   ind = len(link)-1
        print 'kill:',link[ind]
        del link[ind]
        #if ind==-1:
        #    ind=0
    print 'survivor:',link[0]

def Josephus2(n,k):
    '''(number,number) -> NoneType
        n 人数
        k 报数
        return Josephus survivor
        Josephus(5,3)
        survivor: 4
    '''
    last = 0
    for i in range(2,n+1):
        last = (last+k)%i
    last += 1 
    print 'survivor:',last

def Josephus3(N,M,K=1):
    '''(number,number,number) -> NoneType
        return Josephus cycle kill sequence
        N 人数
        M 报数
        K 开始的编号
        Josephus3(5,3,2)
        kill: 4
        kill: 2
        kill: 1
        kill: 3
        survivor: 4
    '''
    queue = range(1,N+1)
    count = K-1 #开始的index
    for i in range(N-1):
        count = (count+M-1) % len(queue)
        print 'OUT: ', str(queue[count])
        del queue[count]
    print 'WIN:',str(queue[0])

if __name__ == '__main__':
    Josephus(5,64)
    print '-'*20
    Josephus2(5,4)
    print '-'*20
    #Josephus3(5,3,2)
    print '-'*20
    #Josephus_1(5,5)
