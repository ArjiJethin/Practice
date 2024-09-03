my_tuple = ("Apple", "Berries", "Cherries","Dragon", "Espanol", "Forange")
my_list = list(my_tuple)
num_list = [1, 2, 3, 4]
sting_tuple = ("One", "Two", "Three", "Four")

# print(my_tuple)
# print(type(my_tuple))
# print(my_list)
""" (A, B, C) = my_tuple
print(A)
print(B)
print(C) """
"""" (A, B, *C) = my_tuple
print(A)
print(B)
print(C) """
print(set(zip(num_list, sting_tuple)))

