# Question = 15 Remove the smallest and largest elements

def remove_smallest_largest(lst):
    if len(lst) > 2:
        lst.remove(min(lst))  
        lst.remove(max(lst)) 
    return lst

list1 = [1, 2, 3, 4, 5]
result = remove_smallest_largest(list1)

print(result)