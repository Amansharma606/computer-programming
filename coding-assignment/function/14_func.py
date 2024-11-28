# Question = 14 Write a function to find the sum of digits of a number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


print(sum_of_digits(12345))
print(sum_of_digits(-987)) 