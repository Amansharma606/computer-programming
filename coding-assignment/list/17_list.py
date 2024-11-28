#  Question = 17 Sort a list without using built-in functions.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        
        if not swapped:
            break
    return lst


list1 = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(list1)

print(sorted_list)