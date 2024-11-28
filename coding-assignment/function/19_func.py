# Question = 19 Write a function to calculate the LCM of two numbers.

import math

def lcm(a, b):
    
    return abs(a * b) // math.gcd(a, b)


print(lcm(12, 15))  
print(lcm(7, 5))  