# Question = 18 Count the number of words in a string.

def count_words(s):
    words = s.split()
    return len(words)

print(count_words("The quick brown fox"))  
