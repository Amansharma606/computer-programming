# Question = 20 Convert a string to binary representation.

def string_to_binary(s):
    return ' '.join(format(ord(char), '08b') for char in s)


print(string_to_binary("hello"))  
