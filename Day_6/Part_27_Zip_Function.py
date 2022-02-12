# PART 27: Zip Function

# The 'zip()' function takes any number of iterator objects (list, tuples, strings, etc..) and pairs
# the items with the same index together and returns a zip object.

names = ['Coors', 'Grizzly', 'Blue']
age = [5, 2, 4]

pets = zip(names, age)

print(pets)  # The zip object is not rendered until iterated over or turned into a list/tuple
for pet in pets:
    print(pet)


# When the iterator objects that are passed in are not the same length, the object with the shortest length will
# decide the length of the new zip object.

characters = ['Fry', 'Leela', 'Amy', 'Farnsworth', 'Zoidberg', 'Bender']
casted = ['Billy', 'Katey', 'Lauren', 'Billy', 'Billy']

futurama = zip(characters, casted)

print(futurama)
print(tuple(futurama))
