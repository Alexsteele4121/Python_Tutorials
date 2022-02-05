# PART 23: Lambda:

# A lambda is an un-named function which can take any numer of arguments but only one expression:

multiply = lambda x, y: x * y
average = lambda *args: sum(args)/len(args)

print(multiply(5, 10))
print(average(10, 5, 20, 6))


my_pets = [{
               'name': 'Coors',
               'age': 5
           },
           {
               'name': 'Grizzly',
               'age': 2
           },
           {
               'name': 'Blue',
               'age': 4
           }]

# We can pass lambda functions as a argument:
sorted_list = sorted(my_pets, key=lambda pet: pet['age'])
print('Sorted by age:', sorted_list)
