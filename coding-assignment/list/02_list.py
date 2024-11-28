# Question no 2 Count the number of vowels in a string.

string = "Hello World"
vowel_count = sum(1 for char in string.lower() if char in "aeiou")
print(vowel_count)  
