# Question = 16 Capitalize the first and last letters of a word.

def capitalize_first_last(s):
    if len(s) > 1:
        return s[0].upper() + s[1:-1] + s[-1].upper()
    return s.upper()  

print(capitalize_first_last("hello")) 
