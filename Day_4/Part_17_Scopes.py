# PART 17: Scopes

# Python has a certain order that it will search for your variables.
# This is called the "LEGB Rule." Which stands for Local, Enclosing, Global, and Built-in.

#       - Local Scope: Any variable defined within a function (or lambda) will be considered a local variable.
#                      This will be where python will search for a specified variable before moving on.
print('\nTesting Local Variables:')
x = 'Global x'


def func():
    x = 'Local x'
    print(f'{x=}')


func()
print(f'{x=}')

#       - Enclosing Scope: This is a special case that only exist if you have a nested function. In this case
#                          python will check your current function for local variables, if it doesn't find it
#                          there then python will check the enclosing function.

print('\nTesting Enclosing Variables:')
y = 'Global y'


def outer_func():
    y = 'Enclosing y'

    def inner_func():

        print(f'{y=}')

    inner_func()
    print(f'{y=}')


outer_func()
print(f'{y=}')

#       - Global Scope: Any variable declared at the "top level" of the scrip will be visible from anywhere
#                       within your code. After python can not find your variable at the local or enclosing
#                       level, it will then look at the global level

print('\nTesting Global Variables:')
z = 'Global z'


def outer_func():

    def inner_func():
        print(f'{z=}')

    inner_func()
    print(f'{z=}')


outer_func()
print(f'{z=}')

#       - Built-in Scope: These are objects that are loaded in by python (keywords, functions, exceptions, ex..)
#                         Its important to not overwrite these because the original object will not be accessible
#                         afterwards.

print('\nPrinting Built-ins:\n')

import builtins
print(*[builtin for builtin in dir(builtins) if '__' not in builtin and builtin.islower()], sep=', ')
