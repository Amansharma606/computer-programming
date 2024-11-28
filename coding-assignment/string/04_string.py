# Question = 4 Find the first non-repeated character in a string.

def first_non_repeated(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None  


print(first_non_repeated("swiss"))  
print(first_non_repeated("aabb"))   
