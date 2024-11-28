# Question = 18 Write a function to check if a number is an Armstrong number.

def is_armstrong(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == number


print(is_armstrong(153)) 
print(is_armstrong(370)) 
print(is_armstrong(123))  
