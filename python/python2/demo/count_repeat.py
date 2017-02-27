def shift_left(L):
    ''' list -> NoneType
    '''
    first_item = L[0]
    for i in range(1,len(L)):
        L[i-1] = L[i]

    L[-1] = first_item
    
def count_adjacent_repeats(s):

    repeats = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            repeats = repeats + 1

    return repeats
