'''
	Ĭ�ϲ��� n=2
'''
def power(x,n=2):
    s = 1
    while n>0:
        n=n-1
        s=s*x
    return s
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
'''	
# ���õݹ麯���ƶ���ŵ��:
'''
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b) #��ǰn-1�����Ӵ�a�ƶ���b��
    print('move', a, '-->', c) #������µ����һ�����Ӵ�a�ƶ���c��
    move(n-1, b, a, c) #��b�ϵ�n-1�������ƶ���c��

move(4, 'A', 'B', 'C')
'''
