# Question = 14 Extract all digits from a string.

def extract_digits(s):
    return ''.join(char for char in s if char.isdigit())


print(extract_digits("abc123def456"))  
