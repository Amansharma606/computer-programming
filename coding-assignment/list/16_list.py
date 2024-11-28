#  Question = 16 Count the occurrences of each element in a list.

from collections import Counter

def count_occurrences(lst):
    return Counter(lst)

list1 = [1, 2, 2, 3, 3, 3, 4]
occurrences = count_occurrences(list1)

print(occurrences)