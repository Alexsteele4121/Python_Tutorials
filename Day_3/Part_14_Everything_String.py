# PART 14: Everything Strings

# Strings are anything surrounded by quotes. Single and double quotes are seen as the same thing.
if 'test' == "test":  # Single vs double quote
    print('They are the same.')


# String operators:
#   +   Joins strings together
print('Test' + 'ing')
#   *   Repeats the string for as many times as specified
print('Hello' * 5)


# Checking if a string is in a string:
name = 'Alexander Benjamin Steele'
if 'Alex' in name:
    print('Yay! Alex is in your name')

if 's' not in name:
    print('Your name doesn\'t contain "s"')


# Escape characters in python (and most other languages) are represented with a backslash.
#   \n = newline            Most common, just moves the following text to the next line
#   \t = tab                Same as the tab key on your keyboard. Used to indent text
#   \b = backspace          Used to delete the previous character
#   \r = carriage return    Used to return to the start of the current line.
#   \' = single quote       Used to print a single quote, so we don't exit the string
#   \" = double quote       Used to print a double quote, so we don't exit the string
#   \\ = backslash          Used in the case we don't want to escape our string but just print a backslash: \\n


# We can prefix our strings with different characters to change how they are handled.
#   f'{}'                   Formatted string, anything expressions we put inside the braces will be replaced
#                           with their values:
name = 'Alex'
print(f'My name is {name}!')

#   r''                     Raw string, any escape character will be stored as raw text:
print(r'print a newline \n')

#   b''                     Bytes string, converts the string into a 'bytes' datatype
print(b'testing')  # Same as 'testing'.encode('utf8')


# If you have a large multiline string, you can use triple quotes:
s = """Multiline string will also keep their format when stored. So when you go the the next line
it will store that in memory as a 'newline'"""
print(s)


# Retrieving specific values from a string. Indexing strings is identical to how we index list:
my_name = 'Alex Steele'
print(my_name[0])
print(my_name[5:11])
print(my_name[::-1])


# String methods (all string methods return new values. They do not change the original string)
# If you would like to dig deeper into any of these methods, here is a good link:
# https://www.w3schools.com/python/python_ref_string.asp

# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# decode()          Return a decoded version of the string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Converts the elements of an iterable into a string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning

