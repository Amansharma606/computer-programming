# Question = 7 Check if a string is an anagram of another string.

def is_anagram(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))    
