# Question = 6 Write a function to count vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"   
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  