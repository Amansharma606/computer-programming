# Question = 14  Find the cumulative sum of a list.

import itertools

def cumulative_sum(lst):
    return list(itertools.accumulate(lst))

list1 = [1, 2, 3, 4, 5]
cum_sum = cumulative_sum(list1)

print(cum_sum)