# Question = 2 Check if a string is a palindrome.

def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
