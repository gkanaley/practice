# Lists - Introduction to data structures
from typing import List

my_list = ["1", "2", "3", "10", "1", "20", "22", "100"]
second_list: List[int] = [2, 1, 3, 5, 4, 6]
my_bool = False

# 0 index of a list is the first object in a list
print("First value in my_list:", my_list[0])

# To get last item, use the -1 index
print("Last value in second_list", second_list[-1])

# Adds value to the end of the list
var1 = my_list.append("0")
print("Added value to the end of my_list", my_list)

# Pop removes the last item added to the list and returns it
last_item_in_list = my_list.pop()
print("Value from pop():", last_item_in_list)
print("The values in list after the pop:", my_list)

# Sorts strings alphabetically, sorts numbers numerically
my_list.sort()
print(my_list)

second_list.sort()
print(second_list)

# Count gives the count of how many times something is in a list
print(my_list.count("1"))

# If you append a list into a list, it will add the list object itself into the list
my_list.append(second_list)
print(my_list)

my_list.pop()

# To take the values out of one list and place them into another list, use extend
my_list.extend(second_list)
print(my_list)
