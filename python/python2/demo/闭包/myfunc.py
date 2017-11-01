#coding:utf-8
def dec(func):
    def in_dec(*arg): #my_sum
        print 'in dec arg=',arg
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec

@dec #装饰器
def my_sum(*arg):
    '''
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val,int):
            return 0
    '''
    return sum(arg)

@dec
def my_avg(*arg):
    '''
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val,int):
            return 0
    '''
    return float(sum(arg)) / len(arg)

#my_sum = in_dec(*arg)
#dec return  in_dec -> my_sum
print my_sum(1,2,3,4)
print my_avg(1,2,3,4)


print my_avg(1,2,3,[2,3,4],'13',4)
'''
my_sum = dec(my_sum)
my_avg = dec(my_avg)

print my_sum(1,2,3,4)
print my_sum(1,2,3,4,'5')

print my_avg(1,2,3,4)
'''
