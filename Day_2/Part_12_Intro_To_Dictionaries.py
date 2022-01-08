# PART 12: Dictionaries

# Python Dictionaries have almost the same syntax as JavaScript Object Notation (json)
# Dictionaries are used to store data values in key:value pairs, each comma-separated between curly brackets.

my_dictionary = {
    # key     :  # Value
    'object_1': 'Testing',
    'my pets': ['Coors', 'Grizzly', 'Blue'],  # Values can be any datatype
    0.5: 'one half'
}
print(my_dictionary)

# Common Methods of a dictionary:

print(my_dictionary.keys())  # Returns a list will all the keys
print(my_dictionary.values())  # Returns a list will all the values
print(my_dictionary.items())  # Returns a list of keys and values

# Below are all the methods of a dictionary. Here's a link if you'd like to dig deeper:
# https://www.w3schools.com/python/python_dictionaries_methods.asp

# .clear() Removes all the elements from the dictionary
# .copy() Returns a copy of the dictionary
# .fromkeys() Returns a dictionary with the specified keys and value
# .get() Returns the value of the specified key
# .items() Returns a list containing a tuple for each key value pair
# .keys() Returns a list containing the dictionary's keys
# .pop() Removes the element with the specified key
# .popitem() Removes the last inserted key-value pair
# .setdefault() Returns the value of the specified key.If the key does not exist insert the key with the specified value
# .update()	Updates the dictionary with the specified key-value pairs
# .values() Returns a list of all the values in the dictionary
