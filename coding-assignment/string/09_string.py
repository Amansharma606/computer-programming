# Question = 9 Find the longest word in a sentence.

def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(find_longest_word("The quick brown fox jumps over the lazy dog"))  
