#  Question = 18 Check if two lists are identical.

def are_lists_identical(list1, list2):
    return list1 == list2


list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [4, 3, 2, 1]

result1 = are_lists_identical(list1, list2)  # True
result2 = are_lists_identical(list1, list3)  # False

print(result1)
print(result2)