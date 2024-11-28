# Question = 13 Find all permutations of a string.

import itertools

def find_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]


print(find_permutations("abc"))  
