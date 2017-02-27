'''
To change a sequence you are iterating over while inside the loop (for example to duplicate certain items),
it is recommended that you first make a copy.
Looping over a sequence does not implicitly make a copy.
The slice notation makes this especially convenient:

'''
words = ['cat', 'window', 'defenestrate']

for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.remove(w)

print words
