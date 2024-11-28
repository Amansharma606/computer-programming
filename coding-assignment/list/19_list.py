#  Question = 19 Find the difference between two lists.

def list_difference(list1, list2):
    return [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

difference = list_difference(list1, list2)

print(difference)