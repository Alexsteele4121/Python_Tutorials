# PART 24: Files

# Python has a built-in 'open' function which return a file object.

# Different methods for opening a file:
# "r"  - Read
# "r+" - Read And Write
# "a"  - Append
# "w"  - Write
# "x"  - Create

# Specifying how the file should be handled:
# "t" - Text
# "b" - Binary

# More information here: https://www.w3schools.com/python/python_file_handling.asp


with open('test.txt', 'w') as f:
    for i in range(1, 10):
        f.write(f'Line Number {i}\n')

with open('test.txt', 'r') as f:

    # Read the entire file:
    print('\nReading all lines: ')
    print(f.read())
    # Reset the cursor back to the start:
    f.seek(0)

    # Retrieve a list containing all the lines in the file:
    print('\n\nRetrieving a list of lines: ')
    print(f.readlines())
    f.seek(0)

    # Iterate through the lines, this saves memory space:
    print('\n\nIterating through the lines (for loop):')
    for line in f:
        print(line, end='')
    f.seek(0)

    # # This only works in python version 3.8 and newer due to the 'walrus operator':
    # print('\n\nIterating through the lines (while loop): ')
    # while line := f.readline():
    #     print(line, end='')
    #     # Get the current cursor location
    #     print(f.tell())
    # f.seek(0)

