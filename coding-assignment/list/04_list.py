#  Question = 4  Flatten a nested list.

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))  
        else:
            flattened.append(item)
    return flattened

nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(nested_list)) 