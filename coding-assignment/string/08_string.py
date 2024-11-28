# Question = 8 Remove duplicate characters from a string.

def remove_duplicates(s):
    return ''.join(dict.fromkeys(s))


print(remove_duplicates("hello"))  
print(remove_duplicates("aabbcc")) 
