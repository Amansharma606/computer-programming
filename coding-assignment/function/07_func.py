# Question = 7 Write a function to find the largest number in a list.

def find_largest(numbers):
    if not numbers: 
        return None  
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 1, 4, 1, 5, 9, 2]))  
