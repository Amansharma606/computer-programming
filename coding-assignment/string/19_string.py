# Question = 19 Check if a string starts and ends with the same character.

def starts_and_ends_same(s):
    return s[0] == s[-1] if s else False


print(starts_and_ends_same("level"))  
print(starts_and_ends_same("hello"))  
