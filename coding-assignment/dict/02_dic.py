# Question = 2 Sort a dictionary by its keys.

my_dict = {'b': 2, 'a': 1, 'c': 3}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
print(sorted_dict) 