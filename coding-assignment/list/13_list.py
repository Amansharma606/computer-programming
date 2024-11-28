# Question = 13 Generate all subsets of a list.

import itertools

def generate_subsets(lst):
    subsets = []
    for r in range(len(lst) + 1): 
        subsets.extend(itertools.combinations(lst, r))
    return [list(subset) for subset in subsets]

list1 = [1, 2, 3]
subsets = generate_subsets(list1)

print(subsets)