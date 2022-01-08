# PART 7: Loops

# For loops can be used to iterate over different datatypes (lists, tuples, dictionaries, sets, or strings)
my_animals = ['Coors', 'Grizzly', 'Blue']  # This is a list datatype. A list can store any datatype within it.
for animal in my_animals:  # This will iterate over all the names in the list, storing its current selection in 'animal'
    print('I have a pet named ' + animal)  # The animal variable can be called upon anywhere within the loop

# While loops will run until the condition provided returns false
x = 5
while x > 0:
    x -= 1
    print('This will run', x, 'more time(s)!')
