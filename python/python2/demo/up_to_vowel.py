def get_answer(prompt):
    answer = raw_input(prompt)
    
# answer = input(prompt)
    while not (answer == 'yes' or answer == 'no'):
        answer = raw_input(prompt)
        # answer = input(prompt)
    return answer





def up_to_vowel2(s):
    # before_vowel contains all the characters found in s[0:i].
    before_vowel = ''
	
    # Accumulate the non-vowels at the beginning of the string.
    
    for ch in s :
        if not (ch in 'aeiouAEIOU'):
            before_vowel = before_vowel + ch

    return before_vowel

def up_to_vowel(s):
    """(str) -> str
	Return a substring of s from index 0 up to but not including the first
	vowel in s
	>>> up_to_vowel('hello')
	'h'
	>>> up_to_vowel('there')
	'th'
    """
	
    # before_vowel contains all the characters found in s[0:i].
    before_vowel = ''
    i = 0
	
    # Accumulate the non-vowels at the beginning of the string.
    
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel
