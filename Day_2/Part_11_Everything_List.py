# PART 11: Lists

# Lists are one of the most flexable datatypes in python. A list can store any other datatype within it.
# All you have to do to create a list is put comma-separated values between square brackets:

list_1 = [1, 2, 3, 4, 5]
list_2: list[str] = ['A', 'B', 'C', 'D', 'E']  # Use a : to declare what kind of variable.
list_3 = [1, 2, 3, ['A', 'B', 'C'], 2.5 + 2.5]

list_of_list = [list_1, list_2, list_3]
for list in list_of_list:
    print(list)
# Retrieving specific the values within list:
my_list = [1, 2, ['A', 'B'], 2.5 + 1.5]
# Index Values: [0 = 1, 1 = 2, 2 = ['A', 'B'], 3 = 4.0]

print(my_list[0])
print(my_list[0:2])  # prints out a range of values starting at 0 and stopping at 2 (will not include the second index)
print(my_list[0:4:2])  # The third value represents how to increment the index

# You can also call on a list with negative integers.
# -1 would be the last item in the list, -2 would be the second to last and so on.
my_list = [1, 2, ['A', 'B'], 2.5 + 1.5]
# Index Values: [-4 = 1, -3 = 2, -2 = ['A', 'B'], -1 = 4.0]

print(my_list[-1])
print(my_list[-1:-3:-1])  # The third value defaults to 1, so we have to specify we want to increment by -1
print(my_list[::-1])  # This will reverse the entire list

# Reassigning values in a list:
my_list = [20, 30, 40, 50]

my_list[0] = my_list[0] - 10  # Is the same as: my_list[0] -= 10
my_list[1] = 25
print(my_list)

# Different list methods:
my_list = [10, 20, 30]

my_list.append(10)  # Add an item to the end of a list
my_list.insert(0, 100)  # Insert an item. In this case at index 0
my_list.remove(10)  # Removes the selected item from the list. Only removes the first instance found
my_list.extend([1, 2, 3])  # Merges two list together
my_list.reverse()  # Reverses the order of the list
my_list.sort(key=lambda x: x)  # Sorts the items of a list relative to what the key function returns

item1 = my_list.pop(0)  # Removes an item at the specified index and returns it as a value
item2 = my_list.index(10)  # Returns the first position of the selected item
item3 = my_list.count(20)  # Returns how many times an item is in a list

my_list.clear()  # Removes all the items in the list

