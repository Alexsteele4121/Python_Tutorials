# PART 22: Function Arguments Indepth:

# A function is a chunk of code that only runs when called upon.
# When creating a function you can set arguments that you want your function to accept.

# You can also set optional arguments with default values:

def remove(text: str, char: str = ' ', case_sensitive: bool = True):
    # the variables 'char' and 'case_sensitive' are optional.
    index_list = []
    string_to_check = text if case_sensitive else text.upper()
    char_to_check = char if case_sensitive else char.upper()

    while char_to_check in string_to_check:
        index_list.append(string_to_check.find(char_to_check))
        string_to_check = string_to_check.replace(char_to_check, '', 1)
    result = ''

    for count, index in enumerate(index_list):
        if not count:
            result += text[0:index]
        else:
            result += text[index_list[count - 1] + (len(char) * count): index + (len(char) * count)]

    result += text[index_list[-1] + (len(char) * len(index_list)):] if index_list else text
    return result


print('Removing Spaces:', remove('I want to remove all spaces from my text'))
print('Removing \'Hello\':', remove('Hello everyone!', 'hello', case_sensitive=False))


# Receiving an unknown amount of arguments / keyword arguments:

# A single wildcard (asterisk) will grab any arguments that do not have a keyword
# A double wildcard will grab any arguments given with a keyword
def print_this(*args, **kwargs):
    # The arguments will be stored in a tuple:
    print(args)
    # We can also 'unpack' those arguments with a single asterisk:
    print(*args, sep=' | ')

    # Keyword arguments will be stored in a dictionary:
    print(kwargs)
    # You can unpack dictionaries with a double asterisk:
    # **kwargs


print('\n' * 4)  # Adding a spacer
print_this('Coors', 'Grizzly', 'Blue', Hello='Alex', time='6:30')



