def quicksort(array):
    less,greater=[],[]
    #greater=[]
    if len(array)<=1:
        return array
    pivot = array.pop()
    for x in array:
        if x<= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less)+[pivot]+quicksort(greater)

if __name__ == '__main__':
    a = quicksort([1,4,2,-1,0,4])
    print a
    print '-'*20
    b = quicksort(range(1,-10,-1))
    print b
    print b[::-1]
