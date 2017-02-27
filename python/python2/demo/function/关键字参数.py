'''
关键字参数允许你传入0个或任意个含参数名的参数，这些参数在函数内部自动组装为一个dict

关键字参数可以扩展函数的功能
'''
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw


person('Michael', 30)

person('Bob', 35, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}

person('Jack', 24, **kw)
