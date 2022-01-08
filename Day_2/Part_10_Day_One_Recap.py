# PART 10: Overview of day 1
# https://github.com/Alexsteele4121/Python_Tutorials/tree/main/Day_1

# Different math operators:
# Exponent:             **          5 ** 2 = 25
# Modulus(Remainder):   %           5 % 2 = 1
# Division:             /           5 / 2 = 2.5
# Integer Division:     //          5 // 2 = 2
# Multiplication:       *           5 * 2 = 10
# Subtraction:          -           5 - 2 = 3
# Addition:             +           5 + 2 = 7

# Different (entry level) data types:
# Integer (int):                    -2, -1, 0, 1, 2, 3, 4, 5
# Floating-point number (float):    -1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25
# String (str):                     "testing", 'String Values', 'cats', 'dogs'

# Assigning variables:
x = 9  # Using a single '=' to declare a variable
y: int  # Use a ':' to declare what kind of variable (Not necessary, only used for max efficiency)
z: float = 1.5  # You can declare the variable and the variable type at the same time

first_name = 'Alex'  # String Values require quotations when being declared
last_name = "Steele"  # Single and double quotations both work
full_name = first_name + ' ' + last_name  # Use the '+' to add strings together

# Basic functions
# The print function will output almost any datatype to our 'standard out' which in this case is our console
print('Print this out to the console')
print(9 + 10)

# The input function will prompt the user to enter text (which we can store in a string)
response = input('Is this where the prompt goes? ')
print(response)

# The 'len' function will return the number of values in a dataset
print('There are', len('abcdefghijklmnopqrstuvwxyz'), 'characters in the alphabet.')

# Different comparison operators:
# Equal:                    ==
# Not equal:                !=
# Greater than:             >
# Greater than or equal:    >=
# Less than:                <
# Less than or equal:       <=

# IF ELSE and ELIF
# An if statement takes a condition and determines whether its True or False
i = 1
if i == 1:
    print('This will only execute if the condition was true')

# An elif (or 'else if') statement only gets considered if the previous conditions all return False
if 0 < i < 5:
    print('i was between 0 and 5!')
elif i == 5 or i == 6:
    print('i was equal to 5 or 6')
elif i == 7 and i == 8:
    print('this will never execute')

# An else statement will run if none of the statements before it were executed.
if input('What\'s your name? ') == 'Alex':
    print('Your name is Alex! Yay')
else:
    print('ACCESS DENIED')

# Loops
# For loops can be used to iterate over different datatypes (lists, tuples, dictionaries, sets, or strings)
my_animals = ['Coors', 'Grizzly', 'Blue']  # This is a list datatype. A list can store any datatype within it.
for animal in my_animals:  # This will iterate over all the names in the list, storing its current selection in 'animal'
    print('I have a pet named ' + animal)  # The animal variable can be called upon anywhere within the loop

# While loops will run until the condition provided returns false
x = 5
while x > 0:
    x -= 1
    print('This will run', x, 'more time(s)!')

# Testing for empty or zero values
# If you pass a variable into an 'if' statement and there is nothing to compare,
# it will check whether the variable has anything in it. In the case it's a number it will
# check if the value is equal to 0. If there's nothing in it (or it's equal to zero) it
# will return false.

# All these values will return false.
a = False
b = ''
c = None
d = []  # Square brackets are 'lists'
e = ()  # Parenthesis are 'tuples'
f = {}  # Curly brackets are 'dictionaries'
g = 0
h = 0.0

test_case = [a, b, c, d, e, f, g, h]

for case in test_case:
    if case:
        print(f"Got One! Number {test_case.index(case)} returned positive!")
print("\nThis test is complete.\n")

# Functions
# A function is a chunk of code that only runs when called upon.
# When creating a function you can set parameters that you want
# your function to accept.


def say_hello(n):
    print('Hello', n)
    print('You can put as much code in here as you want!')


name = input('What is your name? ')

say_hello(name)
say_hello('Alex')
