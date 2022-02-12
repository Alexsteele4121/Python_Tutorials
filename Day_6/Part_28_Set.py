# PART 28: Sets

# A 'set' an unordered collection of unique elements. The items stored within it must be immutable.
# Sets are defined with curly brackets (Same way we define dictionaries but without keys)

data = {1, 1, 2, 3, 4, 4, 5}  # The duplicate values will be removed.
print(data)

# You can also convert objects into sets using the 'set()' function
my_list = [21, 20, 4, 6, 10, 5, 10]
my_set = set(my_list)  # This will also remove any of the duplicates
print(my_set)

