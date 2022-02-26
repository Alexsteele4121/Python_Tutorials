# PART 30: Pickle Data
import pickle

# Pickle is a part of python's standard library.
# It is used to store a python object structure such as lists, dict, tuples, class attributes, etc. into
# a file that we can load back into our code at a later point.

file = 'data.pickle'
data = ['Testing', input('Whats your name: ')]

with open(file, 'wb') as f:
    pickle.dump(data, f)  # Serializing the data and storing it to the file


with open(file, 'rb') as f:
    saved_data = pickle.load(f)  # Deserializing the data and storing it in the new variable

print(saved_data)


