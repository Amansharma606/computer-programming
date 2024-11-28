# Question = 8 Rotate a list by n positions.

def rotate_list(lst, n):
    n = n % len(lst) 
    return lst[-n:] + lst[:-n]


list1 = [1, 2, 3, 4, 5]
rotated_list = rotate_list(list1, 2)

print(rotated_list)
