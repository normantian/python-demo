def deco(func):
    def in_deco(x,y):
        print 'in deco'
        func(x,y)
    print 'call deco'
    return in_deco

#deco(bar) -> in_deco
#bar = in_deco
# bar in_deco bar
@deco
def bar(x,y):
    print 'in bar',x+y

bar(2,3)


'''
call deco
in deco
in bar 5
'''
