# Question = 17 Find the frequency of characters in a string.

from collections import Counter

def character_frequency(s):
    return dict(Counter(s))

print(character_frequency("hello"))  