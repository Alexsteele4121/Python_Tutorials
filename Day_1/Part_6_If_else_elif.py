# PART 6: IF ELSE and ELIF

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
