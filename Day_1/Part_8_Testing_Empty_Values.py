# PART 8: Testing for empty or zero values

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
