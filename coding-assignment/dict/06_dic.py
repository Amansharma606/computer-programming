# Question = 6 Invert keys and values in a dictionary.

my_dict = {"a": 1, "b": 2, "c": 3}


inverted_dict = {v: k for k, v in my_dict.items()}

print(inverted_dict)