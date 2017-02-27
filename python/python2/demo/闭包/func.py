#coding:utf-8
passline = 60
def func(val):
    if val >= passline:
        print 'pass'
    else:
        print 'failed'
    def in_func():
        print val
    in_func()
    return in_func

def func_100(val):
    passline = 60
    if val >= passline:
        print 'pass'
    else:
        print 'failed'
def func_150(val):
    passline = 90
    if val >= passline:
        print 'pass'
    else:
        print 'failed'

def set_passline(passline): 
    def cmp(val): #闭包，内置函数，实现封装和代码复用
        if val >= passline:
            print 'pass'
        else:
            print 'failed'
    return cmp

#f = func(89)
#f() #in_func

#print f.func_closure

#func_100(89)
#func_150(89)
f_100 = set_passline(60)

f_150 = set_passline(90)

f_100(89)
f_150(89)

