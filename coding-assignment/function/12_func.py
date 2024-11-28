# Question = 12 Write a function to calculate the sum of squares of numbers in a list.

def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

print(sum_of_squares([1, 2, 3, 4]))  
