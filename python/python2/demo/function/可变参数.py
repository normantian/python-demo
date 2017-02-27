'''
numbers 为可变参数
可变参数可以传入0个或任意个参数，这些可变参数调用时自动组装成一个tuple。
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

nums = [1,2,3,4]
print calc(*nums)

nums = (1,2,3,4)
print calc(*nums)

print calc(1,2,3,4)


