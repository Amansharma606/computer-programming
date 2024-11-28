# Question = 17 Write a function to remove duplicates from a list.

def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 3, 2, 4, 5, 3]
print(remove_duplicates(my_list)) 