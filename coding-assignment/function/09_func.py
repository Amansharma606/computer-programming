# Question = 9  Write a function to calculate the area of a circle.

import math

def area_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative"
    return math.pi * radius ** 2


print(area_of_circle(5))  