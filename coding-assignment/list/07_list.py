# Question = 7 Find the second largest element in a list.


def second_largest(lst):
    unique_elements = list(set(lst))  
    unique_elements.sort()  
    return unique_elements[-2] if len(unique_elements) >= 2 else None

list1 = [10, 20, 4, 45, 99, 99]
second_largest_element = second_largest(list1)

print(second_largest_element)