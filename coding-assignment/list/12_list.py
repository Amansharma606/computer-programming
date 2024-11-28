# Question = 12 Remove all even numbers from a list.


def remove_even_numbers(lst):
    return [x for x in lst if x % 2 != 0]

list1 = [1, 2, 3, 4, 5, 6]
filtered_list = remove_even_numbers(list1)

print(filtered_list)