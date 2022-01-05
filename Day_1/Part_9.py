# PART 9: Functions

# A function is a chunk of code that only runs when called upon.
# When creating a function you can set parameters that you want
# your function to accept.

def say_hello(name):
    print('Hello', name)
    print('You can put as much code in here as you want!')


name = input('What is your name? ')

say_hello(name)
say_hello('Alex')
