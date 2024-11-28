#  Question = 20 Convert a list of integers to a single concatenated integer.

def list_to_concatenated_integer(lst):
    return int(''.join(map(str, lst)))


list1 = [1, 2, 3, 4]
concatenated_integer = list_to_concatenated_integer(list1)

print(concatenated_integer)