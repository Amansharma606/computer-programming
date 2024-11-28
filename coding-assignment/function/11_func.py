# Question = 11  Write a function to find the nth Fibonacci number.

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0  
    elif n == 2:
        return 1  

    a, b = 0, 1
    for _ in range(2, n):
        a
