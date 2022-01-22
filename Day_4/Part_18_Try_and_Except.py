# PART 18: try, except, else and finally

# In python we have the 'try' keyword which lets us test a code block for errors.
# 'try' must always be paired with either except or finally.

# Use the except code block will catch any specified errors and execute accordingly:
print('\nFirst try block:')

try:
    print(x)
except NameError as e:
    print(f'Undefined Value: {e}')

print('Got past the first try block!')


# The else code block will run if no errors were raised:
print('\nSecond try block:')

y = 2.5
try:
    print(f'{round(y)=}')
except TypeError as e:
    print(f'Invalid entry: {e}')
except Exception as e:
    print(f'Fatal Error: {e}')
    exit()
else:
    print('No errors occurred!')

print('Got past the second try block!')


# Code in the 'finally' block will run no matter what:
print('\nThird try block:')

z = 1
try:
    print(z.lower())
except AttributeError as e:
    print(f'Attribute Error: {e}')
finally:
    print('This will run no matter what happens!')

print('Got past the third try block!')
