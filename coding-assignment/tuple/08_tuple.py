# Question = 8 Slice a tuple.

my_tuple = (0, 1, 2, 3, 4, 5, 6)

slice1 = my_tuple[2:5]
print(slice1)  

slice2 = my_tuple[1:6:2]
print(slice2)  

slice3 = my_tuple[:3]
print(slice3)  
slice4 = my_tuple[4:]
print(slice4)  

reversed_tuple = my_tuple[::-1]
print(reversed_tuple) 