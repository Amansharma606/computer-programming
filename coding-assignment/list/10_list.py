# Question = 10 Check if a list is a palindrome.

def is_palindrome(lst):
    return lst == lst[::-1]


list1 = [1, 2, 3, 2, 1]
result = is_palindrome(list1)

print(result)