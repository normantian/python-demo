'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
'''
#阶乘
'''
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。
尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

尾递归调用时，如果做了优化，栈不会增长.
因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化.
所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


#懒惰的Python程序员
def fact(x):
    return x>1 and x * fact(x-1) or 1

#更懒的Python程序员
f = lambda x: x and x * f(x - 1) or 1
print f(6)

#Python 专家
facter = lambda x : reduce(int.__mul__, xrange(2,x+1),1)
print facter(4)

#专家级程序员
import cmath
print fact(6)


#Python 黑客
import sys
#@tailcall
def fact1(x, acc=1):
    if x: return fact1(x.__sub__(1), acc.__mul__(x))
    return acc
sys.stdout.write(str(fact1(6)) + '\n')
