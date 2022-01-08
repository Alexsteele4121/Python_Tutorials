# PART 13: Importing Modules


# Modules are pre-writen code that we can load into our own script.
# A file containing a set of functions or objects that we want to include.
# To uses a module we first have to load it in with the import statement.
import my_test_module


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_test_module.get_odds(numbers))


# We can use the 'from' statement to clarify we want to import objects from this module
from my_test_module import get_evens
print(get_evens(numbers))


# We can use the 'as' statement to rename what we just imported
from my_test_module import my_lucky_number as lucky
print(lucky)


# Python has a large number of modules already installed on your system called the 'Standard Library'
# Here's a full list if you'd like to dig deeper: https://docs.python.org/3/library/
# If you're importing a module from the standard library you don't have to specify any path.
# Python has its own path, multiple locations where it will check for the selected module.

# from random import randint
# print(randint(1, 10))
