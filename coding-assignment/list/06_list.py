# Question = 6 Split a list into chunks of a specific size.

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunks = chunk_list(list1, 3)

print(chunks)