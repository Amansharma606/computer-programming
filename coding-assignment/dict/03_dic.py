# Question = 3 Sort a dictionary by its values.

my_dict = {'b': 2, 'a': 1, 'c': 3}


sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
print(sorted_dict)  