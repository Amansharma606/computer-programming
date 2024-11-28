# Question = 13 Write a function to determine if a number is even or odd.

def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(4))  
print(is_even_or_odd(7)) 