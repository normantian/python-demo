def is_palindrome_v3(s):
    """(str) -> bool
    return true if and only if s is a palindrome
    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """
    i = 0
    j = len(s) - 1

    while i<j and s[i] == s[j]:
        i = i + 1
        j = j - 1
    return j <= i

def is_palindrome_v2(s):
    """(str) -> bool
    return true if and only if s is a palindrome
    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """
    n = len(s)
    return s[:n // 2] == reverse(s[n-n//2:])
    
def reverse(s):
   rev = ''
   for ch in s:
       rev = ch + rev
   return rev

    