import functools

def add_2(x):
    x += 2
    return x

def add(x, y):
    return x+y


my_list = ["Apple", "Berry", "Cherries", "DragonFruit", "Berry", "Cherries"]
conv_list = list(('A', 'B', 'C', 'D'))
diff_list = ["Apple", 12, True, 13.5, 'C']
conv_list.insert(4, 'E')
pop = conv_list.pop(4)
my_tuple = ('A', 'B', 'C')
sort_list = [1, 6, 3, 33, 45, 23, 12, 4]
sort_list.sort()
conv_list.insert(5, my_tuple)
new_list = my_list.copy()
# diff_list.reverse()
map_list = list(map(add_2, sort_list))


# print(my_list)
# print(conv_list)
# print(diff_list)
# print(type(diff_list))
# print(my_list[0])
# print(my_list[0::2])
# print(my_list[5:0:-1])
# print(pop)
# print("Return value: ", conv_list.pop())
# print(new_list)
# print(diff_list)
# print(sort_list)
"""for my_list in my_list:
    print(my_list)"""
"""for i in range(len(my_list)):
    print(my_list[i])"""
# print(map_list)
# print(functools.reduce(add, sort_list))

