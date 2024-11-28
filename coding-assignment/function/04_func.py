# Question = 4 Write a function to generate Fibonacci numbers up to n.

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print(fibonacci(20))  