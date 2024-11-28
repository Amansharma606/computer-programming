#  Question no 3  Check if a string is a palindrome.

def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

string = "radar"
print(is_palindrome(string))
