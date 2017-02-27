'''
	默认参数 n=2
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
# 利用递归函数移动汉诺塔:
'''
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b) #将前n-1个盘子从a移动到b上
    print('move', a, '-->', c) #将最底下的最后一个盘子从a移动到c上
    move(n-1, b, a, c) #将b上的n-1个盘子移动到c上

move(4, 'A', 'B', 'C')
'''
