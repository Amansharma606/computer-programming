# Question = 6 Count the occurrence of a specific word in a string.

def count_word_occurrences(s, word):
    return s.lower().split().count(word.lower())


print(count_word_occurrences("The cat chased the cat", "cat")) 
