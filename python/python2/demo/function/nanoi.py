# 利用递归函数移动汉诺塔:
def hanot(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    hanot(n-1, a, c, b) #将前n-1个盘子从a移动到b上
    print('move', a, '-->', c) #将最底下的最后一个盘子从a移动到c上
    hanot(n-1, b, a, c) #将b上的n-1个盘子移动到c上

hanot(4, 'A', 'B', 'C')